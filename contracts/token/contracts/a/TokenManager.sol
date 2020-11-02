pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "./BaseErrors.sol";

/// @title Token manager contract
/// @notice This contract holds implementation logic for all token management
/// functionality. This can be called only by the implementation contract.
contract TokenManager is BaseErrors {
    using SafeMath for uint256;

    bool private booted = false;
    address private implementation;

    struct Token {
        address owner;
        uint256 tokenType;
        uint256 balance;
        uint256 origin;
    }
    uint256 tokenNonce;
    mapping(uint256 => Token) tokens;

    struct TokenType {
        address creator;
        uint256 parent;
        string name;
    }
    uint256 tokenTypeNonce;
    mapping(uint256 => TokenType) tokenTypes;

    mapping(address => mapping(bytes32 => uint256[])) formulas;

    mapping(bytes32 => bool) exchangeHashes;

    /// EVENTS

    /// @dev Create MUST emit when a tokenType is created.
    event GraphTokenType(
        address indexed creator,
        uint256 tokenType,
        string name,
        string uri
    );

    /// @dev MUST emit when the URI is updated for a token ID.
    event GraphURI(string uri, uint256 indexed tokenType);

    /// @dev Either TransferSingle or TransferBatch MUST emit when tokens are transferred.
    event GraphTransfer(
        address indexed sender,
        address indexed receiver,
        uint256[] tokens,
        uint256[] amounts
    );

    /// @dev SetProducts MUST emit when a new reactants/products has been set.
    event GraphFormula(
        address indexed owner,
        uint256[] reactantTypes,
        uint256[] productTypes
    );

    /// @dev Exchange MUST emit when a tokens are transformed.
    event GraphTransform(
        address indexed owner,
        uint256[] burnedTokens,
        uint256[] reactantAmounts,
        uint256[] mintedTokens,
        uint256[] productAmounts
    );

    /// MODIFIERS

    /// @notice confirms that the caller is the address of implementation contract
    modifier onlyImplementation {
        require(msg.sender == implementation, INVALID_CALLER);
        _;
    }

    /// @notice sets the implementation contract address.
    function init(address _implementation) external {
        require(!booted, INVALID_BOOT_STATUS);
        implementation = _implementation;
        booted = true;
    }

    /// EXTERNAL

    /// @notice function to create a new tokentype
    /// @param _creator the creator of new type.
    /// @param _parent the parent type of the token.
    /// @param _name name of the token type.
    /// @param _uri point a JSON file that conforms to the "ERC-1155 Metadata JSON Schema".
    function createTokenType(
        address _creator,
        uint256 _parent,
        string calldata _name,
        string calldata _uri
    ) external {
        tokenTypeNonce++;
        tokenTypes[tokenTypeNonce] = TokenType({
            creator: _creator,
            parent: _parent,
            name: _name
        });

        emit GraphTokenType(_creator, tokenTypeNonce, _name, _uri);
    }

    /// @dev set the URI of a token.
    /// @param _owner token owner.
    /// @param _tokenType of token.
    /// @param _uri point a JSON file that conforms to the "ERC-1155 Metadata JSON Schema".
    function setUri(
        address _owner,
        uint256 _tokenType,
        string calldata _uri
    ) external {
        require(bytes(_uri).length > 0, INVALID_URI);
        require(_creator(_tokenType) == _owner, NOT_CREATOR);

        emit GraphURI(_uri, _tokenType);
    }

    /// @param _owner address of the new tokens to be minted.
    /// @param _tokenTypes the token types the `_owner` are minting.
    /// @param _amounts the corresponding amounts.
    function mint(
        address _owner,
        uint256[] calldata _tokenTypes,
        uint256[] calldata _amounts
    ) external {
        require(_tokenTypes.length == _amounts.length, LENGTH_MISMATCH);
        uint256[] memory newTokens = _mint(_owner, _tokenTypes, _amounts);

        emit GraphTransfer(address(0x0), _owner, newTokens, _amounts);
    }

    /// @param _owner address of the tokens to be burned.
    /// @param _tokens the tokens the `_owner` are burning.
    /// @param _amounts the corresponding amounts.
    function burn(
        address _owner,
        uint256[] calldata _tokens,
        uint256[] calldata _amounts
    ) external {
        require(_tokens.length == _amounts.length, LENGTH_MISMATCH);
        _burn(_owner, _tokens, _amounts);

        emit GraphTransfer(_owner, address(0x0), _tokens, _amounts);
    }

    /// @param _sender address of the sender.
    /// @param _receiver address of the receiver.
    /// @param _tokens the tokens the `_owner` are transferring.
    /// @param _amounts the corresponding amounts.
    function transfer(
        address _sender,
        address _receiver,
        uint256[] calldata _tokens,
        uint256[] calldata _amounts
    ) external {
        require(_tokens.length == _amounts.length, LENGTH_MISMATCH);
        uint256[] memory newTokens = _transfer(
            _sender,
            _receiver,
            _tokens,
            _amounts
        );

        emit GraphTransfer(_sender, _receiver, newTokens, _amounts);
    }

    /// @dev sets what types of tokens can be produced with the correct combination of tokenTypes.
    /// @param _owner the owner.
    /// @param _reactantTypes the combination of types to be consumed.
    /// @param _productTypes the types to be produced by the combination of  `_reactantTypes`.
    function setProducts(
        address _owner,
        uint256[] calldata _reactantTypes,
        uint256[] calldata _productTypes
    ) external {
        // This loop can discussed, maybe not necessary as non-creators will never be able to mint tokens
        // Leaving it for now.
        for (uint256 i = 0; i < _productTypes.length; i++) {
            require(_creator(_productTypes[i]) == _owner, NOT_CREATOR);
        }
        uint256 len = _reactantTypes.length;
        require(len != 0, EMPTY_ARRAY);
        uint256 previous = _reactantTypes[0];
        for (uint256 i = 1; i < len; i++) {
            require(previous < _reactantTypes[i], UNSORTED_ARRAY);
            previous = _reactantTypes[i];
        }
        formulas[_owner][keccak256(
            abi.encodePacked(_reactantTypes)
        )] = _productTypes;

        emit GraphFormula(_owner, _reactantTypes, _productTypes);
    }

    /// @param _owner The owner.
    /// @param _reactantTokens the tokens used for the transformation. Their types will be looked up to find what are the corresponding product types.
    /// @param _reactantAmounts the amount of reactant tokens.
    /// @param _productAmounts the amount of product tokens.
    function transform(
        address _owner,
        uint256[] calldata _reactantTokens,
        uint256[] calldata _reactantAmounts,
        uint256[] calldata _productAmounts
    ) external {
        require(
            _reactantTokens.length == _reactantAmounts.length,
            LENGTH_MISMATCH
        );

        uint256[] memory mintedTokens = _transform(
            _owner,
            _reactantTokens,
            _reactantAmounts,
            _productAmounts
        );

        emit GraphTransform(
            _owner,
            _reactantTokens,
            _reactantAmounts,
            mintedTokens,
            _productAmounts
        );
    }

    /// EXTERNAL VIEW

    function graphParent(uint256 _tokenType) external view returns (uint256) {
        return tokenTypes[_tokenType].parent;
    }

    function graphOwner(uint256 _token) external view returns (address) {
        return tokens[_token].owner;
    }

    function graphType(uint256 _token) external view returns (uint256) {
        return tokens[_token].tokenType;
    }

    function graphBalance(uint256 _token) external view returns (uint256) {
        return tokens[_token].balance;
    }

    function graphOrigin(uint256 _token) external view returns (uint256) {
        return tokens[_token].origin;
    }

    /// INTERNAL

    function _transfer(
        address _sender,
        address _receiver,
        uint256[] memory _tokens,
        uint256[] memory _amounts
    ) internal returns (uint256[] memory newTokens) {
        uint256 len = _tokens.length;
        newTokens = new uint256[](len);
        for (uint256 i = 0; i < len; i++) {
            _debit(_sender, _tokens[i], _amounts[i]);
            newTokens[i] = ++tokenNonce;
            _credit(
                _receiver,
                tokenNonce,
                tokens[_tokens[i]].tokenType,
                _tokens[i],
                _amounts[i]
            );
        }
    }

    function _swap(
        address _sender,
        uint256[] memory _senderTokens,
        uint256[] memory _senderAmounts,
        address _receiver,
        uint256[] memory _receiverTokens,
        uint256[] memory _receiverAmounts
    )
        internal
        returns (
            uint256[] memory newSenderTokens,
            uint256[] memory newReceiverTokens
        )
    {
        newSenderTokens = _transfer(
            _sender,
            _receiver,
            _senderTokens,
            _senderAmounts
        );
        newReceiverTokens = _transfer(
            _receiver,
            _sender,
            _receiverTokens,
            _receiverAmounts
        );
    }

    function _transform(
        address _owner,
        uint256[] memory _reactantTokens,
        uint256[] memory _reactantAmounts,
        uint256[] memory _productAmounts
    ) internal returns (uint256[] memory mintedTokens) {
        {
            uint256[] memory productTypes = _lookupProducts(
                _owner,
                _lookupUniqueRootTypes(_lookupTypes(_reactantTokens))
            );
            mintedTokens = _mint(_owner, productTypes, _productAmounts);
        }

        _burn(_owner, _reactantTokens, _reactantAmounts);
    }

    function _mint(
        address _owner,
        uint256[] memory _tokenTypes,
        uint256[] memory _amounts
    ) internal returns (uint256[] memory newTokens) {
        // may need to check error here
        uint256 len = _tokenTypes.length;
        require(len != 0, EMPTY_ARRAY);
        newTokens = new uint256[](len);
        for (uint256 i = 0; i < len; i++) {
            require(_creator(_tokenTypes[i]) == _owner, NOT_CREATOR);
            newTokens[i] = ++tokenNonce;
            _credit(_owner, tokenNonce, _tokenTypes[i], 0, _amounts[i]);
        }
    }

    function _burn(
        address _owner,
        uint256[] memory _tokens,
        uint256[] memory _amounts
    ) internal {
        uint256 len = _tokens.length;
        for (uint256 i = 0; i < len; i++) {
            _debit(_owner, _tokens[i], _amounts[i]);
        }
    }

    function _credit(
        address _owner,
        uint256 _id,
        uint256 _tokenType,
        uint256 _origin,
        uint256 _amount
    ) internal {
        tokens[_id] = Token({
            owner: _owner,
            tokenType: _tokenType,
            origin: _origin,
            balance: _amount
        });
    }

    function _debit(
        address _owner,
        uint256 _id,
        uint256 _amount
    ) internal {
        require(tokens[_id].owner == _owner, NOT_OWNER);
        tokens[_id].balance = tokens[_id].balance.sub(_amount);
    }

    /// INTERNAL VIEW

    function _creator(uint256 _tokenType) internal view returns (address) {
        return tokenTypes[_tokenType].creator;
    }

    /// @param _owner the lookup on this particular address.
    /// @param _tokenTypes the token types owned by the _owner.
    /// @return the token types resulting from combining _tokenTypes.
    function _lookupProducts(address _owner, uint256[] memory _tokenTypes)
        internal
        view
        returns (uint256[] memory)
    {
        uint256 len = _tokenTypes.length;
        require(len != 0, EMPTY_ARRAY);
        // All checks need to be ascertained on setProducts.
        // Up to the front to perform proper lookup or return empty formula
        // uint256 previous = _tokenTypes[0];
        // for (uint256 i = 1; i < _tokenTypes.length; i++) {
        //     require(previous < _tokenTypes[i], UNSORTED_ARRAY);
        //     previous = _tokenTypes[i];
        // }
        return formulas[_owner][keccak256(abi.encodePacked(_tokenTypes))];
    }

    /// @dev lookup the type of a single token
    /// @param _token id of token of which the type to look up.
    function _lookupType(uint256 _token) internal view returns (uint256) {
        // This will need to be changed later
        return tokens[_token].tokenType;
    }

    /// @dev Query up the token tree to find the type of the original token.
    /// @param _tokens the tokens to lookup.
    /// @return the corresponding of each tokens input.
    function _lookupTypes(uint256[] memory _tokens)
        internal
        view
        returns (uint256[] memory)
    {
        uint256[] memory toks = new uint256[](_tokens.length);
        for (uint256 i = 0; i < _tokens.length; i++) {
            toks[i] = _lookupType(_tokens[i]);
        }
        return toks;
    }

    /// @dev This function needs to be written in assembly.
    /// @dev Leaving for now for clarification, but I will optimize.
    /// @dev lookup types with unique ids. This is necessary for `transform`.
    /// @param _tokenTypes ids of tokenTypes. The ids are expected to have types in ascending order.
    function _lookupUniqueRootTypes(uint256[] memory _tokenTypes)
        internal
        view
        returns (uint256[] memory uniqueRootTypes)
    {
        uint256 len = _tokenTypes.length;
        require(len != 0, EMPTY_ARRAY);
        // initialize as same length;
        uniqueRootTypes = new uint256[](len);
        uint256 previous = _lookupRootType(_tokenTypes[0]);
        uniqueRootTypes[0] = previous;
        uint256 resultLen = 1;
        for (uint256 i = 1; i < len; i++) {
            uint256 nextType = _lookupRootType(_tokenTypes[i]);
            if (previous != nextType) {
                uniqueRootTypes[resultLen++] = nextType;
                previous = nextType;
            }
        }
        assembly {
            mstore(uniqueRootTypes, resultLen)
        }
        return uniqueRootTypes;
    }

    /// @dev lookup the root type of a single type
    /// @param _type id of tokenType of which the root type is sought.
    function _lookupRootType(uint256 _type) internal view returns (uint256) {
        uint256 parent;
        uint256 t = _type;
        while ((parent = tokenTypes[t].parent) != 0) {
            t = parent;
        }

        return t;
    }
}
