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

    mapping(uint256 => mapping(address => uint256)) internal balances;

    address[] internal defaultOperators;
    mapping(address => bool) internal isDefaultOperators;
    mapping(address => mapping(address => bool)) internal operators;
    mapping(address => mapping(address => bool))
        internal revokedDefaultOperators;

    /// SEND

    /// @notice Sends value amount of an _id from msg.sender to the _to address specified.
    /// @param to      Target address
    /// @param id      ID of the token type
    /// @param value   Transfer amount
    /// @param data    Additional data with no specified format
    function send(
        address to,
        uint256 id,
        uint256 value,
        bytes calldata data
    ) external {
        _send(msg.sender, msg.sender, to, id, amount, data, "");
    }

    /// @notice Sends value amount of an _id from the _from address to the _to address specified.
    /// @param from    Source address
    /// @param to      Target address
    /// @param id      ID of the token type
    /// @param value   Transfer amount
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function operatorSend(
        address from,
        address to,
        uint256 id,
        uint256 value,
        bytes calldata data,
        bytes calldata operatorData
    ) external {
        require(_isOperatorFor(msg.sender, from), "INSUFFICIENT_ALLOWANCE");
        _send(msg.sender, from, to, id, amount, data, operatorData);
    }

    /// @notice Actually make the transfer.
    /// @param operator msg.sender
    /// @param from    Source address
    /// @param to      Target address
    /// @param id      ID of the token type
    /// @param value   Transfer amount
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function _send(
        address operator,
        address from,
        address to,
        uint256 id,
        uint256 value,
        bytes calldata data,
        bytes calldata operatorData
    ) internal {
        require(to != address(0x0), "CANNOT_TRANSFER_TO_ADDRESS_ZERO");

        // perform transfer
        if (isNonFungible(id)) {
            require(value == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
            require(nfOwners[id] == from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
            nfOwners[id] = to;
            // Keep the balance of NF type in base type id
            uint256 baseType = getNonFungibleBaseType(_id);
            balances[baseType][from] = balances[baseType][_from].sub(value);
            balances[baseType][to] = balances[baseType][_to].add(value);
        } else {
            balances[id][from] = balances[id][from].sub(value);
            balances[id][to] = balances[id][to].add(value);
        }
        emit TransferSingle(msg.sender, from, to, id, value);
    }

    /// BATCH

    /// @notice Send multiple types of Tokens in one transfer from msg.sender.
    /// @param to      Target addresses
    /// @param ids     IDs of each token type
    /// @param values  Transfer amounts per token type
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function batchSend(
        address to,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data,
        bytes calldata operatorData
    ) external {
        _batchSend(msg.sender, msg.sender, to, ids, values, data, "");
    }

    /// @notice Send multiple types of Tokens in one transfer from the _from address.
    /// @param from    Source addresses
    /// @param to      Target addresses
    /// @param ids     IDs of each token type
    /// @param values  Transfer amounts per token type
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function operatorBatchSend(
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data,
        bytes calldata operatorData
    ) external {
        require(_isOperatorFor(msg.sender, from), "INSUFFICIENT_ALLOWANCE");
        _batchSend(msg.sender, from, to, ids, values, data, operatorData);
    }

    /// @notice Actually make the transfers.
    /// @param operator msg.sender
    /// @param from    Source addresses
    /// @param to      Target addresses
    /// @param ids     IDs of each token type
    /// @param values  Transfer amounts per token type
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function _batchSend(
        address operator,
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data,
        bytes calldata operatorData
    ) internal {
        // sanity checks
        require(to != address(0x0), "CANNOT_TRANSFER_TO_ADDRESS_ZERO");
        require(ids.length == values.length, "IDS_AND_VALUES_LENGTH_MISMATCH");

        // perform transfers
        for (uint256 i = 0; i < ids.length; ++i) {
            // Cache value to local variable to reduce read costs.
            uint256 id = ids[i];
            uint256 value = values[i];

            if (isNonFungible(id)) {
                require(value == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
                require(nfOwners[id] == from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
                nfOwners[id] = to;
                // Keep the balance of NF type in base type id
                uint256 baseType = getNonFungibleBaseType(id);
                balances[baseType][from] = balances[baseType][from].sub(value);
                balances[baseType][to] = balances[baseType][to].add(value);
            } else {
                balances[id][from] = balances[id][from].sub(value);
                balances[id][to] = balances[id][to].add(value);
            }
        }
        emit TransferBatch(msg.sender, from, to, ids, values);
    }

    /// BURN

    /// @notice Burn value amount of an _id from msg.sender.
    /// @param id      ID of the token type
    /// @param value   Burn amount
    /// @param data    Additional data with no specified format
    function burn(
        uint256 id,
        uint256 value,
        bytes calldata data
    ) external {
        _burn(msg.sender, msg.sender, id, amount, data, "");
    }

    /// @notice Burn value amount of an _id from _from.
    /// @param from    Source address
    /// @param id      ID of the token type
    /// @param value   Burn amount
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function operatorBurn(
        address from,
        uint256 id,
        uint256 value,
        bytes calldata data,
        bytes calldata operatorData
    ) external {
        require(_isOperatorFor(msg.sender, from), "INSUFFICIENT_ALLOWANCE");
        _burn(msg.sender, from, id, amount, data, operatorData);
    }

    /// @notice Actually make the burnning.
    /// @param operator msg.sender
    /// @param from    Source address
    /// @param id      ID of the token type
    /// @param value   Burn amount
    /// @param data    Additional data with no specified format
    /// @param operatorData Additional data with no specified format
    function _burn(
        address operator,
        address from,
        uint256 id,
        uint256 value,
        bytes memory data,
        bytes memory operatorData
    ) internal {
        require(from != address(0), "CANNOT_BURN_FROM_ADDRESS_ZERO");
        _balances[from] = _balances[from].sub(amount);

        if (isNonFungible(id)) {
            require(value == 1, "AMOUNT_EQUAL_TO_ONE_REQUIRED");
            require(nfOwners[id] == from, "NFT_NOT_OWNED_BY_FROM_ADDRESS");
            nfOwners[id] == address(0);
            uint256 baseType = getNonFungibleBaseType(id);
            balances[baseType][from] = balances[baseType][from].sub(value);
        } else {
            balances[id][from] = balances[id][from].sub(value);
        }

        emit Burned(operator, from, amount, data, operatorData);
    }

    /// OPERATOR

    /// @notice Returns the list of default operators as defined by the token contract.
    function defaultOperators() external view returns (address[] memory) {
        return defaultOperators;
    }

    /// @notice Set a third party operator address as an operator of msg.sender to send
    /// and burn tokens on its behalf.
    /// @param operator  Address to add to the set of authorized operators
    function authorizeOperator(address operator) external {
        require(msg.sender != operator, "SENDER_ALREADY_HIS_OPERATOR");

        if (isDefaultOperators[operator]) {
            revokedDefaultOperators[msg.sender][operator] = false;
        } else {
            operators[msg.sender][operator] = true;
        }
        emit ApprovalForAll(msg.sender, operator, approved);
    }

    /// @notice Remove the right of the operator address to be an operator for msg.sender
    /// and to send and burn tokens on its behalf.
    /// @param operator  Address to add to the set of authorized operators
    function revokeOperator(address operator) external {
        require(msg.sender != operator, "SENDER_ALREADY_HIS_OPERATOR");
        if (isDefaultOperators[operator]) {
            revokedDefaultOperators[msg.sender][operator] = true;
        } else {
            operators[msg.sender][operator] = false;
        }
        emit ApprovalForAll(msg.sender, operator, approved);
    }

    /// @notice Queries whether the operator address is an operator of the holder address.
    /// @param operator  Address of authorized operator
    /// @param holder    The owner of the Tokens
    /// @return          True if the operator is approved, false if not
    function isOperatorFor(address operator, address holder)
        external
        view
        returns (bool)
    {
        return _isOperatorFor(operator, holder);
    }

    function _isOperatorFor(address operator, address holder)
        internal
        view
        returns (bool)
    {
        return
            holder == operator ||
            (isDefaultOperators[operator] &&
                !revokedDefaultOperators[holder][operator]) ||
            operators[holder][operator];
    }

    /// BALANCE

    /// @notice Get the balance of an account's Tokens.
    /// @param owner  The address of the token holder
    /// @param id     ID of the Token
    /// @return        The _owner's balance of the Token type requested
    function balanceOf(address owner, uint256 id)
        external
        view
        returns (uint256)
    {
        if (isNonFungibleItem(id)) {
            return nfOwners[id] == owner ? 1 : 0;
        }
        return balances[id][owner];
    }

    /// @notice Get the balance of multiple account/token pairs
    /// @param owners The addresses of the token holders
    /// @param ids    ID of the Tokens
    /// @return        The _owner's balance of the Token types requested
    function balanceOfBatch(address[] calldata owners, uint256[] calldata ids)
        external
        view
        returns (uint256[] memory balances_)
    {
        // sanity check
        require(owners.length == ids.length, "OWNERS_AND_IDS_LENGTH_MISMATCH");

        // get balances
        balances_ = new uint256[](owners.length);
        for (uint256 i = 0; i < owners.length; ++i) {
            uint256 id = ids[i];
            if (isNonFungibleItem(id)) {
                balances_[i] = nfOwners[id] == owners[i] ? 1 : 0;
            } else {
                balances_[i] = balances[id][owners[i]];
            }
        }

        return balances_;
    }
}
