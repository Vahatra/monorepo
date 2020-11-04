// SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/access/Ownable.sol";
import "./SwapVerifier.sol";
import "./Account.sol";
import "./Token.sol";

/// @title Implementation contract.
/// @notice This contract is wrapper arround the implementation contracts (Account, Token).
/// @dev Function docs are inside the implementation contracts.
contract implementation is Ownable, SwapVerifier {
    Account private account;
    Token private token;

    /// @notice Constructor accepts the contracts addresses of other deployed contracts.
    /// @param _account Address of account manager contract.
    /// @param _token   Address of token manager contract.
    constructor(address _account, address _token) public {
        account = Account(_account);
        account.initialize(address(this));
        account.addAccount(msg.sender, address(0), "OWNER");

        token = Token(_token);
        token.initialize(address(this));
    }

    /// @notice Verifies if _acc exist and active.
    modifier isActive(address _acc) {
        require(_isActive(_acc), "NOT_LISTED_OR_INACTIVE_ACCOUNT");
        _;
    }

    /// @notice Verifies if msg.sender is the parent account of _acc.
    modifier isParent(address _acc) {
        require(msg.sender == _parentAccount(_acc), "NOT_PARENT_ACCOUNT");
        _;
    }

    /// ACCOUNT

    function register(string calldata _name) external {
        account.addAccount(msg.sender, address(0), _name);
    }

    function addSubAccount(address _acc, string calldata _name) external {
        account.addAccount(_acc, msg.sender, _name);
    }

    function suspendAccount(address _acc) external isParent(_acc) {
        account.updateAccountStatus(_acc, 1);
    }

    function reactivateAccount(address _acc) external isParent(_acc) {
        account.updateAccountStatus(_acc, 2);
    }

    function blacklistAccount(address _acc) external onlyOwner {
        account.updateAccountStatus(_acc, 3);
    }

    function recoverAccount(address _acc) external onlyOwner {
        account.updateAccountStatus(_acc, 4);
    }

    function authorizeOperator(address _operator) external {
        account.authorizeOperator(msg.sender, _operator);
    }

    function revokeOperator(address _operator) external {
        account.revokeOperator(msg.sender, _operator);
    }

    function _isActive(address _acc) internal view returns (bool) {
        return account.isActive(_acc);
    }

    function _parentAccount(address _acc) internal view returns (address) {
        return account.getParentAccount(_acc);
    }

    function _isOperatorFor(address _operator, address _acc) internal view returns (bool) {
        return account.isOperatorFor(_operator, _acc);
    }

    /// TOKEN

    function create(
        string calldata _uri,
        bool _isNF,
        bytes calldata _data
    ) external onlyOwner {
        token.create(msg.sender, _uri, _isNF, _data);
    }

    function mintFungible(
        address[] calldata _to,
        uint256 _id,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyOwner {
        token.mintFungible(msg.sender, _to, _id, _amounts, _data);
    }

    function mintNonFungible(
        address[] calldata _to,
        uint256 _type,
        bytes calldata _data
    ) external onlyOwner {
        token.mintNonFungible(msg.sender, _to, _type, _data);
    }

    function send(
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external isActive(msg.sender) {
        token.send(msg.sender, msg.sender, _to, _ids, _amounts, _data, "");
    }

    function operatorSend(
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external isActive(_from) {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        token.send(msg.sender, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    function burn(
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external isActive(msg.sender) {
        token.burn(msg.sender, msg.sender, _ids, _amounts, _data, "");
    }

    function operatorBurn(
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external isActive(_from) {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        token.burn(msg.sender, _from, _ids, _amounts, _data, _operatorData);
    }

    function swap(
        SwapLib.Swap memory _swap,
        uint256 _nonce,
        uint256 _expiry,
        uint8 _v,
        bytes32 _r,
        bytes32 _s,
        bytes memory _data
    ) public isActive(msg.sender) {
        address signer = swapVerify(_swap, _nonce, _expiry, _v, _r, _s);
        require(_isActive(signer), "NOT_LISTED_OR_INACTIVE_ACCOUNT");
        token.swap(msg.sender, signer, _swap, _data);
    }
}
