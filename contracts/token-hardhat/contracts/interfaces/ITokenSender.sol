// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

/// @dev a.
interface ITokenSender {
    /// @dev a
    function tokensToSend(
        address operator,
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata amounts,
        bytes calldata userData,
        bytes calldata operatorData
    ) external;
}
