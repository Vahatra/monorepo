"""Generated wrapper for Account Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # noqa
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for Account below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        AccountValidator,
    )
except ImportError:

    class AccountValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class AccountAcc(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    acc: str

    pAcc: str

    uAcc: str

    name: str

    level: int

    subAccs: List[str]

    status: int


class InitializeMethod(ContractMethod):
    """Various interfaces to the initialize method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, implementation: str):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_implementation",
            argument_value=implementation,
        )
        implementation = self.validate_and_checksum_address(implementation)
        return implementation

    def call(self, implementation: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(implementation).call(tx_params.as_dict())

    def send_transaction(
        self, implementation: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation).transact(tx_params.as_dict())

    def build_transaction(
        self, implementation: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, implementation: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation).estimateGas(tx_params.as_dict())


class AddAccountMethod(ContractMethod):
    """Various interfaces to the addAccount method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, acc: str, p_acc: str, name: str):
        """Validate the inputs to the addAccount method."""
        self.validator.assert_valid(
            method_name="addAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        self.validator.assert_valid(
            method_name="addAccount", parameter_name="_pAcc", argument_value=p_acc,
        )
        p_acc = self.validate_and_checksum_address(p_acc)
        self.validator.assert_valid(
            method_name="addAccount", parameter_name="_name", argument_value=name,
        )
        return (acc, p_acc, name)

    def call(
        self, acc: str, p_acc: str, name: str, tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc, p_acc, name) = self.validate_and_normalize_inputs(acc, p_acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc, p_acc, name).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, p_acc: str, name: str, tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc, p_acc, name) = self.validate_and_normalize_inputs(acc, p_acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, p_acc, name).transact(tx_params.as_dict())

    def build_transaction(
        self, acc: str, p_acc: str, name: str, tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc, p_acc, name) = self.validate_and_normalize_inputs(acc, p_acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, p_acc, name).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, acc: str, p_acc: str, name: str, tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (acc, p_acc, name) = self.validate_and_normalize_inputs(acc, p_acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, p_acc, name).estimateGas(
            tx_params.as_dict()
        )


class UpdateAccountStatusMethod(ContractMethod):
    """Various interfaces to the updateAccountStatus method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, acc: str, action: int):
        """Validate the inputs to the updateAccountStatus method."""
        self.validator.assert_valid(
            method_name="updateAccountStatus",
            parameter_name="_acc",
            argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        self.validator.assert_valid(
            method_name="updateAccountStatus",
            parameter_name="_action",
            argument_value=action,
        )
        # safeguard against fractional inputs
        action = int(action)
        return (acc, action)

    def call(self, acc: str, action: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc, action) = self.validate_and_normalize_inputs(acc, action)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc, action).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, action: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc, action) = self.validate_and_normalize_inputs(acc, action)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, action).transact(tx_params.as_dict())

    def build_transaction(
        self, acc: str, action: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc, action) = self.validate_and_normalize_inputs(acc, action)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, action).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, acc: str, action: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (acc, action) = self.validate_and_normalize_inputs(acc, action)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, action).estimateGas(tx_params.as_dict())


class AuthorizeOperatorMethod(ContractMethod):
    """Various interfaces to the authorizeOperator method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, sender: str, operator: str):
        """Validate the inputs to the authorizeOperator method."""
        self.validator.assert_valid(
            method_name="authorizeOperator",
            parameter_name="_sender",
            argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
        self.validator.assert_valid(
            method_name="authorizeOperator",
            parameter_name="_operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (sender, operator)

    def call(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sender, operator).call(tx_params.as_dict())

    def send_transaction(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, operator).transact(tx_params.as_dict())

    def build_transaction(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, operator).estimateGas(
            tx_params.as_dict()
        )


class RevokeOperatorMethod(ContractMethod):
    """Various interfaces to the revokeOperator method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, sender: str, operator: str):
        """Validate the inputs to the revokeOperator method."""
        self.validator.assert_valid(
            method_name="revokeOperator",
            parameter_name="_sender",
            argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
        self.validator.assert_valid(
            method_name="revokeOperator",
            parameter_name="_operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (sender, operator)

    def call(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sender, operator).call(tx_params.as_dict())

    def send_transaction(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, operator).transact(tx_params.as_dict())

    def build_transaction(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, sender: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (sender, operator) = self.validate_and_normalize_inputs(sender, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, operator).estimateGas(
            tx_params.as_dict()
        )


class GetAccountMethod(ContractMethod):
    """Various interfaces to the getAccount method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, acc: str):
        """Validate the inputs to the getAccount method."""
        self.validator.assert_valid(
            method_name="getAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> AccountAcc:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(acc).call(tx_params.as_dict())
        return AccountAcc(
            acc=returned[0],
            pAcc=returned[1],
            uAcc=returned[2],
            name=returned[3],
            level=returned[4],
            subAccs=returned[5],
            status=returned[6],
        )

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


class GetParentAccountMethod(ContractMethod):
    """Various interfaces to the getParentAccount method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, acc: str):
        """Validate the inputs to the getParentAccount method."""
        self.validator.assert_valid(
            method_name="getParentAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(acc).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


class IsOperatorForMethod(ContractMethod):
    """Various interfaces to the isOperatorFor method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str, acc: str):
        """Validate the inputs to the isOperatorFor method."""
        self.validator.assert_valid(
            method_name="isOperatorFor",
            parameter_name="_operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="isOperatorFor", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return (operator, acc)

    def call(
        self, operator: str, acc: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (operator, acc) = self.validate_and_normalize_inputs(operator, acc)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(operator, acc).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, operator: str, acc: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator, acc) = self.validate_and_normalize_inputs(operator, acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, acc).estimateGas(tx_params.as_dict())


class IsActiveMethod(ContractMethod):
    """Various interfaces to the isActive method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, acc: str):
        """Validate the inputs to the isActive method."""
        self.validator.assert_valid(
            method_name="isActive", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(acc).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Account:
    """Wrapper class for Account Solidity contract."""

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    add_account: AddAccountMethod
    """Constructor-initialized instance of
    :class:`AddAccountMethod`.
    """

    update_account_status: UpdateAccountStatusMethod
    """Constructor-initialized instance of
    :class:`UpdateAccountStatusMethod`.
    """

    authorize_operator: AuthorizeOperatorMethod
    """Constructor-initialized instance of
    :class:`AuthorizeOperatorMethod`.
    """

    revoke_operator: RevokeOperatorMethod
    """Constructor-initialized instance of
    :class:`RevokeOperatorMethod`.
    """

    get_account: GetAccountMethod
    """Constructor-initialized instance of
    :class:`GetAccountMethod`.
    """

    get_parent_account: GetParentAccountMethod
    """Constructor-initialized instance of
    :class:`GetParentAccountMethod`.
    """

    is_operator_for: IsOperatorForMethod
    """Constructor-initialized instance of
    :class:`IsOperatorForMethod`.
    """

    is_active: IsActiveMethod
    """Constructor-initialized instance of
    :class:`IsActiveMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: AccountValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = AccountValidator(web3_or_provider, contract_address)

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"], layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address), abi=Account.abi()
        ).functions

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize, validator
        )

        self.add_account = AddAccountMethod(
            web3_or_provider, contract_address, functions.addAccount, validator
        )

        self.update_account_status = UpdateAccountStatusMethod(
            web3_or_provider,
            contract_address,
            functions.updateAccountStatus,
            validator,
        )

        self.authorize_operator = AuthorizeOperatorMethod(
            web3_or_provider, contract_address, functions.authorizeOperator, validator,
        )

        self.revoke_operator = RevokeOperatorMethod(
            web3_or_provider, contract_address, functions.revokeOperator, validator,
        )

        self.get_account = GetAccountMethod(
            web3_or_provider, contract_address, functions.getAccount, validator
        )

        self.get_parent_account = GetParentAccountMethod(
            web3_or_provider, contract_address, functions.getParentAccount, validator,
        )

        self.is_operator_for = IsOperatorForMethod(
            web3_or_provider, contract_address, functions.isOperatorFor, validator,
        )

        self.is_active = IsActiveMethod(
            web3_or_provider, contract_address, functions.isActive, validator
        )

    def get_account_created_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AccountCreated event.

        :param tx_hash: hash of transaction emitting AccountCreated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Account.abi(),
            )
            .events.AccountCreated()
            .processReceipt(tx_receipt)
        )

    def get_account_status_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AccountStatusUpdated event.

        :param tx_hash: hash of transaction emitting AccountStatusUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Account.abi(),
            )
            .events.AccountStatusUpdated()
            .processReceipt(tx_receipt)
        )

    def get_authorized_operator_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuthorizedOperator event.

        :param tx_hash: hash of transaction emitting AuthorizedOperator event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Account.abi(),
            )
            .events.AuthorizedOperator()
            .processReceipt(tx_receipt)
        )

    def get_revoked_operator_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RevokedOperator event.

        :param tx_hash: hash of transaction emitting RevokedOperator event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Account.abi(),
            )
            .events.RevokedOperator()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"uint256","name":"_breadth","type":"uint256"},{"internalType":"uint256","name":"_depth","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_acc","type":"address"},{"indexed":false,"internalType":"address","name":"_pAcc","type":"address"},{"indexed":false,"internalType":"address","name":"_uAcc","type":"address"},{"indexed":false,"internalType":"string","name":"_name","type":"string"},{"indexed":false,"internalType":"uint256","name":"level","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_status","type":"uint256"}],"name":"AccountCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_acc","type":"address"},{"indexed":false,"internalType":"uint256","name":"_status","type":"uint256"}],"name":"AccountStatusUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"holder","type":"address"}],"name":"AuthorizedOperator","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"holder","type":"address"}],"name":"RevokedOperator","type":"event"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"},{"internalType":"address","name":"_pAcc","type":"address"},{"internalType":"string","name":"_name","type":"string"}],"name":"addAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"},{"internalType":"uint256","name":"_action","type":"uint256"}],"name":"updateAccountStatus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"address","name":"_operator","type":"address"}],"name":"authorizeOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"address","name":"_operator","type":"address"}],"name":"revokeOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"getAccount","outputs":[{"components":[{"internalType":"address","name":"acc","type":"address"},{"internalType":"address","name":"pAcc","type":"address"},{"internalType":"address","name":"uAcc","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"address[]","name":"subAccs","type":"address[]"},{"internalType":"uint256","name":"status","type":"uint256"}],"internalType":"struct Account.Acc","name":"","type":"tuple"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"getParentAccount","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"address","name":"_acc","type":"address"}],"name":"isOperatorFor","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"isActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function","constant":true}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
