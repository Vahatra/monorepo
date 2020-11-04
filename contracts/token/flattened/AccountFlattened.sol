// File: contracts\Initializable.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;

/// @title Initializable contract
contract Initializable {
    bool internal booted = false;
    address internal implementation;

    /// @notice Confirms that the caller is the address of implementation contract
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

// File: contracts\Account.sol

/// @title Account manager contract.
/// @notice This contract holds the implementation logic for all account management
/// functionality. This can be called only by the implementation contract.
/// @dev account status is denoted by a fixed integer value. The values are:
///     0 - Not in list
///     1 - Active
///     2 - Suspended
///     3 - Blacklisted
contract Account is Initializable {
    /// @dev Control the breadth and depth of the sub account tree.
    uint256 private BREADTH_LIMIT;
    uint256 private DEPTH_LIMIT;

    /// @dev Mapping of operators.
    mapping(address => mapping(address => bool)) internal operators;

    struct Acc {
        address acc;
        address pAcc; // parent account
        address uAcc; // ultimate parent account
        string name;
        uint256 level;
        address[] subAccs;
        uint256 status;
    }

    mapping(address => Acc) private accMap;

    /// @dev `addAccount` MUST emit when an account is created.
    event AccountCreated(
        address _acc,
        address _pAcc,
        address _uAcc,
        string _name,
        uint256 level,
        uint256 _status
    );

    /// @dev `updateAccountStatus` MUST emit when an account status changes.
    event AccountStatusUpdated(address _acc, uint256 _status);

    /// @dev `authorizeOperator` MUST emit when an operator is authorized.
    /// Holder will always be msg.sender.
    event AuthorizedOperator(address indexed operator, address indexed holder);

    /// @dev `revokeOperator` MUST emit when an operator is revoked.
    /// Holder will always be msg.sender.
    event RevokedOperator(address indexed operator, address indexed holder);

    /// @notice Constructor sets the BREADTH_LIMIT and DEPTH_LIMIT.
    /// @param _breadth Max sub account count an account can have.
    /// @param _depth   Max depth of the account tree.
    constructor(uint256 _breadth, uint256 _depth) public {
        BREADTH_LIMIT = _breadth;
        DEPTH_LIMIT = _depth;
    }

    /// @notice Add a new account.
    /// @param _acc     Account address.
    /// @param _pAcc    Parent account.
    /// @param _name    Name of the account.
    /// @dev If _pAcc != 0, check that msg.sender == _pAcc.
    function addAccount(
        address _acc,
        address _pAcc,
        string calldata _name
    ) external onlyImplementation {
        require(accMap[_acc].acc == address(0), "ACCOUNT_ALREADY_EXIST");

        if (_pAcc == address(0)) {
            //root
            accMap[_acc] = Acc(_acc, _pAcc, _acc, _name, 1, new address[](0), 1);
        } else {
            require(isActive(_pAcc), "INVALID_PARENT_ACCOUNT");
            require(accMap[_pAcc].subAccs.length < BREADTH_LIMIT, "BREADTH_EXCEEDED");
            require(accMap[_pAcc].level < DEPTH_LIMIT, "DEPTH_EXCEEDED");

            // example: (acc) google, (subacc) google.paris
            string memory name = string(abi.encodePacked((accMap[_pAcc].name), ".", _name));
            accMap[_pAcc].subAccs.push(_acc);
            accMap[_acc] = Acc(
                _acc,
                _pAcc,
                accMap[_acc].uAcc,
                name,
                accMap[_pAcc].level + 1,
                new address[](0),
                1
            );
        }
        emit AccountCreated(
            _acc,
            _pAcc,
            accMap[_acc].uAcc,
            accMap[_acc].name,
            accMap[_acc].level,
            1
        );
    }

    /// @notice Updates the account status to the passed status value
    /// @param _acc     Account address.
    /// @param _action  New status of the account.
    /// @dev the following actions are allowed:
    ///     1 - Suspend - called by pAcc
    ///     2 - Reactivate - called by pAcc
    ///     3 - Blacklist - called by owner
    ///     4 - Recover - called by owner
    function updateAccountStatus(address _acc, uint256 _action) external onlyImplementation {
        require((_action > 0 && _action < 5), "INVALID_ACTION");

        uint256 status = accMap[_acc].status;
        uint256 newStatus;
        if (_action == 1) {
            // For suspending an account current status should be active.
            require(status == 1, "NOT_LISTED_OR_INACTIVE_ACCOUNT");
            newStatus = 2;
        } else if (_action == 2) {
            // For reactivating a suspended account, current status should be suspended.
            require(status == 2, "ACCOUNT_NOT_SUSPENDED");
            newStatus = 1;
        } else if (_action == 3) {
            require((status != 3), "ACCOUNT_ALREADY_BLACKLISTED");
            newStatus = 3;
        } else if (_action == 4) {
            require(status == 3, "ACCOUNT_NOT_BLACKLISTED");
            newStatus = 1;
        }
        accMap[_acc].status = newStatus;
        emit AccountStatusUpdated(_acc, newStatus);
    }

    /// @notice Set a third party operator address as an operator of _sender (msg.sender) to send
    /// and burn tokens on its behalf.
    /// @param _sender      Address of the sender (msg.sender).
    /// @param _operator    Address to add to the set of authorized operators.
    function authorizeOperator(address _sender, address _operator) external onlyImplementation {
        require(isActive(_sender), "NOT_LISTED_OR_INACTIVE_ACCOUNT");
        require(_sender != _operator, "INVALID_OPERATOR");

        operators[_sender][_operator] = true;
        emit AuthorizedOperator(_operator, _sender);
    }

    /// @notice Remove the right of the operator address to be an operator for
    /// _sender (msg.sender) and to send and burn tokens on its behalf.
    /// @param _sender      Address of the sender (msg.sender).
    /// @param _operator    Address to add to the set of authorized operators.
    function revokeOperator(address _sender, address _operator) external onlyImplementation {
        require(isActive(_sender), "NOT_LISTED_OR_INACTIVE_ACCOUNT");
        require(_sender != _operator, "INVALID_OPERATOR");

        operators[_sender][_operator] = false;
        emit RevokedOperator(_operator, _sender);
    }

    /// @notice Get an account info.
    /// @param _acc Account address.
    /// @return Parent address.
    function getAccount(address _acc) external view returns (Acc memory) {
        return accMap[_acc];
    }

    /// @notice Get the parent account of _acc.
    /// @param _acc Account address.
    /// @return Parent address.
    function getParentAccount(address _acc) external view returns (address) {
        return accMap[_acc].pAcc;
    }

    /// @notice Queries whether the operator address is an operator of the _acc address.
    /// @param _operator    Address of authorized operator.
    /// @param _acc         Account address.
    /// @return true/false.
    function isOperatorFor(address _operator, address _acc) external view returns (bool) {
        return operators[_acc][_operator];
    }

    /// @notice Confirms that the _acc account status is active.
    /// @param _acc Account address
    /// @return true/false
    /// @dev 0 - Not listed. 1 - active. 2 - suspended.
    function isActive(address _acc) public view returns (bool) {
        return (accMap[_acc].status == 1);
    }

    /// @notice Confirms if the given acc exist (active/suspended).
    /// @param _acc Account address.
    /// @return true/false.
    function _accountExist(address _acc) internal view returns (bool) {
        return (accMap[_acc].acc != address(0));
    }
}
