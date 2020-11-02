// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "./Initializable.sol";

/// @title Organization contract
/// @notice This contract holds implementation logic for all org management
/// functionality. This can be called only by the implementation
/// contract only.
/// @dev the status of the organization is denoted by a set of integer
/// values. These are as below:
///     0 - Not in list,
///     1 - Org Active
///     2 - Org Suspended
contract Organization is Initializable {
    /// @dev variables which control the breadth and depth of the sub org tree
    uint256 private BREADTH_LIMIT = 5;
    uint256 private DEPTH_LIMIT = 1;

    struct Org {
        address org;
        address pOrg; // parent org
        address uOrg; // ultimate parent org
        string name;
        uint256 level;
        address[] subOrgs;
        uint256 status;
    }

    mapping(address => Org) private orgMap;

    /// EVENTS

    event OrgCreated(
        address _org,
        address _pOrg,
        address _uOrg,
        string _name,
        uint256 level,
        uint256 _status
    );
    event OrgStatusUpdated(address _org, uint256 _status);

    /// CONST

    /// @notice Constructor sets the BREADTH_LIMIT and DEPTH_LIMIT.
    /// @param _breadth Max suborg count an org can have
    /// @param _depth   Max depth of an org
    constructor(uint256 _breadth, uint256 _depth) public {
        BREADTH_LIMIT = _breadth;
        DEPTH_LIMIT = _depth;
    }

    /// EXTERNAL

    /// @notice Checks if an org can make a transaction.
    /// @param _org Org address
    /// @return true/false
    function transact(address _org) external view returns (bool) {
        return ((_org != address(0)) && (orgMap[_org].status == 1));
    }

    /// @notice Add a new org to the network.
    /// @param _org     Org address
    /// @param _pOrg    Parent org
    /// @param _name    Name of the org
    /// @dev Check if the _org does not already exist as an account before calling
    function addOrg(
        address _org,
        address _pOrg,
        string calldata _name
    ) external onlyImplementation {
        require(!(orgExist(_org)), "ORG_ALREADY_EXIST");

        if (_pOrg == address(0)) {
            //root
            orgMap[_org] = Org(_org, _pOrg, _org, _name, 1, new address[](0), 1);
        } else {
            require(orgExist(_pOrg), "INVALID_PORG");
            require(orgMap[_pOrg].subOrgs.length < BREADTH_LIMIT, "BREADTH_EXCEEDED");
            require(orgMap[_pOrg].level < DEPTH_LIMIT, "DEPTH_EXCEEDED");

            // example: (org) google, (suborg) google.paris
            string memory name = string(abi.encodePacked((orgMap[_pOrg].name), ".", _name));

            orgMap[_pOrg].subOrgs.push(_org);

            orgMap[_org] = Org(
                _org,
                _pOrg,
                orgMap[_org].uOrg,
                name,
                orgMap[_pOrg].level + 1,
                new address[](0),
                1
            );
        }
        emit OrgCreated(_org, _pOrg, orgMap[_org].uOrg, orgMap[_org].name, orgMap[_org].level, 1);
    }

    /// @notice Updates the status of an org.
    /// @param _org     Org address
    /// @param _action  Action being performed
    /// This function can be called for the following actions:
    ///     1 - Suspend - called by admin
    ///     2 - Reactivate - called by admin
    /// @dev should only be called by the admin.
    function updateOrgStatus(address _org, uint256 _action) external onlyImplementation {
        require(orgExist(_org), "ORG_ALREADY_EXIST");
        require((_action == 1 || _action == 2), "INVALID_ACTION");
        if (_action == 1) {
            _suspendOrg(_org);
        } else if (_action == 2) {
            _revokeOrg(_org);
        }
    }

    /// EXTERNAL VIEW

    /// @notice Confirms that the org status is same as passed status
    /// @param _org     Org address
    /// @param _status  Org status
    /// @return true/false
    /// @dev 1 - active. 2 - suspended.
    function orgStatus(address _org, uint256 _status) public view returns (bool) {
        return (orgMap[_org].status == _status);
    }

    /// @notice Confirms if the given org exists in the network
    /// @param _org Org address
    /// @return true/false
    function orgExist(address _org) public view returns (bool) {
        return (orgMap[_org].org != address(0));
    }

    /// INTERNAL

    /// @notice Suspend an org
    /// @param _org Org address
    function _suspendOrg(address _org) internal {
        require(orgStatus(_org, 1), "ALREADY_SUPENDED");
        orgMap[_org].status = 2;
        emit OrgStatusUpdated(_org, 2);
    }

    /// @notice Sevoke an org suspension
    /// @param _org Org address
    function _revokeOrg(address _org) internal {
        require(orgStatus(_org, 2), "ALREADY_REVOKED");
        orgMap[_org].status = 1;
        emit OrgStatusUpdated(_org, 1);
    }
}
