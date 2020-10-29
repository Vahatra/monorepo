// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";
import "@openzeppelin/contracts/proxy/Initializable.sol";
import "@openzeppelin/contracts/introspection/IERC1820Registry.sol";
import "./Interfaces/IToken.sol";
import "./Interfaces/ITokenRecipient.sol";
import "./Interfaces/ITokenSender.sol";
import "./MixinNF.sol";
import "./SwapVerifier.sol";

contract Token is IToken, SwapVerifier, MixinNF, Initializable, Pausable, AccessControl {
    using Address for address;
    using SafeMath for uint256;

    /// token nonce
    uint256 internal nonce;

    /// mapping from token to creator
    mapping(uint256 => address) public creators;

    /// mapping from token to max index
    mapping(uint256 => uint256) public maxIndex;

    /// granularity for fungible tokens.
    uint256 internal granNF;

    IERC1820Registry private erc1820;

    /// balance
    mapping(uint256 => mapping(address => uint256)) internal balances;

    /// operators
    address[] internal arrayDefaultOperators;
    mapping(address => bool) internal isDefaultOperators;
    mapping(address => mapping(address => bool)) internal operators;
    mapping(address => mapping(address => bool)) internal revokedDefaultOperators;

    bytes32 private TOKENS_SENDER_INTERFACE_HASH;
    bytes32 private TOKENS_RECIPIENT_INTERFACE_HASH;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant BURNER_ROLE = keccak256("BURNER_ROLE");

    /// asserts token is owned by msg.sender
    modifier creatorOnly(uint256 _id) {
        require(creators[_id] == msg.sender, "NOT_CREATOR");
        _;
    }

    /// INIT

    function initialize(address[] calldata _defaultOperators, uint256 _granNF) external initializer {
        granNF = _granNF;
        arrayDefaultOperators = _defaultOperators;

        for (uint256 i = 0; i < arrayDefaultOperators.length; i++) {
            isDefaultOperators[arrayDefaultOperators[i]] = true;
        }

        TOKENS_SENDER_INTERFACE_HASH = keccak256("ITokenSender");
        TOKENS_RECIPIENT_INTERFACE_HASH = keccak256("ITokenRecipient");

        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /// OTHER

    function _checkGranularity(uint256 _amount) internal view {
        require(_amount % granNF == 0, "NOT_MULTIPLE_OF_GRANULARITY");
    }

    function granularity() external view returns (uint256) {
        return granNF;
    }

    function defaultOperators() external view returns (address[] memory) {
        return arrayDefaultOperators;
    }

    /// CREATE

    /// @dev creates a new token
    /// @param _isNF is non-fungible token
    /// @return type_ of token (a unique identifier)
    function create(bool _isNF) external whenNotPaused returns (uint256 type_) {
        require(hasRole(MINTER_ROLE, msg.sender), "CALLER_CANNOT_MINT_OR_CREATE");
        // Store the type in the upper 128 bits
        type_ = (++nonce << 128);

        // Set a flag if this is an NFI.
        if (_isNF) {
            type_ = type_ | TYPE_NF_BIT;
        }

        // This will allow restricted access to creators.
        creators[type_] = msg.sender;

        // emit a Sent event with Create semantic to help with discovery.
        emit Sent(msg.sender, address(0), address(0), type_, 0, "", "");
    }

    /// MINT

    /// @dev mints fungible tokens
    /// @param _id token type
    /// @param _to beneficiaries of minted tokens
    /// @param _amounts amounts of minted tokens
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function mintFungible(
        uint256 _id,
        address[] calldata _to,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external whenNotPaused creatorOnly(_id) {
        require(hasRole(MINTER_ROLE, msg.sender), "CALLER_CANNOT_MINT_OR_CREATE");
        require(isFungible(_id), "TRIED_TO_MINT_FUNGIBLE_FOR_NON_FUNGIBLE_TOKEN");
        // HERE need to check contract caller

        // mint tokens
        for (uint256 i = 0; i < _to.length; ++i) {
            // cache to reduce number of loads
            address to = _to[i];
            require(to != address(0), "CANNOT_MINT_FOR_ADDRESS_ZERO");
            uint256 amount = _amounts[i];

            // Grant the items to the caller
            balances[_id][to] = amount.add(balances[_id][to]);

            // Emit the Sent/Mint event.
            // the 0x0 source address implies a mint
            emit Minted(msg.sender, to, _id, amount, _data, _operatorData);
        }
    }

    /// @dev mints a non-fungible token
    /// @param _type token type
    /// @param _to beneficiaries of minted tokens
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function mintNonFungible(
        uint256 _type,
        address[] calldata _to,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external whenNotPaused creatorOnly(_type) {
        require(hasRole(MINTER_ROLE, msg.sender), "CALLER_CANNOT_MINT_OR_CREATE");
        // No need to check this is a nf type rather than an id since
        // creatorOnly() will only let a type pass through.
        require(isNonFungible(_type), "TRIED_TO_MINT_NON_FUNGIBLE_FOR_FUNGIBLE_TOKEN");

        // Index are 1-based.
        uint256 index = maxIndex[_type] + 1;

        for (uint256 i = 0; i < _to.length; ++i) {
            // cache to reduce number of loads
            address to = _to[i];
            require(to != address(0), "CANNOT_MINT_FOR_ADDRESS_ZERO");
            uint256 id = _type | (index + i);

            nfOwners[id] = to;

            // NFT base type balance
            balances[_type][to] = 1;

            emit Minted(msg.sender, to, id, 1, _data, _operatorData);
        }

        // record the `maxIndex` of this nft type
        // this allows us to mint more nft's of this type in a subsequent call.
        maxIndex[_type] = _to.length.add(maxIndex[_type]);
    }

    /// SEND

    /// @notice Send multiple types of Tokens in one transfer from msg.sender.
    /// @param _to      Target addresses
    /// @param _ids     IDs of each token type
    /// @param _amounts  Transfer amounts per token type
    /// @param _data    Additional data with no specified format
    function send(
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external whenNotPaused {
        _send(msg.sender, msg.sender, _to, _ids, _amounts, _data, "");
    }

    /// @notice Send multiple types of Tokens in one transfer from the _from address.
    /// @param _from    Source addresses
    /// @param _to      Target addresses
    /// @param _ids     IDs of each token type
    /// @param _amounts  Transfer amounts per token type
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function operatorSend(
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external whenNotPaused {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        _send(msg.sender, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Actually make the transfers.
    /// @param _operator msg.sender
    /// @param _from    Source addresses
    /// @param _to      Target addresses
    /// @param _ids     IDs of each token type
    /// @param _amounts  Transfer amounts per token type
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _send(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        // sanity checks
        require(_to != address(0x0), "CANNOT_TRANSFER_TO_ADDRESS_ZERO");
        require(_ids.length == _amounts.length, "IDS_AND_VALUES_LENGTH_MISMATCH");

        callSender(_operator, _from, _to, _ids, _amounts, _data, _operatorData);

        // perform transfers
        for (uint256 i = 0; i < _ids.length; ++i) {
            // Cache amount to local variable to reduce read costs.
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];

            if (isNonFungible(id)) {
                require(amount == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
                require(nfOwners[id] == _from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
                nfOwners[id] = _to;
                // Keep the balance of NF type in base type id
                uint256 baseType = getNonFungibleBaseType(id);
                balances[baseType][_from] = balances[baseType][_from].sub(amount);
                balances[baseType][_to] = balances[baseType][_to].add(amount);
            } else {
                _checkGranularity(amount);
                balances[id][_from] = balances[id][_from].sub(amount);
                balances[id][_to] = balances[id][_to].add(amount);
            }
            emit Sent(_operator, _from, _to, id, amount, _data, _operatorData);
        }

        callReceiver(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    /// SWAP

    /// @notice Swap tokens
    /// @param _swap Swap data
    /// @param _nonce Contract state required to match the signature
    /// @param _expiry Time at which to expire the signature
    /// @param _v Recovery byte of the signature
    /// @param _r Half of the ECDSA signature pair
    /// @param _s Half of the ECDSA signature pair
    /// @param _data    Additional data with no specified format
    function swap(
        SwapLib.Swap memory _swap,
        uint256 _nonce,
        uint256 _expiry,
        uint8 _v,
        bytes32 _r,
        bytes32 _s,
        bytes memory _data
    ) public whenNotPaused {
        address signer = SwapVerify(_swap, _nonce, _expiry, _v, _r, _s);
        _send(msg.sender, msg.sender, signer, _swap.senderTokenIds, _swap.senderTokenAmounts, _data, "");
        _send(signer, signer, msg.sender, _swap.signerTokenIds, _swap.signerTokenAmounts, _data, "");
    }

    /// BURN

    /// @notice Burn _value amount of an _id from msg.sender.
    /// @param _ids      IDs of the token type
    /// @param _amounts  Burn amounts
    /// @param _data     Additional data with no specified format
    function burn(
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external whenNotPaused {
        _burn(msg.sender, msg.sender, _ids, _amounts, _data, "");
    }

    /// @notice Burn _value amount of an _id from _from.
    /// @param _from    Source address
    /// @param _ids      ID of the token type
    /// @param _amounts   Burn amount
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function operatorBurn(
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external whenNotPaused {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        _burn(msg.sender, _from, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Actually make the burnning.
    /// @param _operator msg.sender
    /// @param _from    Source address
    /// @param _ids     IDs of the token type
    /// @param _amounts Burn amounts
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _burn(
        address _operator,
        address _from,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        require(_from != address(0), "CANNOT_BURN_FROM_ADDRESS_ZERO");
        require(hasRole(BURNER_ROLE, _operator), "CALLER_CANNOT_BURN");

        callSender(_operator, _from, address(0), _ids, _amounts, _data, _operatorData);

        // perform transfers
        for (uint256 i = 0; i < _ids.length; ++i) {
            // Cache amount to local variable to reduce read costs.
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];

            if (isNonFungible(id)) {
                require(amount == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
                require(nfOwners[id] == _from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
                nfOwners[id] == address(0);
                uint256 baseType = getNonFungibleBaseType(id);
                balances[baseType][_from] = balances[baseType][_from].sub(amount);
            } else {
                _checkGranularity(amount);
                balances[id][_from] = balances[id][_from].sub(amount);
            }
            emit Burned(_operator, _from, id, amount, _data, _operatorData);
        }
    }

    /// ERC1820

    function callSender(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) private {
        address impl = erc1820.getInterfaceImplementer(_from, TOKENS_SENDER_INTERFACE_HASH);
        if (impl != address(0)) {
            ITokenSender(impl).tokensToSend(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
        }
    }

    function callReceiver(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) private {
        address impl = erc1820.getInterfaceImplementer(_to, TOKENS_RECIPIENT_INTERFACE_HASH);
        if (impl != address(0)) {
            ITokenRecipient(impl).tokensReceived(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
        } else {
            require(!_to.isContract(), "RECIPIENT_NOT_IMPLEMENTING_INTERFACE");
        }
    }

    /// OPERATOR

    /// @notice Set a third party operator address as an operator of msg.sender to send
    /// and burn tokens on its behalf.
    /// @param _operator  Address to add to the set of authorized operators
    function authorizeOperator(address _operator) external whenNotPaused {
        require(msg.sender != _operator, "SENDER_ALREADY_HIS_OPERATOR");

        if (isDefaultOperators[_operator]) {
            revokedDefaultOperators[msg.sender][_operator] = false;
        } else {
            operators[msg.sender][_operator] = true;
        }
        emit AuthorizedOperator(_operator, msg.sender);
    }

    /// @notice Remove the right of the operator address to be an operator for msg.sender
    /// and to send and burn tokens on its behalf.
    /// @param _operator  Address to add to the set of authorized operators
    function revokeOperator(address _operator) external whenNotPaused {
        require(msg.sender != _operator, "SENDER_ALREADY_HIS_OPERATOR");
        if (isDefaultOperators[_operator]) {
            revokedDefaultOperators[msg.sender][_operator] = true;
        } else {
            operators[msg.sender][_operator] = false;
        }
        emit RevokedOperator(_operator, msg.sender);
    }

    /// @notice Queries whether the operator address is an operator of the holder address.
    /// @param _operator  Address of authorized operator
    /// @param _holder    The owner of the Tokens
    /// @return          True if the operator is approved, false if not
    function isOperatorFor(address _operator, address _holder) external view returns (bool) {
        return _isOperatorFor(_operator, _holder);
    }

    function _isOperatorFor(address _operator, address _holder) internal view returns (bool) {
        return
            _holder == _operator ||
            (isDefaultOperators[_operator] && !revokedDefaultOperators[_holder][_operator]) ||
            operators[_holder][_operator];
    }

    /// BALANCE

    /// @notice Get the balance of an account's Tokens.
    /// @param _owner  The address of the token holder
    /// @param _id     ID of the Token
    /// @return        The _owner's balance of the Token type requested
    function balanceOf(address _owner, uint256 _id) external view returns (uint256) {
        if (isNonFungibleItem(_id)) {
            return nfOwners[_id] == _owner ? 1 : 0;
        }
        return balances[_id][_owner];
    }

    /// @notice Get the balance of multiple account/token pairs
    /// @param _owners The addresses of the token holders
    /// @param _ids    ID of the Tokens
    /// @return balances_   The _owner's balance of the Token types requested
    function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids)
        external
        view
        returns (uint256[] memory balances_)
    {
        // sanity check
        require(_owners.length == _ids.length, "OWNERS_AND_IDS_LENGTH_MISMATCH");

        // get balances
        balances_ = new uint256[](_owners.length);
        for (uint256 i = 0; i < _owners.length; ++i) {
            uint256 id = _ids[i];
            if (isNonFungibleItem(id)) {
                balances_[i] = nfOwners[id] == _owners[i] ? 1 : 0;
            } else {
                balances_[i] = balances[id][_owners[i]];
            }
        }
        return balances_;
    }
}
