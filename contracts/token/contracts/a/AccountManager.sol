pragma solidity ^0.6.0;

/// @title Account manager contract
/// @notice This contract holds implementation logic for all account management
/// functionality. This can be called only by the implementation contract.
/// @dev account status is denoted by a fixed integer value. The values are
/// as below:
///     0 - Not in list
///     1 - Active
///     2 - Suspended
///     3 - Blacklisted
contract AccountManager {
    bool private booted = false;
    address private implementation;

    struct Account {
        address account;
        address org;
        string role;
        uint256 status;
    }

    mapping(address => Account) private accountMap;

    /// EVENTS

    event AccountCreated(
        address _account,
        address _org,
        string _role,
        uint256 _status
    );
    event AccountRoleChanged(address _account, string _role);
    event AccountStatusChanged(address _account, uint256 _status);

    /// MODIFIERS

    /// @notice confirms that the caller is the address of implementation contract
    modifier onlyImplementation {
        require(msg.sender == implementation, "invalid caller");
        _;
    }

    /// INIT

    /// @notice sets the implementation contract address.
    function init(address _implementation) external {
        require(!booted, "init already called");
        implementation = _implementation;
        booted = true;
    }

    /// EXTERNAL

    /// @notice assigns any role to the passed account.
    /// if the account doesn't exist, add it.
    /// @param _account - account address
    /// @param _org - org to which it belongs
    /// @param _role - role to be assigned
    /// @dev should only be called by an org
    /// check if the org is active before calling this function.
    /// check if the role exist before calling this function.
    function assignRole(
        address _account,
        address _org,
        string calldata _role
    ) external onlyImplementation {
        // needs to be a new account OR (belongs to the given org AND be active)
        require(
            (accountMap[_account].account == address(0)) ||
                ((accountMap[_account].org == _org) &&
                    (accountMap[_account].status == 1)),
            "invalid acount"
        );
        if (accountMap[_account].account != address(0)) {
            accountMap[_account].role = _role;
            emit AccountRoleChanged(_account, _role);
        } else {
            accountMap[_account] = Account(_account, _org, _role, 1);
            emit AccountCreated(_account, _org, _role, 1);
        }
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
        require((_action > 0 && _action < 5), "invalid status change request");
        require(
            (accountMap[_account].org == _org),
            "account belongs to another org"
        );

        uint256 status = accountMap[_account].status;
        uint256 newStatus;
        if (_action == 1) {
            // for suspending an account current status should be active
            require(status == 1, "account is not in active status");
            newStatus = 2;
        } else if (_action == 2) {
            // for reactivating a suspended account, current status should be suspended
            require(status == 2, "account is not in suspended status");
            newStatus = 1;
        } else if (_action == 3) {
            require((status != 3), "account is already blacklisted");
            newStatus = 3;
        } else if (_action == 4) {
            require(status == 3, "account is not blacklisted");
            newStatus = 1;
        }

        accountMap[_account].status = newStatus;
        emit AccountStatusChanged(_account, newStatus);
    }

    /// EXTERNAL VIEW

    /// @notice get account org
    /// @param _account - account address
    /// @return org address
    function getAccountOrg(address _account) external view returns (address) {
        return (accountMap[_account].org);
    }

    /// @notice checks if the passed account exists.
    /// @param _account - account id
    /// @return bool true if the account exists
    function accountExists(address _account) external view returns (bool) {
        return (accountMap[_account].account != address(0));
    }

    /// @notice confirms that account status is same as passed status.
    /// @param _account - account
    /// @return true/false
    function accountStatus(address _account, uint256 _status)
        public
        view
        returns (bool)
    {
        if (accountMap[_account].account != address(0)) {
            return (accountMap[_account].status == _status);
        }
        return false;
    }
}
