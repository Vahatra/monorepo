// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/access/Ownable.sol";
import "./SwapVerifier.sol";
import "./Account.sol";
import "./Token.sol";

/// @title Token contract
/// @notice This contract holds implementation logic for all token management
// contract Token is SwapVerifier, MixinNF, Initializable, Pausable, AccessControl {
contract implementation is Ownable, SwapVerifier {
    Account private account;
    Token private token;

    /// @notice constructor accepts the contracts addresses of other deployed contracts.
    /// @param _account - address of org manager contract
    /// @param _token - address of token manager contract
    constructor(address _account, address _token) public {
        account = Account(_account);
        token = Token(_token);
        account.initialize(address(this));
        token.initialize(address(this));
    }

    /// ACCOUNT

    function addAccount(
        address _acc,
        address _pAcc,
        string calldata _name
    ) external onlyOwner {
        if (_pAcc != address(0)) {
            require(msg.sender == _pAcc, "INVALID_CALLER");
        }
        account.addAccount(_acc, _pAcc, _name);
    }

    function updateAccountStatus(address _acc, uint256 _action) external {
        if (_action == 1 || _action == 2) {
            require(msg.sender == _parentAccount(_acc), "INVALID_CALLER");
        } else if (_action == 3 || _action == 4) {
            require(msg.sender == owner(), "INVALID_CALLER");
        }
        account.updateAccountStatus(_acc, _action);
    }

    function authorizeOperator(address _operator) external {
        account.authorizeOperator(msg.sender, _operator);
    }

    function revokeOperator(address _operator) external {
        account.revokeOperator(msg.sender, _operator);
    }

    function _accountActive(address _acc) internal view returns (bool) {
        return account.accountActive(_acc);
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
    ) external {
        require(_accountActive(msg.sender), "NOT_ACTIVE_ACCOUNT");
        token.send(msg.sender, _to, _ids, _amounts, _data);
    }

    function operatorSend(
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        require(_accountActive(_from), "NOT_ACTIVE_ACCOUNT");
        token.operatorSend(msg.sender, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    function burn(
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external {
        require(_accountActive(msg.sender), "NOT_ACTIVE_ACCOUNT");
        token.burn(msg.sender, _ids, _amounts, _data);
    }

    function operatorBurn(
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external {
        require(_isOperatorFor(msg.sender, _from), "INSUFFICIENT_ALLOWANCE");
        require(_accountActive(_from), "NOT_ACTIVE_ACCOUNT");
        token.operatorBurn(msg.sender, _from, _ids, _amounts, _data, _operatorData);
    }

    function swap(
        SwapLib.Swap memory _swap,
        uint256 _nonce,
        uint256 _expiry,
        uint8 _v,
        bytes32 _r,
        bytes32 _s,
        bytes memory _data
    ) public {
        require(_accountActive(msg.sender), "NOT_ACTIVE_ACCOUNT");
        address signer = swapVerify(_swap, _nonce, _expiry, _v, _r, _s);
        require(_accountActive(signer), "NOT_ACTIVE_ACCOUNT");
        token.swap(msg.sender, signer, _swap, _data);
    }
}
