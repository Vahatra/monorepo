pragma solidity ^0.6.0;

import "./BaseErrors.sol";

/// @title Organization manager contract
/// @notice This contract holds implementation logic for all org management
/// functionality. This can be called only by the implementation
/// contract only.
/// @dev the status of the organization is denoted by a set of integer
/// values. These are as below:
///     0 - Not in list,
///     1 - Org Active
///     2 - Org Suspended
contract OrgManager is BaseErrors {
    bool private booted = false;
    address private implementation;

    // variables which control the breadth and depth of the sub org tree
    uint256 private BREADTH_LIMIT = 5;
    uint256 private DEPTH_LIMIT = 1;

    struct Org {
        address org;
        address pOrg; // parent org
        address uOrg; // ultimate parent org
        string name;
        string role;
        uint256 level;
        address[] subOrgs;
        uint256 status;
        uint256 txCount;
    }

    mapping(address => Org) private orgMap;

    /// EVENTS

    event GraphOrg(
        address _org,
        address _pOrg,
        address _uOrg,
        string _name,
        string _role,
        uint256 level,
        uint256 _status
    );
    event GraphSubOrg(address _org, address _subOrg);
    event GraphOrgTransact(address _org, uint256 _txCount);
    event GraphOrgStatus(address _org, uint256 _status);

    /// MODIFIERS

    /// @notice confirms that the caller is the address of implementation contract
    modifier onlyImplementation {
        require(msg.sender == implementation, INVALID_CALLER);
        _;
    }

    /// CONST

    /// @notice constructor sets the BREADTH_LIMIT and DEPTH_LIMIT.
    /// @param _breadth - max suborg count an org can have
    /// @param _depth - max depth of an org
    constructor(uint256 _breadth, uint256 _depth) public {
        BREADTH_LIMIT = _breadth;
        DEPTH_LIMIT = _depth;
    }

    /// INIT

    /// @notice sets the implementation contract address.
    function init(address _implementation) external {
        require(!booted, INVALID_BOOT_STATUS);
        implementation = _implementation;
        booted = true;
    }

    /// EXTERNAL

    /// @notice sets the transaction count of an org.
    /// @param _org - org address
    /// @param _txCount - transaction count
    /// @dev should only be called by the admin
    function setTxCount(address _org, uint256 _txCount)
        external
        onlyImplementation
    {
        require(orgExists(_org), ORG_NOT_EXIST);
        orgMap[_org].txCount = _txCount;
        emit GraphOrgTransact(_org, orgMap[_org].txCount);
    }

    /// @notice checks if an org can make a transaction,
    /// if yes, decrement its transaction count by one
    /// @param _org - org address
    /// @return true/false
    function transact(address _org) external returns (bool) {
        if (
            (orgMap[_org].org != address(0)) &&
            (orgMap[_org].txCount > 0) &&
            (orgMap[_org].status == 1)
        ) {
            orgMap[_org].txCount -= 1;
            emit GraphOrgTransact(_org, orgMap[_org].txCount);
            return true;
        }
        return false;
    }

    /// @notice add a new org to the network.
    /// @param _org - org address
    /// @param _pOrg -parent org
    /// @param _name - name of the org
    /// @param _role - role of the org
    /// @dev check if the _org does not already exist as an account before calling
    function addOrg(
        address _org,
        address _pOrg,
        string calldata _name,
        string calldata _role
    ) external onlyImplementation {
        require(!(orgExists(_org)), ORG_EXIST);

        if (_pOrg == address(0)) {
            //root
            orgMap[_org] = Org(
                _org,
                _pOrg,
                _org,
                _name,
                _role,
                1,
                new address[](0),
                1,
                10
            );
        } else {
            require(orgExists(_pOrg), ORG_NOT_EXIST);
            require(
                orgMap[_pOrg].subOrgs.length < BREADTH_LIMIT,
                BREADTH_EXCEEDED
            );
            require(orgMap[_pOrg].level < DEPTH_LIMIT, DEPTH_EXCEEDED);

            // example: (org) wylog, (suborg) wylog.legazpi
            string memory name = string(
                abi.encodePacked((orgMap[_pOrg].name), ".", _name)
            );

            orgMap[_pOrg].subOrgs.push(_org);

            orgMap[_org] = Org(
                _org,
                _pOrg,
                orgMap[_org].uOrg,
                name,
                _role,
                orgMap[_pOrg].level + 1,
                new address[](0),
                1,
                10
            );
        }

        emit GraphOrg(
            _org,
            _pOrg,
            orgMap[_org].uOrg,
            orgMap[_org].name,
            _role,
            orgMap[_org].level,
            1
        );

        if (_pOrg != address(0)) {
            emit GraphSubOrg(_pOrg, _org);
        }

        emit GraphOrgTransact(_org, orgMap[_org].txCount);
    }

    /// @notice updates the status of an org.
    /// @param _org - org address
    /// @param _action - action being performed
    /// This function can be called for the following actions:
    ///     1 - Suspend - called by admin
    ///     2 - Reactivate - called by admin
    /// @dev should only be called by the admin.
    function updateOrgStatus(address _org, uint256 _action)
        external
        onlyImplementation
    {
        require(orgExists(_org), ORG_NOT_EXIST);
        require((_action == 1 || _action == 2), INVALID_ACTION);
        if (_action == 1) {
            _suspendOrg(_org);
        } else if (_action == 2) {
            _revokeOrg(_org);
        }
    }

    /// EXTERNAL VIEW

    /// @notice confirms that the org status is same as passed status
    /// @param _org - org address
    /// @param _status - org status
    /// @return true/false
    /// @dev 1 - active. 2 - suspended.
    function orgStatus(address _org, uint256 _status)
        public
        view
        returns (bool)
    {
        if (orgMap[_org].org != address(0)) {
            return (orgMap[_org].status == _status);
        }
        return false;
    }

    /// @notice confirms if the given org exists in the network
    /// @param _org - org address
    /// @return true/false
    function orgExists(address _org) public view returns (bool) {
        return (orgMap[_org].org != address(0));
    }

    /// INTERNAL

    /// @notice suspend an org
    /// @param _org - org address
    function _suspendOrg(address _org) internal {
        require(orgStatus(_org, 1), ALREADY_HAS_STATUS);
        orgMap[_org].status = 2;
        emit GraphOrgStatus(_org, 2);
    }

    /// @notice revoke an org suspension
    /// @param _org - org address
    function _revokeOrg(address _org) internal {
        require(orgStatus(_org, 2), ALREADY_HAS_STATUS);
        orgMap[_org].status = 1;
        emit GraphOrgStatus(_org, 1);
    }
}
