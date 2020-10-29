// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

/// @dev Interface of the Token.
interface IToken {
    // // /// @dev Returns the name of the token.
    // // function name() external view returns (string memory);

    // // /// @dev Returns the symbol of the token, usually a shorter version of the
    // // /// name.
    // // function symbol() external view returns (string memory);

    // // /// @dev Returns the smallest part of the token that is not divisible. This
    // // /// means all token operations (creation, movement and destruction) must have
    // // /// amounts that are a multiple of this number.
    // // /// For most token contracts, this value will equal 1.
    // // function granularity() external view returns (uint256);

    // // /// @dev Returns the amount of tokens in existence.
    // // function totalSupply() external view returns (uint256);

    // /// @dev Returns the amount of tokens owned by an account (`owner`).
    // function balanceOf(address _owner) external view returns (uint256);

    // function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids)
    //     external
    //     view
    //     returns (uint256[] memory balances_);

    // function create(bool _isNF) external returns (uint256 type_);

    // function mintFungible(
    //     uint256 _id,
    //     address[] calldata _to,
    //     uint256[] calldata _amounts,
    //     bytes calldata _data,
    //     bytes calldata _operatorData
    // ) external;

    // function mintNonFungible(
    //     uint256 _type,
    //     address[] calldata _to,
    //     bytes calldata _data,
    //     bytes calldata _operatorData
    // ) external;

    // /// @dev Moves `amount` tokens from the caller's account to `recipient`.
    // /// If send or receive hooks are registered for the caller and `recipient`,
    // /// the corresponding functions will be called with `data` and empty
    // /// `operatorData`. See {IERC777Sender} and {IERC777Recipient}.
    // /// Emits a {Sent} event.
    // /// Requirements
    // /// - the caller must have at least `amount` tokens.
    // /// - `recipient` cannot be the zero address.
    // /// - if `recipient` is a contract, it must implement the {IERC777Recipient}
    // /// interface.
    // function send(
    //     address _to,
    //     uint256[] calldata _ids,
    //     uint256[] calldata _amounts,
    //     bytes calldata _data
    // ) external;

    // /// @dev Destroys `amount` tokens from the caller's account, reducing the
    // /// total supply.
    // /// If a send hook is registered for the caller, the corresponding function
    // /// will be called with `data` and empty `operatorData`. See {IERC777Sender}.
    // /// Emits a {Burned} event.
    // /// Requirements
    // /// - the caller must have at least `amount` tokens.
    // function burn(
    //     uint256[] calldata _ids,
    //     uint256[] calldata _amounts,
    //     bytes calldata _data
    // ) external;

    // /// @dev Returns true if an account is an operator of `tokenHolder`.
    // /// Operators can send and burn tokens on behalf of their owners. All
    // /// accounts are their own operator.
    // /// See {operatorSend} and {operatorBurn}.
    // function isOperatorFor(address _operator, address _holder) external view returns (bool);

    // /// @dev Make an account an operator of the caller.
    // /// See {isOperatorFor}.
    // /// Emits an {AuthorizedOperator} event.
    // /// Requirements
    // /// - `operator` cannot be calling address.
    // function authorizeOperator(address _operator) external;

    // /// @dev Revoke an account's operator status for the caller.
    // /// See {isOperatorFor} and {defaultOperators}.
    // /// Emits a {RevokedOperator} event.
    // /// Requirements
    // /// - `operator` cannot be calling address.
    // function revokeOperator(address _operator) external;

    // // /// @dev Returns the list of default operators. These accounts are operators
    // // /// for all token holders, even if {authorizeOperator} was never called on
    // // /// them.
    // // /// This list is immutable, but individual holders may revoke these via
    // // /// {revokeOperator}, in which case {isOperatorFor} will return false.
    // // function defaultOperators() external view returns (address[] memory);

    // /// @dev Moves `amount` tokens from `sender` to `recipient`. The caller must
    // /// be an operator of `sender`.
    // /// If send or receive hooks are registered for `sender` and `recipient`,
    // /// the corresponding functions will be called with `data` and
    // /// `operatorData`. See {IERC777Sender} and {IERC777Recipient}.
    // /// Emits a {Sent} event.
    // /// Requirements
    // /// - `sender` cannot be the zero address.
    // /// - `sender` must have at least `amount` tokens.
    // /// - the caller must be an operator for `sender`.
    // /// - `recipient` cannot be the zero address.
    // /// - if `recipient` is a contract, it must implement the {IERC777Recipient}
    // /// interface.
    // function operatorSend(
    //     address _from,
    //     address _to,
    //     uint256[] calldata _ids,
    //     uint256[] calldata _amounts,
    //     bytes calldata _data,
    //     bytes calldata _operatorData
    // ) external;

    // /// @dev Destroys `amount` tokens from `account`, reducing the total supply.
    // /// The caller must be an operator of `account`.
    // /// If a send hook is registered for `account`, the corresponding function
    // /// will be called with `data` and `operatorData`. See {IERC777Sender}.
    // /// Emits a {Burned} event.
    // /// Requirements
    // /// - `account` cannot be the zero address.
    // /// - `account` must have at least `amount` tokens.
    // /// - the caller must be an operator for `account`.
    // function operatorBurn(
    //     address _from,
    //     uint256[] calldata _ids,
    //     uint256[] calldata _amounts,
    //     bytes calldata _data,
    //     bytes calldata _operatorData
    // ) external;

    event Sent(
        address indexed operator,
        address indexed from,
        address indexed to,
        uint256 amount,
        bytes data,
        bytes operatorData
    );

    event Sent(
        address operator,
        address indexed from,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );
    event Minted(
        address operator,
        address indexed to,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );
    event Burned(
        address operator,
        address indexed from,
        uint256 indexed id,
        uint256 amount,
        bytes data,
        bytes operatorData
    );
    event AuthorizedOperator(address indexed operator, address indexed holder);
    event RevokedOperator(address indexed operator, address indexed holder);
}
