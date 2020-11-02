// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

/// @title Initializable contract
/// @notice This contract is for setting implementation
contract Initializable {
    bool internal booted = false;
    address internal implementation;

    /// @notice confirms that the caller is the address of implementation contract
    modifier onlyImplementation {
        require(msg.sender == implementation, "NOT_IMPLEMENTATION_CONTRACT");
        _;
    }

    /// @notice Sets the implementation contract address.
    function initialize(address _implementation) external {
        require(!booted, "INVALID_BOOT_STATUS");
        implementation = _implementation;
        booted = true;
    }
}
