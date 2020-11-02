// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/introspection/IERC1820Registry.sol";
import "./libs/SwapLib.sol";
import "./interfaces/ITokenRecipient.sol";
import "./interfaces/ITokenSender.sol";
import "./Initializable.sol";
import "./MixinNF.sol";

/// @title Token contract
/// @notice This contract holds implementation logic for all token management
contract Token is MixinNF, Initializable {
    using Address for address;
    using SafeMath for uint256;
    using SwapLib for SwapLib.Swap;

    IERC1820Registry private erc1820;

    /// @dev Token nonce
    uint256 internal nonce;

    /// @dev mapping from token to creator.
    mapping(uint256 => address) public creators;

    /// @dev mapping from token to max index for non fungible tokens.
    mapping(uint256 => uint256) public maxIndex;

    /// @dev granularity for fungible tokens.
    uint256 internal gran;

    /// @dev mapping for balance of tokens and owner.
    mapping(uint256 => mapping(address => uint256)) internal balances;

    bytes32 private TOKEN_SENDER_INTERFACE_HASH;
    bytes32 private TOKEN_RECIPIENT_INTERFACE_HASH;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant BURNER_ROLE = keccak256("BURNER_ROLE");

    /// asserts token is owned by msg.sender
    modifier creatorOnly(uint256 _id) {
        require(creators[_id] == msg.sender, "NOT_CREATOR");
        _;
    }

    /// EVENT

    /// @dev create MUST emit when a token is created.
    /// Creator will always be msg.sender.
    event TokenCreated(address indexed creator, uint256 indexed id, bytes data);

    /// @dev emits IF uri is not empty on token creation.
    event TokenURI(string value, uint256 indexed id);

    /// @dev send/sendOperator MUST emit when tokens are transferred.
    /// Operator will always be msg.sender.
    event TokenSent(
        address operator,
        address indexed from,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );

    /// @dev mintFungible/mintNonFungible MUST emit when tokens are minted.
    /// Operator will always be msg.sender.
    event TokenMinted(
        address operator,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data
    );

    /// @dev burn/burnOperator MUST emit when tokens are burned.
    /// Operator will always be msg.sender.
    event TokenBurned(
        address operator,
        address indexed from,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );

    /// CONST

    constructor(uint256 _granularity) public {
        gran = _granularity;
    }

    /// @notice Creates a new token
    /// @param _sender  Address of the sender (msg.sender)
    /// @param _uri     URI of the token
    /// @param _isNF    is non-fungible token
    /// @param _data    Additional data with no specified format
    /// @return type_ Token type (a unique identifier)
    function create(
        address _sender,
        string calldata _uri,
        bool _isNF,
        bytes calldata _data
    ) external onlyImplementation returns (uint256 type_) {
        // Store the type in the upper 128 bits
        type_ = (++nonce << 128);

        if (_isNF) {
            type_ = type_ | TYPE_NF_BIT;
        }
        creators[type_] = _sender;

        emit TokenCreated(_sender, type_, _data);

        if (bytes(_uri).length > 0) {
            emit TokenURI(_uri, type_);
        }
    }

    /// @notice Mints fungible tokens
    /// @param _sender  Address of the sender (msg.sender)
    /// @param _to      Beneficiaries of minted tokens
    /// @param _id      Token type
    /// @param _amounts Amounts of minted tokens
    /// @param _data    Additional data with no specified format
    function mintFungible(
        address _sender,
        address[] calldata _to,
        uint256 _id,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyImplementation creatorOnly(_id) {
        require(isFungible(_id), "NON_FUNGIBLE_TOKEN");

        for (uint256 i = 0; i < _to.length; ++i) {
            address to = _to[i];
            require(to != address(0), "INVALID_ADDRESS");
            uint256 amount = _amounts[i];
            balances[_id][to] = amount.add(balances[_id][to]);

            emit TokenMinted(_sender, to, _id, amount, _data);
        }
    }

    /// @notice Mints a non-fungible token
    /// @param _sender  Address of the sender (msg.sender)
    /// @param _to      Beneficiaries of minted tokens
    /// @param _type    Token type (base type)
    /// @param _data    Additional data with no specified format
    function mintNonFungible(
        address _sender,
        address[] calldata _to,
        uint256 _type,
        bytes calldata _data
    ) external onlyImplementation creatorOnly(_type) {
        require(isNonFungible(_type), "FUNGIBLE_TOKEN");

        // Index are 1-based.
        uint256 index = maxIndex[_type] + 1;

        for (uint256 i = 0; i < _to.length; ++i) {
            address to = _to[i];
            require(to != address(0), "INVALID_ADDRESS");
            uint256 id = _type | (index + i);
            nfOwners[id] = to;
            // NFT base type balance
            balances[_type][to] = 1;

            emit TokenMinted(_sender, to, id, 1, _data);
        }

        // record the `maxIndex` of this nft type (base type).
        maxIndex[_type] = _to.length.add(maxIndex[_type]);
    }

    function send(
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyImplementation {
        _send(_from, _from, _to, _ids, _amounts, _data, "");
    }

    function operatorSend(
        address _operator,
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external onlyImplementation {
        _send(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    function burn(
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyImplementation {
        _burn(_from, _from, _ids, _amounts, _data, "");
    }

    function operatorBurn(
        address _operator,
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external onlyImplementation {
        _burn(_operator, _from, _ids, _amounts, _data, _operatorData);
    }

    /// EXTERNAL VIEW

    /// @notice Get the balance of an account's Tokens.
    /// @param _owner  The address of the token holder
    /// @param _id     ID of the Token
    /// @return The _owner's balance of the Token type requested
    function balanceOf(address _owner, uint256 _id) external view returns (uint256) {
        if (isNonFungibleItem(_id)) {
            return nfOwners[_id] == _owner ? 1 : 0;
        }
        return balances[_id][_owner];
    }

    /// @notice Get the balance of multiple account/token pairs.
    /// @param _owners The addresses of the token holders
    /// @param _ids    ID of the Tokens
    /// @return balances_   The _owner's balance of the Token types requested
    function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids)
        external
        view
        returns (uint256[] memory balances_)
    {
        require(_owners.length == _ids.length, "LENGTH_MISMATCH");

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

    /// @notice Get the granularity of fungible tokens.
    function granularity() external view returns (uint256) {
        return gran;
    }

    /// PUBLIC

    /// @notice Swaps tokens.
    /// @param _sender  Address of the sender (msg.sender)
    /// @param _signer  Address of the signer
    /// @param _swap    Swap data
    /// @param _data    Additional data with no specified format
    function swap(
        address _sender,
        address _signer,
        SwapLib.Swap memory _swap,
        bytes memory _data
    ) public onlyImplementation {
        _send(
            _sender,
            _sender,
            _signer,
            _swap.senderTokenIds,
            _swap.senderTokenAmounts,
            _data,
            ""
        );
        _send(
            _signer,
            _signer,
            _sender,
            _swap.signerTokenIds,
            _swap.signerTokenAmounts,
            _data,
            ""
        );
    }

    /// INTERNAL

    /// @notice Sends multiple types of tokens.
    /// @param _operator    msg.sender
    /// @param _from        Sender addresses
    /// @param _to          Recipient addresses
    /// @param _ids         Ids of each token type
    /// @param _amounts     Transfer amounts per token type
    /// @param _data        Additional data with no specified format
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
        require(_to != address(0x0), "INVALID_ADDRESS");
        require(_ids.length == _amounts.length, "LENGTH_MISMATCH");

        callSender(_operator, _from, _to, _ids, _amounts, _data, _operatorData);

        for (uint256 i = 0; i < _ids.length; ++i) {
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];

            if (isNonFungible(id)) {
                require(amount == 1, "INVALID_AMOUNT");
                require(nfOwners[id] == _from, "NOT_OWNER");
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
            emit TokenSent(_operator, _from, _to, id, amount, _data, _operatorData);
        }

        callReceiver(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Burns token.
    /// @param _operator    msg.sender
    /// @param _from        Source address
    /// @param _ids         IDs of the token type
    /// @param _amounts     Burn amounts
    /// @param _data        Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _burn(
        address _operator,
        address _from,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        require(_from != address(0), "INVALID_ADDRESS");

        callSender(_operator, _from, address(0), _ids, _amounts, _data, _operatorData);

        for (uint256 i = 0; i < _ids.length; ++i) {
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];
            if (isNonFungible(id)) {
                require(amount == 1, "INVALID_AMOUNT");
                require(nfOwners[id] == _from, "NOT_OWNER");
                nfOwners[id] == address(0);
                uint256 baseType = getNonFungibleBaseType(id);
                balances[baseType][_from] = balances[baseType][_from].sub(amount);
            } else {
                _checkGranularity(amount);
                balances[id][_from] = balances[id][_from].sub(amount);
            }
            emit TokenBurned(_operator, _from, id, amount, _data, _operatorData);
        }
    }

    /// @notice Calls/Verifies the sender.
    /// @param _operator    msg.sender
    /// @param _from        Sender address
    /// @param _to          Recepient address
    /// @param _ids         IDs of the token type
    /// @param _amounts     Burn amounts
    /// @param _data        Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function callSender(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) private {
        address impl = erc1820.getInterfaceImplementer(_from, TOKEN_SENDER_INTERFACE_HASH);
        if (impl != address(0)) {
            ITokenSender(impl).tokensToSend(
                _operator,
                _from,
                _to,
                _ids,
                _amounts,
                _data,
                _operatorData
            );
        }
    }

    /// @notice Calls/Verifies the recipient.
    /// @param _operator    msg.sender
    /// @param _from        Sender address
    /// @param _to          Recepient address
    /// @param _ids         IDs of the token type
    /// @param _amounts     Burn amounts
    /// @param _data        Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function callReceiver(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) private {
        address impl = erc1820.getInterfaceImplementer(_to, TOKEN_RECIPIENT_INTERFACE_HASH);
        if (impl != address(0)) {
            ITokenRecipient(impl).tokensReceived(
                _operator,
                _from,
                _to,
                _ids,
                _amounts,
                _data,
                _operatorData
            );
        } else {
            require(!_to.isContract(), "INTERFACE_NOT_IMPLEMENTED");
        }
    }

    /// INTERNAL VIEWS

    function _checkGranularity(uint256 _amount) internal view {
        require(_amount % gran == 0, "INVALID_GRANULARITY");
    }
}
