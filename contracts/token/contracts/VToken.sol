// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "./interfaces/IERC1155.sol";
import "./interfaces/IERC1155Receiver.sol";
import "./MixinNonFungibleToken.sol";

contract VToken is IERC1155, MixinNonFungibleToken {
    using Address for address;
    using SafeMath for uint256;

    bytes4 public constant ERC1155_RECEIVED = 0xf23a6e61;
    bytes4 public constant ERC1155_BATCH_RECEIVED = 0xbc197c81;

    /// token nonce
    uint256 internal nonce;

    /// mapping from token to creator
    mapping(uint256 => address) public creators;

    /// mapping from token to max index
    mapping(uint256 => uint256) public maxIndex;

    /// granularity for fungible tokens.
    uint256 internal granularity;

    /// balance
    mapping(uint256 => mapping(address => uint256)) internal balances;

    /// operators
    address[] internal defaultOperators;
    mapping(address => bool) internal isDefaultOperators;
    mapping(address => mapping(address => bool)) internal operators;
    mapping(address => mapping(address => bool)) internal revokedDefaultOperators;

    /// asserts token is owned by msg.sender
    modifier creatorOnly(uint256 _id) {
        require(creators[_id] == msg.sender, "NOT_CREATOR");
        _;
    }

    /// EVENT

    event Sent(
        address indexed operator,
        address indexed from,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );
    event Minted(
        address indexed operator,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );
    event Burned(
        address indexed operator,
        address indexed from,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );
    event AuthorizedOperator(address indexed operator, address indexed holder);
    event RevokedOperator(address indexed operator, address indexed holder);

    /// OTHER

    function _checkGranularity(uint256 _amount) internal view {
        require(_amount % granularity == 0, "NOT_MULTIPLE_OF_GRANULARITY");
    }

    function granularity() external view returns (uint256) {
        return granularity;
    }

    function defaultOperators() external view returns (address[] memory) {
        return defaultOperators;
    }

    /// CREATE

    /// @dev creates a new token
    /// @param _uri URI of token
    /// @param _isNF is non-fungible token
    /// @return type_ of token (a unique identifier)
    function create(string calldata _uri, bool _isNF) external returns (uint256 type_) {
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

    /// @dev creates a new token
    /// @param _type of token
    /// @param _uri URI of token
    function createWithType(uint256 _type, string calldata _uri) external {
        // This will allow restricted access to creators.
        creators[_type] = msg.sender;

        // emit a Sent event with Create semantic to help with discovery.
        emit Sent(msg.sender, address(0), address(0), _type, 0, "", "");
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
    ) external creatorOnly(id) {
        // sanity checks
        require(_to != address(0x0), "CANNOT_MINT_FOR_ADDRESS_ZERO");
        require(isFungible(id), "TRIED_TO_MINT_FUNGIBLE_FOR_NON_FUNGIBLE_TOKEN");
        // HERE need to check contract caller

        // mint tokens
        for (uint256 i = 0; i < _to.length; ++i) {
            // cache to reduce number of loads
            address to = _to[i];
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
    ) external creatorOnly(_type) {
        // No need to check this is a nf type rather than an id since
        // creatorOnly() will only let a type pass through.
        require(_to != address(0x0), "CANNOT_MINT_FOR_ADDRESS_ZERO");
        require(isNonFungible(_type), "TRIED_TO_MINT_NON_FUNGIBLE_FOR_FUNGIBLE_TOKEN");

        // Index are 1-based.
        uint256 index = maxIndex[_type] + 1;

        for (uint256 i = 0; i < to.length; ++i) {
            // cache to reduce number of loads
            address to = to[i];
            uint256 id = _type | (index + i);

            nfOwners[id] = to;

            // NFT base type balance
            balances[_type][to] = quantity.add(balances[_type][to]);

            emit Minted(msg.sender, to, _id, 1, _data, _operatorData);
        }

        // record the `maxIndex` of this nft type
        // this allows us to mint more nft's of this type in a subsequent call.
        maxIndex[_type] = _to.length.add(maxIndex[_type]);
    }

    /// SEND

    /// @notice Sends amount of an _id from msg.sender to the _to address specified.
    /// @param _to      Target address
    /// @param _id      ID of the token type
    /// @param _amount   Transfer amount
    /// @param _data    Additional data with no specified format
    function send(
        address _to,
        uint256 _id,
        uint256 _amount,
        bytes calldata _data
    ) external {
        _send(msg.sender, msg.sender, _to, _id, _amount, _data, "");
    }

    /// @notice Sends _amount of an _id from the _from address to the _to address specified.
    /// @param _from    Source address
    /// @param _to      Target address
    /// @param _id      ID of the token type
    /// @param _amount   Transfer amount
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function operatorSend(
        address _from,
        address _to,
        uint256 _id,
        uint256 _amount,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        require(_isOperatorFor(msg.sender, from), "INSUFFICIENT_ALLOWANCE");
        _send(msg.sender, _from, _to, _id, _amount, _data, _operatorData);
    }

    /// @notice Actually make the transfer.
    /// @param _operator msg.sender
    /// @param _from    Source address
    /// @param _to      Target address
    /// @param _id      ID of the token type
    /// @param _amount   Transfer amount
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _send(
        address _operator,
        address _from,
        address _to,
        uint256 _id,
        uint256 _amount,
        bytes calldata _data,
        bytes calldata _operatorData
    ) internal {
        require(to != address(0x0), "CANNOT_TRANSFER_TO_ADDRESS_ZERO");

        // perform transfer
        if (isNonFungible(_id)) {
            require(_amount == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
            require(nfOwners[_id] == _from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
            nfOwners[_id] = _to;
            // Keep the balance of NF type in base type id
            uint256 baseType = getNonFungibleBaseType(_id);
            balances[baseType][_from] = balances[baseType][_from].sub(_amount);
            balances[baseType][_to] = balances[baseType][_to].add(_amount);
        } else {
            _checkGranularity(_amount);
            balances[_id][_from] = balances[_id][_from].sub(_amount);
            balances[_id][_to] = balances[_id][_to].add(_amount);
        }
        emit Sent(_operator, _from, _to, _id, _amount, _data, _operatorData);
    }

    /// BATCH

    /// @notice Send multiple types of Tokens in one transfer from msg.sender.
    /// @param _to      Target addresses
    /// @param _ids     IDs of each token type
    /// @param _amounts  Transfer amounts per token type
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function batchSend(
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        _batchSend(msg.sender, msg.sender, _to, _ids, _amounts, _data, "");
    }

    /// @notice Send multiple types of Tokens in one transfer from the _from address.
    /// @param _from    Source addresses
    /// @param _to      Target addresses
    /// @param _ids     IDs of each token type
    /// @param _amounts  Transfer amounts per token type
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function operatorBatchSend(
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        _batchSend(msg.sender, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Actually make the transfers.
    /// @param _operator msg.sender
    /// @param _from    Source addresses
    /// @param _to      Target addresses
    /// @param _ids     IDs of each token type
    /// @param _amounts  Transfer amounts per token type
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _batchSend(
        address _operator,
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) internal {
        // sanity checks
        require(_to != address(0x0), "CANNOT_TRANSFER_TO_ADDRESS_ZERO");
        require(_ids.length == _amounts.length, "IDS_AND_VALUES_LENGTH_MISMATCH");

        // perform transfers
        for (uint256 i = 0; i < _ids.length; ++i) {
            // Cache amount to local variable to reduce read costs.
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];

            if (isNonFungible(id)) {
                require(amount == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
                require(nfOwners[id] == _from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
                nfOwners[id] = to;
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
    }

    function updateBalance(
        address _from,
        address _to,
        uint256 _id,
        uint256 _amount
    ) internal {
        if (isNonFungible(_id)) {
            require(amount == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
            require(nfOwners[_id] == _from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
            nfOwners[_id] = _to;
            // Keep the balance of NF type in base type id
            uint256 baseType = getNonFungibleBaseType(_id);
            balances[baseType][_from] = balances[baseType][_from].sub(amount);
            if (_to != address(0)) {
                balances[baseType][_to] = balances[baseType][_to].add(amount);
            }
        } else {
            _checkGranularity(amount);
            balances[_id][_from] = balances[_id][_from].sub(amount);
            balances[_id][_to] = balances[_id][_to].add(amount);
        }
    }

    /// BURN

    /// @notice Burn _value amount of an _id from msg.sender.
    /// @param _id      ID of the token type
    /// @param _amount   Burn amount
    /// @param _data    Additional data with no specified format
    function burn(
        uint256 _id,
        uint256 _amount,
        bytes calldata _data
    ) external {
        _burn(msg.sender, msg.sender, _id, _amount, _data, "");
    }

    /// @notice Burn _value amount of an _id from _from.
    /// @param _from    Source address
    /// @param _id      ID of the token type
    /// @param _amount   Burn amount
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function operatorBurn(
        address _from,
        uint256 _id,
        uint256 _amount,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        _burn(msg.sender, _from, _id, _amount, _data, _operatorData);
    }

    /// @notice Actually make the burnning.
    /// @param _operator msg.sender
    /// @param _from    Source address
    /// @param _id      ID of the token type
    /// @param _amount   Burn amount
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _burn(
        address _operator,
        address _from,
        uint256 _id,
        uint256 _amount,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        require(_from != address(0), "CANNOT_BURN_FROM_ADDRESS_ZERO");
        _balances[_from] = _balances[_from].sub(_amount);

        if (isNonFungible(_id)) {
            require(_amount == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
            require(nfOwners[id] == _from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
            nfOwners[_id] == address(0);
            uint256 baseType = getNonFungibleBaseType(_id);
            balances[baseType][_from] = balances[baseType][_from].sub(_amount);
        } else {
            _checkGranularity(_amount);
            balances[_id][_from] = balances[_id][_from].sub(_amount);
        }
        emit Burned(_operator, _from, _id, _amount, _data, _operatorData);
    }

    /// @notice Burn _value amount of an _id from msg.sender.
    /// @param _ids      IDs of the token type
    /// @param _amounts  Burn amounts
    /// @param _data     Additional data with no specified format
    function burnBatch(
        uint256 _ids,
        uint256 _amounts,
        bytes calldata _data
    ) external {
        _burnBatch(msg.sender, msg.sender, _ids, _amounts, _data, "");
    }

    /// @notice Burn _value amount of an _id from _from.
    /// @param _from    Source address
    /// @param _ids      ID of the token type
    /// @param _amounts   Burn amount
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function operatorBurnBatch(
        address _from,
        uint256 _ids,
        uint256 _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        _burnBatch(msg.sender, _from, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Actually make the burnning.
    /// @param _operator msg.sender
    /// @param _from    Source address
    /// @param _ids     ID of the token type
    /// @param _amounts Burn amounts
    /// @param _data    Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    function _burnBatch(
        address _operator,
        address _from,
        uint256 _ids,
        uint256 _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        require(_from != address(0), "CANNOT_BURN_FROM_ADDRESS_ZERO");
        _balances[_from] = _balances[_from].sub(_amount);

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

    /// OPERATOR

    /// @notice Returns the list of default operators as defined by the token contract.
    function defaultOperators() external view returns (address[] memory) {
        return defaultOperators;
    }

    /// @notice Set a third party operator address as an operator of msg.sender to send
    /// and burn tokens on its behalf.
    /// @param _operator  Address to add to the set of authorized operators
    function authorizeOperator(address _operator) external {
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
    function revokeOperator(address _operator) external {
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
            (isDefaultOperators[operator] && !revokedDefaultOperators[_holder][_operator]) ||
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
    /// @return        The _owner's balance of the Token types requested
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
