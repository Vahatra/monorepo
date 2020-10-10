pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";

/// @dev Token based on ERC1155.
contract V1155 {
    using SafeMath for uint256;

    // tokenId => (owner => balance).
    mapping(uint256 => mapping(address => uint256)) internal balances;

    // tokenId => creators id of token to its creator
    mapping(uint256 => address) public idToCreator;

    // owner => (operator => approved)
    mapping(address => mapping(address => bool)) internal operatorApproval;

    // tokenId => uri id of a token to its metadata uri (unused for now).
    mapping(uint256 => string) internal idToUri;

    // A nonce to ensure a unique id for each mint.
    uint256 public tokenNonce;

    // A nonce to ensure a unique id for each event.
    uint256 internal eventNonce;

    modifier creatorOnly(uint256 _token) {
        require(idToCreator[_token] == msg.sender, "Creator only");
        _;
    }

    modifier canOperate(address _sender, address _receiver) {
        require(_receiver != address(0x0), "Address must be non-zero.");
        require(
            _sender == msg.sender ||
                operatorApproval[_sender][msg.sender] == true,
            "Need operator approval for 3rd party transfers."
        );
        _;
    }

    /// @dev Emits when tokens are transferred, including zero value transfers as well as minting or burning.
    /// @param _id id of the event.
    /// @param _sender address of the holder whose balance is decreased.
    /// @param _receiver address of the recipient whose balance is increased.
    /// @param _token token type being transferred.
    /// @param _value number of tokens the holder balance is decreased by and match what the recipient balance is increased by.
    // When minting tokens, the `_sender` argument MUST be set to `0x0` (i.e. zero address).
    // When burning tokens, the `_receiver` argument MUST be set to `0x0` (i.e. zero address).
    // When minting tokens, the `_parentId` argument MUST be set to `0`.
    event GraphTransfer(
        uint256 indexed _id,
        address _sender,
        address _receiver,
        uint256 _token,
        uint256 _value
    );

    /// @dev Emits when approval for a second party/operator address to manage all tokens for an owner address is enabled or disabled (absence of an event assumes disabled).
    event ApprovalForAll(
        address indexed _owner,
        address indexed _operator,
        bool _approved
    );

    /// @dev Transfers `_value` amount of an `_token` sender the `_sender` address to the `_receiver` address specified.
    /// @param _sender address of the holder whose balance is decreased.
    /// @param _receiver address of the recipient whose balance is increased.
    /// @param _token token type being transferred.
    /// @param _value number of tokens the holder balance is decreased by and match what the recipient balance is increased by.
    function transfer(
        address _sender,
        address _receiver,
        uint256 _token,
        uint256 _value
    ) external canOperate(_sender, _receiver) {
        _transfer(_sender, _receiver, _token, _value);
    }

    /// @dev Actually performs the transfer.
    function _transfer(
        address _sender,
        address _receiver,
        uint256 _token,
        uint256 _value
    ) internal {
        balances[_token][_sender] = balances[_token][_sender].sub(_value);
        balances[_token][_receiver] = _value.add(balances[_token][_receiver]);

        emit GraphTransfer(eventNonce, _sender, _receiver, _token, _value);
    }

    /// @dev Get the balance of an account's Tokens.
    /// @param _owner address of the token holder
    /// @param _id id of the token
    /// @return owner's balance of the Token type requested
    function balanceOf(address _owner, uint256 _id)
        external
        view
        returns (uint256)
    {
        return balances[_id][_owner];
    }

    /// @dev Get the balance of multiple account/token pairs
    /// @param _owners addresses of the token holders
    /// @param _ids ids of the Tokens
    /// @return owner's balance of the Token types requested (i.e. balance for each (owner, id) pair)
    function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids)
        external
        view
        returns (uint256[] memory)
    {
        require(_owners.length == _ids.length, "Array lenght must match.");

        uint256[] memory balances_ = new uint256[](_owners.length);

        for (uint256 i = 0; i < _owners.length; ++i) {
            balances_[i] = balances[_ids[i]][_owners[i]];
        }

        return balances_;
    }

    /// @dev Enable or disable approval for a third party ("operator") to manage all of the caller's tokens.
    /// @param _operator address to add to the set of authorized operators.
    /// @param _approved true if the operator is approved, false to revoke approval.
    function setApprovalForAll(address _operator, bool _approved) external {
        operatorApproval[msg.sender][_operator] = _approved;
        emit ApprovalForAll(msg.sender, _operator, _approved);
    }

    /// @dev Queries the approval status of an operator for a given owner.
    /// @param _owner owner of the tokens.
    /// @param _operator address of authorized operator.
    /// @return true if the operator is approved, false to revoke approval.
    function isApprovedForAll(address _owner, address _operator)
        external
        view
        returns (bool)
    {
        return operatorApproval[_owner][_operator];
    }

    /// @dev Mints an `_initialSupply` amount(s) of a new token to the minter (msg.sender for now).
    /// @param _initialSupply number of token the minter balance is increased by.
    function mint(uint256 _initialSupply) external {
        uint256 tokenId = ++tokenNonce;
        idToCreator[tokenId] = msg.sender;
        balances[tokenId][msg.sender] = _initialSupply;

        emit GraphTransfer(
            ++eventNonce,
            address(0x0),
            msg.sender,
            tokenId,
            _initialSupply
        );
    }

    /// @dev Burns a `_value` amount(s) of `_id` sender the `_sender` address.
    /// @param _sender address of the owner.
    /// @param _token id of the token.
    /// @param _value amount to be burnt.
    function burn(
        address _sender,
        uint256 _token,
        uint256 _value
    ) external canOperate(_sender, _sender) {
        balances[_token][_sender] = balances[_token][_sender].sub(_value);

        emit GraphTransfer(++eventNonce, _sender, address(0x0), _token, _value);
    }
}
