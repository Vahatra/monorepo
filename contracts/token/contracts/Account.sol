// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "./Initializable.sol";

/// @title Account manager contract
/// @notice This contract holds implementation logic for all account management
/// functionality. This can be called only by the implementation contract.
/// @dev account status is denoted by a fixed integer value. The values are
/// as below:
///     0 - Not in list
///     1 - Active
///     2 - Suspended
///     3 - Blacklisted
contract Account is Initializable {
    struct Acc {
        address account;
        address org;
        uint256 status;
    }

    mapping(address => Acc) private accountMap;

    /// EVENTS

    event AccountCreated(address _account, address _org, uint256 _status);
    event AccountStatusUpdated(address _account, uint256 _status);

    /// EXTERNAL

    /// @notice Add an account to an org.
    /// @param _account Account address
    /// @param _org     Org to which it belongs
    /// @dev should only be called by an org
    /// check if the org is active before calling this function.
    function addAccount(address _account, address _org) external onlyImplementation {
        require(accountMap[_account].account == address(0), "ALREADY_EXIST");
        accountMap[_account] = Acc(_account, _org, 1);
        emit AccountCreated(_account, _org, 1);
    }

    /// @notice updates the account status to the passed status value
    /// @param _account - account
    /// @param _org - org
    /// @param _action - new status of the account
    /// @dev the following actions are allowed
    ///     1 - Suspend - called by org
    ///     2 - Reactivate - called by org
    ///     3 - Blacklist - called by admin
    ///     4 - Recover - called by admin
    function updateAccountStatus(
        address _account,
        address _org,
        uint256 _action
    ) external onlyImplementation {
        require((_action > 0 && _action < 5), "INVALID_ACTION");
        require((accountMap[_account].org == _org), "INVALID_ORG");

        uint256 status = accountMap[_account].status;
        uint256 newStatus;
        if (_action == 1) {
            // for suspending an account current status should be active
            require(status == 1, "ACCOUNT_NOT_ACTIVE");
            newStatus = 2;
        } else if (_action == 2) {
            // for reactivating a suspended account, current status should be suspended
            require(status == 2, "ACCOUNT_NOT_SUSPENDED");
            newStatus = 1;
        } else if (_action == 3) {
            require((status != 3), "ACCOUNT_ALREADY_BLACKLISTED");
            newStatus = 3;
        } else if (_action == 4) {
            require(status == 3, "ACCOUNT_NOT_BLACKLISTED");
            newStatus = 1;
        }

        accountMap[_account].status = newStatus;
        emit AccountStatusUpdated(_account, newStatus);
    }

    /// EXTERNAL VIEW

    /// @notice Get an account's org
    /// @param _account Account address
    /// @return Org address
    function getAccountOrg(address _account) external view returns (address) {
        return (accountMap[_account].org);
    }

    /// @notice Checks if the passed account exists.
    /// @param _account Account id
    /// @return tue/false
    function accountExist(address _account) external view returns (bool) {
        return (accountMap[_account].account != address(0));
    }

    /// @notice Confirms that account status is same as passed status.
    /// @param _account Account
    /// @return true/false
    function accountStatus(address _account, uint256 _status) public view returns (bool) {
        return (accountMap[_account].status == _status);
    }
}
