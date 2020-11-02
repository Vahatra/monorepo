// File: @openzeppelin\contracts\math\SafeMath.sol

// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

/**
 * @dev Wrappers over Solidity's arithmetic operations with added overflow
 * checks.
 *
 * Arithmetic operations in Solidity wrap on overflow. This can easily result
 * in bugs, because programmers usually assume that an overflow raises an
 * error, which is the standard behavior in high level programming languages.
 * `SafeMath` restores this intuition by reverting the transaction when an
 * operation overflows.
 *
 * Using this library instead of the unchecked operations eliminates an entire
 * class of bugs, so it's recommended to use it always.
 */
library SafeMath {
    /**
     * @dev Returns the addition of two unsigned integers, reverting on
     * overflow.
     *
     * Counterpart to Solidity's `+` operator.
     *
     * Requirements:
     *
     * - Addition cannot overflow.
     */
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");

        return c;
    }

    /**
     * @dev Returns the subtraction of two unsigned integers, reverting on
     * overflow (when the result is negative).
     *
     * Counterpart to Solidity's `-` operator.
     *
     * Requirements:
     *
     * - Subtraction cannot overflow.
     */
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        return sub(a, b, "SafeMath: subtraction overflow");
    }

    /**
     * @dev Returns the subtraction of two unsigned integers, reverting with custom message on
     * overflow (when the result is negative).
     *
     * Counterpart to Solidity's `-` operator.
     *
     * Requirements:
     *
     * - Subtraction cannot overflow.
     */
    function sub(
        uint256 a,
        uint256 b,
        string memory errorMessage
    ) internal pure returns (uint256) {
        require(b <= a, errorMessage);
        uint256 c = a - b;

        return c;
    }

    /**
     * @dev Returns the multiplication of two unsigned integers, reverting on
     * overflow.
     *
     * Counterpart to Solidity's `*` operator.
     *
     * Requirements:
     *
     * - Multiplication cannot overflow.
     */
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        // Gas optimization: this is cheaper than requiring 'a' not being zero, but the
        // benefit is lost if 'b' is also tested.
        // See: https://github.com/OpenZeppelin/openzeppelin-contracts/pull/522
        if (a == 0) {
            return 0;
        }

        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");

        return c;
    }

    /**
     * @dev Returns the integer division of two unsigned integers. Reverts on
     * division by zero. The result is rounded towards zero.
     *
     * Counterpart to Solidity's `/` operator. Note: this function uses a
     * `revert` opcode (which leaves remaining gas untouched) while Solidity
     * uses an invalid opcode to revert (consuming all remaining gas).
     *
     * Requirements:
     *
     * - The divisor cannot be zero.
     */
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        return div(a, b, "SafeMath: division by zero");
    }

    /**
     * @dev Returns the integer division of two unsigned integers. Reverts with custom message on
     * division by zero. The result is rounded towards zero.
     *
     * Counterpart to Solidity's `/` operator. Note: this function uses a
     * `revert` opcode (which leaves remaining gas untouched) while Solidity
     * uses an invalid opcode to revert (consuming all remaining gas).
     *
     * Requirements:
     *
     * - The divisor cannot be zero.
     */
    function div(
        uint256 a,
        uint256 b,
        string memory errorMessage
    ) internal pure returns (uint256) {
        require(b > 0, errorMessage);
        uint256 c = a / b;
        // assert(a == b * c + a % b); // There is no case in which this doesn't hold

        return c;
    }

    /**
     * @dev Returns the remainder of dividing two unsigned integers. (unsigned integer modulo),
     * Reverts when dividing by zero.
     *
     * Counterpart to Solidity's `%` operator. This function uses a `revert`
     * opcode (which leaves remaining gas untouched) while Solidity uses an
     * invalid opcode to revert (consuming all remaining gas).
     *
     * Requirements:
     *
     * - The divisor cannot be zero.
     */
    function mod(uint256 a, uint256 b) internal pure returns (uint256) {
        return mod(a, b, "SafeMath: modulo by zero");
    }

    /**
     * @dev Returns the remainder of dividing two unsigned integers. (unsigned integer modulo),
     * Reverts with custom message when dividing by zero.
     *
     * Counterpart to Solidity's `%` operator. This function uses a `revert`
     * opcode (which leaves remaining gas untouched) while Solidity uses an
     * invalid opcode to revert (consuming all remaining gas).
     *
     * Requirements:
     *
     * - The divisor cannot be zero.
     */
    function mod(
        uint256 a,
        uint256 b,
        string memory errorMessage
    ) internal pure returns (uint256) {
        require(b != 0, errorMessage);
        return a % b;
    }
}

// File: @openzeppelin\contracts\utils\Address.sol

/**
 * @dev Collection of functions related to the address type
 */
library Address {
    /**
     * @dev Returns true if `account` is a contract.
     *
     * [IMPORTANT]
     * ====
     * It is unsafe to assume that an address for which this function returns
     * false is an externally-owned account (EOA) and not a contract.
     *
     * Among others, `isContract` will return false for the following
     * types of addresses:
     *
     *  - an externally-owned account
     *  - a contract in construction
     *  - an address where a contract will be created
     *  - an address where a contract lived, but was destroyed
     * ====
     */
    function isContract(address account) internal view returns (bool) {
        // This method relies in extcodesize, which returns 0 for contracts in
        // construction, since the code is only stored at the end of the
        // constructor execution.

        uint256 size;
        // solhint-disable-next-line no-inline-assembly
        assembly {
            size := extcodesize(account)
        }
        return size > 0;
    }

    /**
     * @dev Replacement for Solidity's `transfer`: sends `amount` wei to
     * `recipient`, forwarding all available gas and reverting on errors.
     *
     * https://eips.ethereum.org/EIPS/eip-1884[EIP1884] increases the gas cost
     * of certain opcodes, possibly making contracts go over the 2300 gas limit
     * imposed by `transfer`, making them unable to receive funds via
     * `transfer`. {sendValue} removes this limitation.
     *
     * https://diligence.consensys.net/posts/2019/09/stop-using-soliditys-transfer-now/[Learn more].
     *
     * IMPORTANT: because control is transferred to `recipient`, care must be
     * taken to not create reentrancy vulnerabilities. Consider using
     * {ReentrancyGuard} or the
     * https://solidity.readthedocs.io/en/v0.5.11/security-considerations.html#use-the-checks-effects-interactions-pattern[checks-effects-interactions pattern].
     */
    function sendValue(address payable recipient, uint256 amount) internal {
        require(address(this).balance >= amount, "Address: insufficient balance");

        // solhint-disable-next-line avoid-low-level-calls, avoid-call-value
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "Address: unable to send value, recipient may have reverted");
    }

    /**
     * @dev Performs a Solidity function call using a low level `call`. A
     * plain`call` is an unsafe replacement for a function call: use this
     * function instead.
     *
     * If `target` reverts with a revert reason, it is bubbled up by this
     * function (like regular Solidity function calls).
     *
     * Returns the raw returned data. To convert to the expected return value,
     * use https://solidity.readthedocs.io/en/latest/units-and-global-variables.html?highlight=abi.decode#abi-encoding-and-decoding-functions[`abi.decode`].
     *
     * Requirements:
     *
     * - `target` must be a contract.
     * - calling `target` with `data` must not revert.
     *
     * _Available since v3.1._
     */
    function functionCall(address target, bytes memory data) internal returns (bytes memory) {
        return functionCall(target, data, "Address: low-level call failed");
    }

    /**
     * @dev Same as {xref-Address-functionCall-address-bytes-}[`functionCall`], but with
     * `errorMessage` as a fallback revert reason when `target` reverts.
     *
     * _Available since v3.1._
     */
    function functionCall(
        address target,
        bytes memory data,
        string memory errorMessage
    ) internal returns (bytes memory) {
        return _functionCallWithValue(target, data, 0, errorMessage);
    }

    /**
     * @dev Same as {xref-Address-functionCall-address-bytes-}[`functionCall`],
     * but also transferring `value` wei to `target`.
     *
     * Requirements:
     *
     * - the calling contract must have an ETH balance of at least `value`.
     * - the called Solidity function must be `payable`.
     *
     * _Available since v3.1._
     */
    function functionCallWithValue(
        address target,
        bytes memory data,
        uint256 value
    ) internal returns (bytes memory) {
        return
            functionCallWithValue(
                target,
                data,
                value,
                "Address: low-level call with value failed"
            );
    }

    /**
     * @dev Same as {xref-Address-functionCallWithValue-address-bytes-uint256-}[`functionCallWithValue`], but
     * with `errorMessage` as a fallback revert reason when `target` reverts.
     *
     * _Available since v3.1._
     */
    function functionCallWithValue(
        address target,
        bytes memory data,
        uint256 value,
        string memory errorMessage
    ) internal returns (bytes memory) {
        require(address(this).balance >= value, "Address: insufficient balance for call");
        return _functionCallWithValue(target, data, value, errorMessage);
    }

    function _functionCallWithValue(
        address target,
        bytes memory data,
        uint256 weiValue,
        string memory errorMessage
    ) private returns (bytes memory) {
        require(isContract(target), "Address: call to non-contract");

        // solhint-disable-next-line avoid-low-level-calls
        (bool success, bytes memory returndata) = target.call{value: weiValue}(data);
        if (success) {
            return returndata;
        } else {
            // Look for revert reason and bubble it up if present
            if (returndata.length > 0) {
                // The easiest way to bubble the revert reason is using memory via assembly

                // solhint-disable-next-line no-inline-assembly
                assembly {
                    let returndata_size := mload(returndata)
                    revert(add(32, returndata), returndata_size)
                }
            } else {
                revert(errorMessage);
            }
        }
    }
}

// File: @openzeppelin\contracts\introspection\IERC1820Registry.sol

/**
 * @dev Interface of the global ERC1820 Registry, as defined in the
 * https://eips.ethereum.org/EIPS/eip-1820[EIP]. Accounts may register
 * implementers for interfaces in this registry, as well as query support.
 *
 * Implementers may be shared by multiple accounts, and can also implement more
 * than a single interface for each account. Contracts can implement interfaces
 * for themselves, but externally-owned accounts (EOA) must delegate this to a
 * contract.
 *
 * {IERC165} interfaces can also be queried via the registry.
 *
 * For an in-depth explanation and source code analysis, see the EIP text.
 */
interface IERC1820Registry {
    /**
     * @dev Sets `newManager` as the manager for `account`. A manager of an
     * account is able to set interface implementers for it.
     *
     * By default, each account is its own manager. Passing a value of `0x0` in
     * `newManager` will reset the manager to this initial state.
     *
     * Emits a {ManagerChanged} event.
     *
     * Requirements:
     *
     * - the caller must be the current manager for `account`.
     */
    function setManager(address account, address newManager) external;

    /**
     * @dev Returns the manager for `account`.
     *
     * See {setManager}.
     */
    function getManager(address account) external view returns (address);

    /**
     * @dev Sets the `implementer` contract as ``account``'s implementer for
     * `interfaceHash`.
     *
     * `account` being the zero address is an alias for the caller's address.
     * The zero address can also be used in `implementer` to remove an old one.
     *
     * See {interfaceHash} to learn how these are created.
     *
     * Emits an {InterfaceImplementerSet} event.
     *
     * Requirements:
     *
     * - the caller must be the current manager for `account`.
     * - `interfaceHash` must not be an {IERC165} interface id (i.e. it must not
     * end in 28 zeroes).
     * - `implementer` must implement {IERC1820Implementer} and return true when
     * queried for support, unless `implementer` is the caller. See
     * {IERC1820Implementer-canImplementInterfaceForAddress}.
     */
    function setInterfaceImplementer(
        address account,
        bytes32 interfaceHash,
        address implementer
    ) external;

    /**
     * @dev Returns the implementer of `interfaceHash` for `account`. If no such
     * implementer is registered, returns the zero address.
     *
     * If `interfaceHash` is an {IERC165} interface id (i.e. it ends with 28
     * zeroes), `account` will be queried for support of it.
     *
     * `account` being the zero address is an alias for the caller's address.
     */
    function getInterfaceImplementer(address account, bytes32 interfaceHash)
        external
        view
        returns (address);

    /**
     * @dev Returns the interface hash for an `interfaceName`, as defined in the
     * corresponding
     * https://eips.ethereum.org/EIPS/eip-1820#interface-name[section of the EIP].
     */
    function interfaceHash(string calldata interfaceName) external pure returns (bytes32);

    /**
     *  @notice Updates the cache with whether the contract implements an ERC165 interface or not.
     *  @param account Address of the contract for which to update the cache.
     *  @param interfaceId ERC165 interface for which to update the cache.
     */
    function updateERC165Cache(address account, bytes4 interfaceId) external;

    /**
     *  @notice Checks whether a contract implements an ERC165 interface or not.
     *  If the result is not cached a direct lookup on the contract address is performed.
     *  If the result is not cached or the cached value is out-of-date, the cache MUST be updated manually by calling
     *  {updateERC165Cache} with the contract address.
     *  @param account Address of the contract to check.
     *  @param interfaceId ERC165 interface to check.
     *  @return True if `account` implements `interfaceId`, false otherwise.
     */
    function implementsERC165Interface(address account, bytes4 interfaceId)
        external
        view
        returns (bool);

    /**
     *  @notice Checks whether a contract implements an ERC165 interface or not without using nor updating the cache.
     *  @param account Address of the contract to check.
     *  @param interfaceId ERC165 interface to check.
     *  @return True if `account` implements `interfaceId`, false otherwise.
     */
    function implementsERC165InterfaceNoCache(address account, bytes4 interfaceId)
        external
        view
        returns (bool);

    event InterfaceImplementerSet(
        address indexed account,
        bytes32 indexed interfaceHash,
        address indexed implementer
    );

    event ManagerChanged(address indexed account, address indexed newManager);
}

// File: contracts\libs\SwapLib.sol

library SwapLib {
    using SwapLib for Swap;

    struct Swap {
        address sender;
        uint256[] senderTokenIds;
        uint256[] senderTokenAmounts;
        uint256[] signerTokenIds;
        uint256[] signerTokenAmounts;
    }
}

// File: contracts\interfaces\ITokenRecipient.sol

/// @dev a.
interface ITokenRecipient {
    /// @dev a
    function tokensReceived(
        address operator,
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata amounts,
        bytes calldata data,
        bytes calldata operatorData
    ) external;
}

// File: contracts\interfaces\ITokenSender.sol

/// @dev a.
interface ITokenSender {
    /// @dev a
    function tokensToSend(
        address operator,
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata amounts,
        bytes calldata userData,
        bytes calldata operatorData
    ) external;
}

// File: contracts\Initializable.sol

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

// File: contracts\MixinNF.sol

contract MixinNF {
    /// @dev Use a split bit implementation.
    /// Store the type in the upper 128 bits..
    uint256 internal constant TYPE_MASK = uint256(uint128(~0)) << 128;

    /// @dev ..and the non-fungible index in the lower 128
    uint256 internal constant NF_INDEX_MASK = uint128(~0);

    /// @dev The top bit is a flag to tell if this is a NFI.
    uint256 internal constant TYPE_NF_BIT = 1 << 255;

    /// @dev mapping of nft to owner
    mapping(uint256 => address) internal nfOwners;

    /// @dev Returns true if token is non-fungible
    function isNonFungible(uint256 id) public pure returns (bool) {
        return id & TYPE_NF_BIT == TYPE_NF_BIT;
    }

    /// @dev Returns true if token is fungible
    function isFungible(uint256 id) public pure returns (bool) {
        return id & TYPE_NF_BIT == 0;
    }

    /// @dev Returns index of non-fungible token
    function getNonFungibleIndex(uint256 id) public pure returns (uint256) {
        return id & NF_INDEX_MASK;
    }

    /// @dev Returns base type of non-fungible token
    function getNonFungibleBaseType(uint256 id) public pure returns (uint256) {
        return id & TYPE_MASK;
    }

    /// @dev Returns true if input is base-type of a non-fungible token
    function isNonFungibleBaseType(uint256 id) public pure returns (bool) {
        // A base type has the NF bit but does not have an index.
        return (id & TYPE_NF_BIT == TYPE_NF_BIT) && (id & NF_INDEX_MASK == 0);
    }

    /// @dev Returns true if input is a non-fungible token
    function isNonFungibleItem(uint256 id) public pure returns (bool) {
        // A base type has the NF bit but does has an index.
        return (id & TYPE_NF_BIT == TYPE_NF_BIT) && (id & NF_INDEX_MASK != 0);
    }

    /// @dev returns owner of a non-fungible token
    function ownerOf(uint256 id) public view returns (address) {
        return nfOwners[id];
    }
}

// File: contracts\Token.sol

/// @title Token contract.
/// @notice This contract holds the implementation logic for all token management
/// functionality. This can be called only by the implementation contract.
contract Token is MixinNF, Initializable {
    using Address for address;
    using SafeMath for uint256;
    using SwapLib for SwapLib.Swap;

    IERC1820Registry private erc1820;

    /// @dev Token nonce.
    uint256 internal nonce;

    /// @dev Mapping from token to creator.
    mapping(uint256 => address) public creators;

    /// @dev Mapping from token to max index for non fungible tokens.
    mapping(uint256 => uint256) public maxIndex;

    /// @dev Granularity for fungible tokens.
    uint256 internal gran;

    /// @dev Mapping for balance of tokens and owner.
    mapping(uint256 => mapping(address => uint256)) internal balances;

    bytes32 private TOKEN_SENDER_INTERFACE_HASH = keccak256("ITokenSender");
    bytes32 private TOKEN_RECIPIENT_INTERFACE_HASH = keccak256("ITokenRecipient");

    /// EVENT

    /// @dev `create` MUST emit when a token is created.
    /// Creator will always be msg.sender.
    event TokenCreated(address indexed creator, uint256 indexed id, bytes data);

    /// @dev emits IF uri is not empty on token creation.
    event TokenURI(string value, uint256 indexed id);

    /// @dev `send/sendOperator` MUST emit when tokens are transferred.
    /// Operator will always be msg.sender.
    event TokenSent(
        address operator,
        address indexed from,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );

    /// @dev `mintFungible/mintNonFungible` MUST emit when tokens are minted.
    /// Operator will always be msg.sender.
    event TokenMinted(
        address operator,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data
    );

    /// @dev `burn/burnOperator` MUST emit when tokens are burned.
    /// Operator will always be msg.sender.
    event TokenBurned(
        address operator,
        address indexed from,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );

    /// @notice Constructor sets the granularity for fungible tokens.
    /// @param _granularity     Granularity of fungible tokens.
    /// @param _1820Registry    ERC1820 Registry contract address.
    constructor(uint256 _granularity, address _1820Registry) public {
        gran = _granularity;
        erc1820 = IERC1820Registry(_1820Registry);
    }

    /// @notice Creates a new token.
    /// @param _sender  Address of the sender (msg.sender).
    /// @param _uri     URI of the token.
    /// @param _isNF    is non-fungible token.
    /// @param _data    Additional data with no specified format.
    /// @return type_ Token type (a unique identifier).
    /// @dev Only the owner should call this.
    function create(
        address _sender,
        string calldata _uri,
        bool _isNF,
        bytes calldata _data
    ) external onlyImplementation returns (uint256 type_) {
        // Store the type in the upper 128 bits
        type_ = (++nonce << 128);

        if (_isNF) {
            type_ = type_ | TYPE_NF_BIT;
        }
        creators[type_] = _sender;

        emit TokenCreated(_sender, type_, _data);

        if (bytes(_uri).length > 0) {
            emit TokenURI(_uri, type_);
        }
    }

    /// @notice Mints fungible tokens.
    /// @param _sender  Address of the sender (msg.sender).
    /// @param _to      Beneficiaries of minted tokens.
    /// @param _id      Token type.
    /// @param _amounts Amounts of minted tokens.
    /// @param _data    Additional data with no specified format.
    /// @dev Only the owner should call this.
    function mintFungible(
        address _sender,
        address[] calldata _to,
        uint256 _id,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyImplementation {
        require(_isCreator(_sender, _id), "NOT_CREATOR");
        require(isFungible(_id), "NON_FUNGIBLE_TOKEN");

        for (uint256 i = 0; i < _to.length; ++i) {
            address to = _to[i];
            require(to != address(0), "INVALID_ADDRESS");
            uint256 amount = _amounts[i];
            require(_checkGranularity(amount), "INVALID_GRANULARITY");
            balances[_id][to] = amount.add(balances[_id][to]);

            emit TokenMinted(_sender, to, _id, amount, _data);
        }
    }

    /// @notice Mints a non-fungible token.
    /// @param _sender  Address of the sender (msg.sender).
    /// @param _to      Beneficiaries of minted tokens.
    /// @param _type    Token type.
    /// @param _data    Additional data with no specified format.
    /// @dev Only the owner should call this.
    function mintNonFungible(
        address _sender,
        address[] calldata _to,
        uint256 _type,
        bytes calldata _data
    ) external onlyImplementation {
        require(_isCreator(_sender, _type), "NOT_CREATOR");
        require(isNonFungible(_type), "FUNGIBLE_TOKEN");

        // Index are 1-based.
        uint256 index = maxIndex[_type] + 1;

        for (uint256 i = 0; i < _to.length; ++i) {
            address to = _to[i];
            require(to != address(0), "INVALID_ADDRESS");
            uint256 id = _type | (index + i);
            nfOwners[id] = to;
            // NFT type balance.
            balances[_type][to] = 1;

            emit TokenMinted(_sender, to, id, 1, _data);
        }

        // record the `maxIndex` of this nft type.
        maxIndex[_type] = _to.length.add(maxIndex[_type]);
    }

    function send(
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyImplementation {
        _send(_from, _from, _to, _ids, _amounts, _data, "");
    }

    function operatorSend(
        address _operator,
        address _from,
        address _to,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external onlyImplementation {
        _send(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    function burn(
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data
    ) external onlyImplementation {
        _burn(_from, _from, _ids, _amounts, _data, "");
    }

    function operatorBurn(
        address _operator,
        address _from,
        uint256[] calldata _ids,
        uint256[] calldata _amounts,
        bytes calldata _data,
        bytes calldata _operatorData
    ) external onlyImplementation {
        _burn(_operator, _from, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Get the balance of an account's Tokens.
    /// @param _owner  The address of the token holder.
    /// @param _id     ID of the Token.
    /// @return The _owner's balance of the Token type requested.
    function balanceOf(address _owner, uint256 _id) external view returns (uint256) {
        if (isNonFungibleItem(_id)) {
            return nfOwners[_id] == _owner ? 1 : 0;
        }
        return balances[_id][_owner];
    }

    /// @notice Get the balance of multiple account/token pairs.
    /// @param _owners The addresses of the token holders.
    /// @param _ids    ID of the Tokens.
    /// @return balances_   The _owner's balance of the Token types requested.
    function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids)
        external
        view
        returns (uint256[] memory balances_)
    {
        require(_owners.length == _ids.length, "LENGTH_MISMATCH");

        balances_ = new uint256[](_owners.length);
        for (uint256 i = 0; i < _owners.length; ++i) {
            uint256 id = _ids[i];
            if (isNonFungibleItem(id)) {
                balances_[i] = nfOwners[id] == _owners[i] ? 1 : 0;
            } else {
                balances_[i] = balances[id][_owners[i]];
            }
        }
        return balances_;
    }

    /// @notice Get the granularity of fungible tokens.
    function granularity() external view returns (uint256) {
        return gran;
    }

    /// @notice Swaps tokens.
    /// @param _sender  Address of the sender (msg.sender).
    /// @param _signer  Address of the signer.
    /// @param _swap    Swap data.
    /// @param _data    Additional data with no specified format.
    function swap(
        address _sender,
        address _signer,
        SwapLib.Swap memory _swap,
        bytes memory _data
    ) public onlyImplementation {
        _send(
            _sender,
            _sender,
            _signer,
            _swap.senderTokenIds,
            _swap.senderTokenAmounts,
            _data,
            ""
        );
        _send(
            _signer,
            _signer,
            _sender,
            _swap.signerTokenIds,
            _swap.signerTokenAmounts,
            _data,
            ""
        );
    }

    /// @notice Sends multiple types of tokens.
    /// @param _operator    msg.sender.
    /// @param _from        Sender addresses.
    /// @param _to          Recipient addresses.
    /// @param _ids         Ids of each token type.
    /// @param _amounts     Transfer amounts per token type.
    /// @param _data        Additional data with no specified format.
    /// @param _operatorData Additional data with no specified format.
    function _send(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        require(_to != address(0x0), "INVALID_ADDRESS");
        require(_ids.length == _amounts.length, "LENGTH_MISMATCH");

        callSender(_operator, _from, _to, _ids, _amounts, _data, _operatorData);

        for (uint256 i = 0; i < _ids.length; ++i) {
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];

            if (isNonFungible(id)) {
                require(amount == 1, "INVALID_AMOUNT");
                require(nfOwners[id] == _from, "NOT_OWNER");
                nfOwners[id] = _to;
                // Keep the balance of NF type in base type id
                uint256 baseType = getNonFungibleBaseType(id);
                balances[baseType][_from] = balances[baseType][_from].sub(1);
                balances[baseType][_to] = balances[baseType][_to].add(1);
            } else {
                require(_checkGranularity(amount), "INVALID_GRANULARITY");
                balances[id][_from] = balances[id][_from].sub(amount);
                balances[id][_to] = balances[id][_to].add(amount);
            }
            emit TokenSent(_operator, _from, _to, id, amount, _data, _operatorData);
        }

        callReceiver(_operator, _from, _to, _ids, _amounts, _data, _operatorData);
    }

    /// @notice Burns token.
    /// @param _operator    msg.sender.
    /// @param _from        Source address.
    /// @param _ids         IDs of the token type.
    /// @param _amounts     Burn amounts per type.
    /// @param _data        Additional data with no specified format.
    /// @param _operatorData Additional data with no specified format.
    function _burn(
        address _operator,
        address _from,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) internal {
        require(_from != address(0), "INVALID_ADDRESS");

        callSender(_operator, _from, address(0), _ids, _amounts, _data, _operatorData);

        for (uint256 i = 0; i < _ids.length; ++i) {
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];
            if (isNonFungible(id)) {
                require(amount == 1, "INVALID_AMOUNT");
                require(nfOwners[id] == _from, "NOT_OWNER");
                nfOwners[id] == address(0);
                uint256 baseType = getNonFungibleBaseType(id);
                balances[baseType][_from] = balances[baseType][_from].sub(1);
            } else {
                require(_checkGranularity(amount), "INVALID_GRANULARITY");
                balances[id][_from] = balances[id][_from].sub(amount);
            }
            emit TokenBurned(_operator, _from, id, amount, _data, _operatorData);
        }
    }

    /// @notice Calls/Verifies the sender.
    /// @param _operator    msg.sender.
    /// @param _from        Sender address.
    /// @param _to          Recepient address.
    /// @param _ids         IDs of the token type.
    /// @param _amounts     Burn amounts.
    /// @param _data        Additional data with no specified format.
    /// @param _operatorData Additional data with no specified format.
    /// @dev EIP1820
    function callSender(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) private {
        address impl = erc1820.getInterfaceImplementer(_from, TOKEN_SENDER_INTERFACE_HASH);
        if (impl != address(0)) {
            ITokenSender(impl).tokensToSend(
                _operator,
                _from,
                _to,
                _ids,
                _amounts,
                _data,
                _operatorData
            );
        }
    }

    /// @notice Calls/Verifies the recipient.
    /// @param _operator    msg.sender
    /// @param _from        Sender address
    /// @param _to          Recepient address
    /// @param _ids         IDs of the token type
    /// @param _amounts     Burn amounts
    /// @param _data        Additional data with no specified format
    /// @param _operatorData Additional data with no specified format
    /// @dev EIP1820
    function callReceiver(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) private {
        address impl = erc1820.getInterfaceImplementer(_to, TOKEN_RECIPIENT_INTERFACE_HASH);
        if (impl != address(0)) {
            ITokenRecipient(impl).tokensReceived(
                _operator,
                _from,
                _to,
                _ids,
                _amounts,
                _data,
                _operatorData
            );
        } else {
            require(!_to.isContract(), "INTERFACE_NOT_IMPLEMENTED");
        }
    }

    /// @notice Checks if _creator is the creator of token of type _id.
    function _isCreator(address _creator, uint256 _id) internal view returns (bool) {
        return (creators[_id] == _creator);
    }

    /// @notice Checks if an amount is a mulitple of the granularity for fungible tokens.
    function _checkGranularity(uint256 _amount) internal view returns (bool) {
        return (_amount % gran == 0);
    }
}
