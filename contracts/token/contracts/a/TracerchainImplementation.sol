pragma solidity ^0.6.0;

import "./OrgManager.sol";
import "./TokenManager.sol";
import "./BaseErrors.sol";

/// @title Tracerchain Implementation Contract
/// @notice This contract holds implementation logic for all tracerchain
/// related functionality.
contract TracerchainImplementation is BaseErrors {
    OrgManager private orgManager;
    TokenManager private tokenManager;

    address private admin;

    /// MODIFIER

    /// @notice confirms that the caller is the admin account
    modifier isAdmin() {
        require(msg.sender == admin, NOT_ADMIN);
        _;
    }

    /// @notice confirms that the caller is an active org.
    /// @dev 1 - active
    modifier isOrg() {
        require(_orgStatus(msg.sender, 1), INVALID_ORG);
        _;
    }

    /// CONST

    /// @notice constructor accepts the contracts addresses of other deployed
    /// contracts of the tracerchain model and assigns the admin account.
    /// @param _orgManager - address of org manager contract
    /// @param _tokenManager - address of token manager contract
    /// @param _admin - address of admin account
    constructor(
        address _orgManager,
        address _tokenManager,
        address _admin
    ) public {
        orgManager = OrgManager(_orgManager);
        orgManager.init(address(this));
        tokenManager = TokenManager(_tokenManager);
        tokenManager.init(address(this));
        admin = _admin;
        orgManager.addOrg(_admin, address(0), "ADMIN_ORG", "ADMIN_ROLE");
        orgManager.setTxCount(_admin, 1000000000);
    }

    /// ORG

    /// @notice sets the transaction count of an org.
    /// @param _org - org address
    /// @param _txCount - transaction count
    function setTxCount(address _org, uint256 _txCount) external isAdmin {
        orgManager.setTxCount(_org, _txCount);
    }

    /// @notice add a new org to the network.
    /// @param _org - org address
    /// @param _pOrg -parent org
    /// @param _name - name of the org
    /// @param _role - role of the org
    function addOrg(
        address _org,
        address _pOrg,
        string calldata _name,
        string calldata _role
    ) external isAdmin {
        orgManager.addOrg(_org, _pOrg, _name, _role);
    }

    /// @notice updates the status of an org.
    /// @param _org - org address
    /// @param _action - action being performed
    /// This function can be called for the following actions:
    ///     1 - Suspend - called by admin
    ///     2 - Reactivate - called by admin
    function updateOrgStatus(address _org, uint256 _action) external isAdmin {
        orgManager.updateOrgStatus(_org, _action);
    }

    /// @notice checks if the passed org can make a transaction.
    /// @param _adr - address of an org
    /// @return true/false
    /// @dev should be called before each Token function call.
    function _transact(address _adr) internal returns (bool) {
        address _org = _adr;
        if (!(orgManager.transact(_org))) {
            revert(CANNOT_TRANSACT);
        }
    }

    /// @notice checks if the passed org exists or not.
    /// @param _org - org address
    /// @return true/false
    function _orgExists(address _org) internal view returns (bool) {
        return orgManager.orgExists(_org);
    }

    /// @notice confirms that org status is same as passed status
    /// @param _org - org address
    /// @return true/false
    function _orgStatus(address _org, uint256 _status)
        internal
        view
        returns (bool)
    {
        return orgManager.orgStatus(_org, _status);
    }

    /// TOKEN
    /// TO DISCUSS, NO ROLE CHECK YET.

    /// createTokenType - the admin only (or org?)
    /// @notice function to create a new tokentype
    /// @notice msg.sender is the _creator (for now).
    /// @param _parent the parent type of the token.
    /// @param _name name of the token type.
    /// @param _uri point a JSON file that conforms to the "ERC-1155 Metadata JSON Schema".
    function createTokenType(
        uint256 _parent,
        string calldata _name,
        string calldata _uri
    ) external {
        if (_parent == 0) {
            require(msg.sender == admin, NOT_ADMIN);
        } else {
            _transact(msg.sender);
        }
        tokenManager.createTokenType(msg.sender, _parent, _name, _uri);
    }

    /// setUri - only creator (already covered inside token manager), other? role?
    /// @notice set the URI of a token.
    /// @notice msg.sender is the _owner (for now).
    /// @param _tokenType of token.
    /// @param _uri point a JSON file that conforms to the "ERC-1155 Metadata JSON Schema".
    function setUri(uint256 _tokenType, string calldata _uri) external {
        _transact(msg.sender);
        tokenManager.setUri(msg.sender, _tokenType, _uri);
    }

    /// mint - only miner role, account exists, other? role?
    /// @notice mint a new tokens.
    /// @notice msg.sender is the _owner (for now).
    /// @param _tokenTypes the token types the `_owner` are minting.
    /// @param _amounts the corresponding amounts.
    function mint(uint256[] calldata _tokenTypes, uint256[] calldata _amounts)
        external
    {
        _transact(msg.sender);
        tokenManager.mint(msg.sender, _tokenTypes, _amounts);
    }

    /// burn - only refiner role?, only owner (already covered inside token manager)
    /// @notice msg.sender is the _owner (for now).
    /// @param _tokens the tokens the `_owner` are burning.
    /// @param _amounts the corresponding amounts.
    function burn(uint256[] calldata _tokens, uint256[] calldata _amounts)
        external
    {
        _transact(msg.sender);
        tokenManager.burn(msg.sender, _tokens, _amounts);
    }

    /// transfer - only owner (already covered inside token manager), other? role?
    /// @notice msg.sender is the _sender (for now).
    /// @param _tokens the tokens the `_owner` are transferring.
    /// @param _amounts the corresponding amounts.
    function transfer(
        address _receiver,
        uint256[] calldata _tokens,
        uint256[] calldata _amounts
    ) external {
        _transact(msg.sender);
        tokenManager.transfer(msg.sender, _receiver, _tokens, _amounts);
    }

    /// setProducts - only creator (already covered inside token manager), other? role?
    /// @dev sets what types of tokens can be produced with the correct combination of tokenTypes.
    /// @notice msg.sender is the _owner (for now).
    /// @param _reactantTypes the combination of types to be consumed.
    /// @param _productTypes the types to be produced by the combination of  `_reactantTypes`.
    function setProducts(
        uint256[] calldata _reactantTypes,
        uint256[] calldata _productTypes
    ) external {
        _transact(msg.sender);
        tokenManager.setProducts(msg.sender, _reactantTypes, _productTypes);
    }

    /// transform - only refiner role?, only owner (already covered inside token manager), other?
    /// @notice msg.sender is the owner (for now).
    /// @param _reactantTokens the tokens used for the transformation. Their types will be looked up to find what are the corresponding product types.
    /// @param _reactantAmounts the amount of reactant tokens.
    /// @param _productAmounts the amount of product tokens.
    function transform(
        uint256[] calldata _reactantTokens,
        uint256[] calldata _reactantAmounts,
        uint256[] calldata _productAmounts
    ) external {
        _transact(msg.sender);
        tokenManager.transform(
            msg.sender,
            _reactantTokens,
            _reactantAmounts,
            _productAmounts
        );
    }
}
