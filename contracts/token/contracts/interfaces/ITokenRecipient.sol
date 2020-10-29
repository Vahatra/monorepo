// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

/// @dev a.
interface ITokenRecipient {
    /// @dev a
    function tokensReceived(
        address operator,
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata amounts,
        bytes calldata data,
        bytes calldata operatorData
    ) external;
}
