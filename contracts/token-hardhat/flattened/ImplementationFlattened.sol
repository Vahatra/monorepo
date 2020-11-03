// File: ..\..\node_modules\@openzeppelin\contracts\GSN\Context.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

/*
 * @dev Provides information about the current execution context, including the
 * sender of the transaction and its data. While these are generally available
 * via msg.sender and msg.data, they should not be accessed in such a direct
 * manner, since when dealing with GSN meta-transactions the account sending and
 * paying for execution may not be the actual sender (as far as an application
 * is concerned).
 *
 * This contract is only required for intermediate, library-like contracts.
 */
abstract contract Context {
    function _msgSender() internal virtual view returns (address payable) {
        return msg.sender;
    }

    function _msgData() internal virtual view returns (bytes memory) {
        this; // silence state mutability warning without generating bytecode - see https://github.com/ethereum/solidity/issues/2691
        return msg.data;
    }
}

// File: @openzeppelin\contracts\access\Ownable.sol

/**
 * @dev Contract module which provides a basic access control mechanism, where
 * there is an account (an owner) that can be granted exclusive access to
 * specific functions.
 *
 * By default, the owner account will be the one that deploys the contract. This
 * can later be changed with {transferOwnership}.
 *
 * This module is used through inheritance. It will make available the modifier
 * `onlyOwner`, which can be applied to your functions to restrict their use to
 * the owner.
 */
contract Ownable is Context {
    address private _owner;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Initializes the contract setting the deployer as the initial owner.
     */
    constructor() internal {
        address msgSender = _msgSender();
        _owner = msgSender;
        emit OwnershipTransferred(address(0), msgSender);
    }

    /**
     * @dev Returns the address of the current owner.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner() {
        require(_owner == _msgSender(), "Ownable: caller is not the owner");
        _;
    }

    /**
     * @dev Leaves the contract without owner. It will not be possible to call
     * `onlyOwner` functions anymore. Can only be called by the current owner.
     *
     * NOTE: Renouncing ownership will leave the contract without an owner,
     * thereby removing any functionality that is only available to the owner.
     */
    function renounceOwnership() public virtual onlyOwner {
        emit OwnershipTransferred(_owner, address(0));
        _owner = address(0);
    }

    /**
     * @dev Transfers ownership of the contract to a new account (`newOwner`).
     * Can only be called by the current owner.
     */
    function transferOwnership(address newOwner) public virtual onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }
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

// File: contracts\SwapVerifier.sol

/// @title Contract for verifying the signature of a token swap transaction.
contract SwapVerifier {
    using SwapLib for SwapLib.Swap;

    /// @dev Mapping of nonces to avoid replays.
    mapping(address => uint256) public signerNonces;

    /// @dev EIP712
    string public constant name = "Vahatra";
    bytes32 public constant SWAP_TYPEHASH = keccak256(
        "Swap(address sender,uint256[] senderTokenIds,uint256[] senderTokenAmounts,uint256[] signerTokenIds,uint256[] signerTokenAmounts)"
    );
    bytes32 public constant EIP712_DOMAIN_TYPEHASH = keccak256(
        "EIP712Domain(string name,uint256 chainId,address verifyingContract)"
    );
    bytes32 public DOMAIN_SEPARATOR = keccak256(
        abi.encode(EIP712_DOMAIN_TYPEHASH, keccak256(bytes(name)), getChainId(), address(this))
    );

    /// @notice Verifies the signature and returns the signer.
    /// @param _swap    Swap data
    /// @param _nonce   Contract state required to match the signature
    /// @param _expiry  Time at which to expire the signature
    /// @param _v       Recovery byte of the signature
    /// @param _r       Half of the ECDSA signature pair
    /// @param _s       Half of the ECDSA signature pair
    function swapVerify(
        SwapLib.Swap memory _swap,
        uint256 _nonce,
        uint256 _expiry,
        uint8 _v,
        bytes32 _r,
        bytes32 _s
    ) public returns (address signer_) {
        signer_ = ecrecover(hashSwap(_swap), _v, _r, _s);
        require(signer_ != address(0), "INVALID_SIGNER");
        require(_nonce == signerNonces[signer_]++, "INVALID_NONCE");
        require(now <= _expiry, "SIGNATURE_EXPIRED");
    }

    function getChainId() internal pure returns (uint256) {
        uint256 chainId;
        assembly {
            chainId := chainid()
        }
        return chainId;
    }

    function hashSwap(SwapLib.Swap memory _swap) private view returns (bytes32) {
        return
            keccak256(
                abi.encodePacked(
                    "\\x19\\x01",
                    DOMAIN_SEPARATOR,
                    keccak256(
                        abi.encode(
                            SWAP_TYPEHASH,
                            _swap.sender,
                            _swap.senderTokenIds,
                            _swap.senderTokenAmounts,
                            _swap.signerTokenIds,
                            _swap.signerTokenAmounts
                        )
                    )
                )
            );
    }
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
            require(status == 1, "ACCOUNT_NOT_ACTIVE");
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
        require(isActive(_sender), "ACCOUNT_NOT_ACTIVE");
        require(_sender != _operator, "INVALID_OPERATOR");

        operators[_sender][_operator] = true;
        emit AuthorizedOperator(_operator, _sender);
    }

    /// @notice Remove the right of the operator address to be an operator for
    /// _sender (msg.sender) and to send and burn tokens on its behalf.
    /// @param _sender      Address of the sender (msg.sender).
    /// @param _operator    Address to add to the set of authorized operators.
    function revokeOperator(address _sender, address _operator) external onlyImplementation {
        require(isActive(_sender), "ACCOUNT_NOT_ACTIVE");
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

// File: @openzeppelin\contracts\math\SafeMath.sol

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
        require(_to.length == _amounts.length, "LENGTH_MISMATCH");

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
        send(_sender, _sender, _signer, _swap.senderTokenIds, _swap.senderTokenAmounts, _data, "");
        send(_signer, _signer, _sender, _swap.signerTokenIds, _swap.signerTokenAmounts, _data, "");
    }

    /// @notice Sends multiple types of tokens.
    /// @param _operator    msg.sender.
    /// @param _from        Sender addresses.
    /// @param _to          Recipient addresses.
    /// @param _ids         Ids of each token type.
    /// @param _amounts     Transfer amounts per token type.
    /// @param _data        Additional data with no specified format.
    /// @param _operatorData Additional data with no specified format.
    function send(
        address _operator,
        address _from,
        address _to,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) public onlyImplementation {
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
    function burn(
        address _operator,
        address _from,
        uint256[] memory _ids,
        uint256[] memory _amounts,
        bytes memory _data,
        bytes memory _operatorData
    ) public onlyImplementation {
        require(_from != address(0), "INVALID_ADDRESS");

        callSender(_operator, _from, address(0), _ids, _amounts, _data, _operatorData);
        for (uint256 i = 0; i < _ids.length; ++i) {
            uint256 id = _ids[i];
            uint256 amount = _amounts[i];
            if (isNonFungible(id)) {
                require(amount == 1, "INVALID_AMOUNT");
                require(nfOwners[id] == _from, "NOT_OWNER");
                nfOwners[id] == address(0);
                // Keep the balance of NF type in base type id
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

    /// @notice Checks if _amount is a mulitple of the granularity for fungible tokens.
    function _checkGranularity(uint256 _amount) internal view returns (bool) {
        return (_amount % gran == 0);
    }
}

// File: contracts\Implementation.sol

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
        require(_isActive(_acc), "ACCOUNT_NOT_ACTIVE");
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
        require(_isActive(signer), "ACCOUNT_NOT_ACTIVE");
        token.swap(msg.sender, signer, _swap, _data);
    }
}
