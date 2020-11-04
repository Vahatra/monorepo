"""Generated wrapper for Implementation Solidity contract."""

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
# constructor for Implementation below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ImplementationValidator,
    )
except ImportError:

    class ImplementationValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class SwapLibSwap(TypedDict):
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

    sender: str

    senderTokenIds: List[int]

    senderTokenAmounts: List[int]

    signerTokenIds: List[int]

    signerTokenAmounts: List[int]


class DomainSeparatorMethod(ContractMethod):
    """Various interfaces to the DOMAIN_SEPARATOR method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class Eip712DomainTypehashMethod(ContractMethod):
    """Various interfaces to the EIP712_DOMAIN_TYPEHASH method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class SwapTypehashMethod(ContractMethod):
    """Various interfaces to the SWAP_TYPEHASH method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class NameMethod(ContractMethod):
    """Various interfaces to the name method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class OwnerMethod(ContractMethod):
    """Various interfaces to the owner method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class RenounceOwnershipMethod(ContractMethod):
    """Various interfaces to the renounceOwnership method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class SignerNoncesMethod(ContractMethod):
    """Various interfaces to the signerNonces method."""

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

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the signerNonces method."""
        self.validator.assert_valid(
            method_name="signerNonces",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())


class TransferOwnershipMethod(ContractMethod):
    """Various interfaces to the transferOwnership method."""

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

    def validate_and_normalize_inputs(self, new_owner: str):
        """Validate the inputs to the transferOwnership method."""
        self.validator.assert_valid(
            method_name="transferOwnership",
            parameter_name="newOwner",
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return new_owner

    def call(self, new_owner: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_owner).call(tx_params.as_dict())

    def send_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, new_owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(tx_params.as_dict())


class RegisterMethod(ContractMethod):
    """Various interfaces to the register method."""

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

    def validate_and_normalize_inputs(self, name: str):
        """Validate the inputs to the register method."""
        self.validator.assert_valid(
            method_name="register", parameter_name="_name", argument_value=name,
        )
        return name

    def call(self, name: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (name) = self.validate_and_normalize_inputs(name)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(name).call(tx_params.as_dict())

    def send_transaction(
        self, name: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (name) = self.validate_and_normalize_inputs(name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(name).transact(tx_params.as_dict())

    def build_transaction(
        self, name: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (name) = self.validate_and_normalize_inputs(name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(name).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, name: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (name) = self.validate_and_normalize_inputs(name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(name).estimateGas(tx_params.as_dict())


class AddSubAccountMethod(ContractMethod):
    """Various interfaces to the addSubAccount method."""

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

    def validate_and_normalize_inputs(self, acc: str, name: str):
        """Validate the inputs to the addSubAccount method."""
        self.validator.assert_valid(
            method_name="addSubAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        self.validator.assert_valid(
            method_name="addSubAccount", parameter_name="_name", argument_value=name,
        )
        return (acc, name)

    def call(self, acc: str, name: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc, name) = self.validate_and_normalize_inputs(acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc, name).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, name: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc, name) = self.validate_and_normalize_inputs(acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, name).transact(tx_params.as_dict())

    def build_transaction(
        self, acc: str, name: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc, name) = self.validate_and_normalize_inputs(acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, name).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self, acc: str, name: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (acc, name) = self.validate_and_normalize_inputs(acc, name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc, name).estimateGas(tx_params.as_dict())


class SuspendAccountMethod(ContractMethod):
    """Various interfaces to the suspendAccount method."""

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
        """Validate the inputs to the suspendAccount method."""
        self.validator.assert_valid(
            method_name="suspendAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).transact(tx_params.as_dict())

    def build_transaction(self, acc: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


class ReactivateAccountMethod(ContractMethod):
    """Various interfaces to the reactivateAccount method."""

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
        """Validate the inputs to the reactivateAccount method."""
        self.validator.assert_valid(
            method_name="reactivateAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).transact(tx_params.as_dict())

    def build_transaction(self, acc: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


class BlacklistAccountMethod(ContractMethod):
    """Various interfaces to the blacklistAccount method."""

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
        """Validate the inputs to the blacklistAccount method."""
        self.validator.assert_valid(
            method_name="blacklistAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).transact(tx_params.as_dict())

    def build_transaction(self, acc: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


class RecoverAccountMethod(ContractMethod):
    """Various interfaces to the recoverAccount method."""

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
        """Validate the inputs to the recoverAccount method."""
        self.validator.assert_valid(
            method_name="recoverAccount", parameter_name="_acc", argument_value=acc,
        )
        acc = self.validate_and_checksum_address(acc)
        return acc

    def call(self, acc: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(acc).call(tx_params.as_dict())

    def send_transaction(
        self, acc: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).transact(tx_params.as_dict())

    def build_transaction(self, acc: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, acc: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (acc) = self.validate_and_normalize_inputs(acc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(acc).estimateGas(tx_params.as_dict())


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

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the authorizeOperator method."""
        self.validator.assert_valid(
            method_name="authorizeOperator",
            parameter_name="_operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return operator

    def call(self, operator: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator).call(tx_params.as_dict())

    def send_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(tx_params.as_dict())


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

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the revokeOperator method."""
        self.validator.assert_valid(
            method_name="revokeOperator",
            parameter_name="_operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return operator

    def call(self, operator: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator).call(tx_params.as_dict())

    def send_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(tx_params.as_dict())


class CreateMethod(ContractMethod):
    """Various interfaces to the create method."""

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

    def validate_and_normalize_inputs(
        self, uri: str, is_nf: bool, data: Union[bytes, str]
    ):
        """Validate the inputs to the create method."""
        self.validator.assert_valid(
            method_name="create", parameter_name="_uri", argument_value=uri,
        )
        self.validator.assert_valid(
            method_name="create", parameter_name="_isNF", argument_value=is_nf,
        )
        self.validator.assert_valid(
            method_name="create", parameter_name="_data", argument_value=data,
        )
        return (uri, is_nf, data)

    def call(
        self,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri, is_nf, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf, data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf, data).estimateGas(
            tx_params.as_dict()
        )


class MintFungibleMethod(ContractMethod):
    """Various interfaces to the mintFungible method."""

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

    def validate_and_normalize_inputs(
        self, to: List[str], _id: int, amounts: List[int], data: Union[bytes, str],
    ):
        """Validate the inputs to the mintFungible method."""
        self.validator.assert_valid(
            method_name="mintFungible", parameter_name="_to", argument_value=to,
        )
        self.validator.assert_valid(
            method_name="mintFungible", parameter_name="_id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="mintFungible",
            parameter_name="_amounts",
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="mintFungible", parameter_name="_data", argument_value=data,
        )
        return (to, _id, amounts, data)

    def call(
        self,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, _id, amounts, data) = self.validate_and_normalize_inputs(
            to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, _id, amounts, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, _id, amounts, data) = self.validate_and_normalize_inputs(
            to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _id, amounts, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, _id, amounts, data) = self.validate_and_normalize_inputs(
            to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _id, amounts, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, _id, amounts, data) = self.validate_and_normalize_inputs(
            to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _id, amounts, data).estimateGas(
            tx_params.as_dict()
        )


class MintNonFungibleMethod(ContractMethod):
    """Various interfaces to the mintNonFungible method."""

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

    def validate_and_normalize_inputs(
        self, to: List[str], _type: int, data: Union[bytes, str]
    ):
        """Validate the inputs to the mintNonFungible method."""
        self.validator.assert_valid(
            method_name="mintNonFungible", parameter_name="_to", argument_value=to,
        )
        self.validator.assert_valid(
            method_name="mintNonFungible", parameter_name="_type", argument_value=_type,
        )
        # safeguard against fractional inputs
        _type = int(_type)
        self.validator.assert_valid(
            method_name="mintNonFungible", parameter_name="_data", argument_value=data,
        )
        return (to, _type, data)

    def call(
        self,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, _type, data) = self.validate_and_normalize_inputs(to, _type, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, _type, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, _type, data) = self.validate_and_normalize_inputs(to, _type, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _type, data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, _type, data) = self.validate_and_normalize_inputs(to, _type, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _type, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, _type, data) = self.validate_and_normalize_inputs(to, _type, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _type, data).estimateGas(tx_params.as_dict())


class SendMethod(ContractMethod):
    """Various interfaces to the send method."""

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

    def validate_and_normalize_inputs(
        self, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str],
    ):
        """Validate the inputs to the send method."""
        self.validator.assert_valid(
            method_name="send", parameter_name="_to", argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="send", parameter_name="_ids", argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="send", parameter_name="_amounts", argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="send", parameter_name="_data", argument_value=data,
        )
        return (to, ids, amounts, data)

    def call(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, ids, amounts, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).estimateGas(
            tx_params.as_dict()
        )


class OperatorSendMethod(ContractMethod):
    """Various interfaces to the operatorSend method."""

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

    def validate_and_normalize_inputs(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
    ):
        """Validate the inputs to the operatorSend method."""
        self.validator.assert_valid(
            method_name="operatorSend", parameter_name="_from", argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="operatorSend", parameter_name="_to", argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="operatorSend", parameter_name="_ids", argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="operatorSend",
            parameter_name="_amounts",
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="operatorSend", parameter_name="_data", argument_value=data,
        )
        self.validator.assert_valid(
            method_name="operatorSend",
            parameter_name="_operatorData",
            argument_value=operator_data,
        )
        return (_from, to, ids, amounts, data, operator_data)

    def call(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, ids, amounts, data, operator_data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, amounts, data, operator_data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, amounts, data, operator_data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, amounts, data, operator_data
        ).estimateGas(tx_params.as_dict())


class BurnMethod(ContractMethod):
    """Various interfaces to the burn method."""

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

    def validate_and_normalize_inputs(
        self, ids: List[int], amounts: List[int], data: Union[bytes, str]
    ):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn", parameter_name="_ids", argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="burn", parameter_name="_amounts", argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="burn", parameter_name="_data", argument_value=data,
        )
        return (ids, amounts, data)

    def call(
        self,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(ids, amounts, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(ids, amounts, data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(ids, amounts, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(ids, amounts, data).estimateGas(
            tx_params.as_dict()
        )


class OperatorBurnMethod(ContractMethod):
    """Various interfaces to the operatorBurn method."""

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

    def validate_and_normalize_inputs(
        self,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
    ):
        """Validate the inputs to the operatorBurn method."""
        self.validator.assert_valid(
            method_name="operatorBurn", parameter_name="_from", argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="operatorBurn", parameter_name="_ids", argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="operatorBurn",
            parameter_name="_amounts",
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="operatorBurn", parameter_name="_data", argument_value=data,
        )
        self.validator.assert_valid(
            method_name="operatorBurn",
            parameter_name="_operatorData",
            argument_value=operator_data,
        )
        return (_from, ids, amounts, data, operator_data)

    def call(
        self,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, ids, amounts, data, operator_data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, ids, amounts, data, operator_data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, ids, amounts, data, operator_data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, ids, amounts, data, operator_data
        ).estimateGas(tx_params.as_dict())


class SwapMethod(ContractMethod):
    """Various interfaces to the swap method."""

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

    def validate_and_normalize_inputs(
        self,
        swap: SwapLibSwap,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the swap method."""
        self.validator.assert_valid(
            method_name="swap", parameter_name="_swap", argument_value=swap,
        )
        self.validator.assert_valid(
            method_name="swap", parameter_name="_nonce", argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name="swap", parameter_name="_expiry", argument_value=expiry,
        )
        # safeguard against fractional inputs
        expiry = int(expiry)
        self.validator.assert_valid(
            method_name="swap", parameter_name="_v", argument_value=v,
        )
        self.validator.assert_valid(
            method_name="swap", parameter_name="_r", argument_value=r,
        )
        self.validator.assert_valid(
            method_name="swap", parameter_name="_s", argument_value=s,
        )
        self.validator.assert_valid(
            method_name="swap", parameter_name="_data", argument_value=data,
        )
        return (swap, nonce, expiry, v, r, s, data)

    def call(
        self,
        swap: SwapLibSwap,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (swap, nonce, expiry, v, r, s, data,) = self.validate_and_normalize_inputs(
            swap, nonce, expiry, v, r, s, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(swap, nonce, expiry, v, r, s, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        swap: SwapLibSwap,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (swap, nonce, expiry, v, r, s, data,) = self.validate_and_normalize_inputs(
            swap, nonce, expiry, v, r, s, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        swap: SwapLibSwap,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (swap, nonce, expiry, v, r, s, data,) = self.validate_and_normalize_inputs(
            swap, nonce, expiry, v, r, s, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            swap, nonce, expiry, v, r, s, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        swap: SwapLibSwap,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (swap, nonce, expiry, v, r, s, data,) = self.validate_and_normalize_inputs(
            swap, nonce, expiry, v, r, s, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s, data).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Implementation:
    """Wrapper class for Implementation Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    domain_separator: DomainSeparatorMethod
    """Constructor-initialized instance of
    :class:`DomainSeparatorMethod`.
    """

    eip712_domain_typehash: Eip712DomainTypehashMethod
    """Constructor-initialized instance of
    :class:`Eip712DomainTypehashMethod`.
    """

    swap_typehash: SwapTypehashMethod
    """Constructor-initialized instance of
    :class:`SwapTypehashMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    renounce_ownership: RenounceOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceOwnershipMethod`.
    """

    signer_nonces: SignerNoncesMethod
    """Constructor-initialized instance of
    :class:`SignerNoncesMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    register: RegisterMethod
    """Constructor-initialized instance of
    :class:`RegisterMethod`.
    """

    add_sub_account: AddSubAccountMethod
    """Constructor-initialized instance of
    :class:`AddSubAccountMethod`.
    """

    suspend_account: SuspendAccountMethod
    """Constructor-initialized instance of
    :class:`SuspendAccountMethod`.
    """

    reactivate_account: ReactivateAccountMethod
    """Constructor-initialized instance of
    :class:`ReactivateAccountMethod`.
    """

    blacklist_account: BlacklistAccountMethod
    """Constructor-initialized instance of
    :class:`BlacklistAccountMethod`.
    """

    recover_account: RecoverAccountMethod
    """Constructor-initialized instance of
    :class:`RecoverAccountMethod`.
    """

    authorize_operator: AuthorizeOperatorMethod
    """Constructor-initialized instance of
    :class:`AuthorizeOperatorMethod`.
    """

    revoke_operator: RevokeOperatorMethod
    """Constructor-initialized instance of
    :class:`RevokeOperatorMethod`.
    """

    create: CreateMethod
    """Constructor-initialized instance of
    :class:`CreateMethod`.
    """

    mint_fungible: MintFungibleMethod
    """Constructor-initialized instance of
    :class:`MintFungibleMethod`.
    """

    mint_non_fungible: MintNonFungibleMethod
    """Constructor-initialized instance of
    :class:`MintNonFungibleMethod`.
    """

    send: SendMethod
    """Constructor-initialized instance of
    :class:`SendMethod`.
    """

    operator_send: OperatorSendMethod
    """Constructor-initialized instance of
    :class:`OperatorSendMethod`.
    """

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    operator_burn: OperatorBurnMethod
    """Constructor-initialized instance of
    :class:`OperatorBurnMethod`.
    """

    swap: SwapMethod
    """Constructor-initialized instance of
    :class:`SwapMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ImplementationValidator = None,
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
            validator = ImplementationValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Implementation.abi(),
        ).functions

        self.domain_separator = DomainSeparatorMethod(
            web3_or_provider, contract_address, functions.DOMAIN_SEPARATOR
        )

        self.eip712_domain_typehash = Eip712DomainTypehashMethod(
            web3_or_provider, contract_address, functions.EIP712_DOMAIN_TYPEHASH,
        )

        self.swap_typehash = SwapTypehashMethod(
            web3_or_provider, contract_address, functions.SWAP_TYPEHASH
        )

        self.name = NameMethod(web3_or_provider, contract_address, functions.name)

        self.owner = OwnerMethod(web3_or_provider, contract_address, functions.owner)

        self.renounce_ownership = RenounceOwnershipMethod(
            web3_or_provider, contract_address, functions.renounceOwnership
        )

        self.signer_nonces = SignerNoncesMethod(
            web3_or_provider, contract_address, functions.signerNonces, validator,
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider, contract_address, functions.transferOwnership, validator,
        )

        self.register = RegisterMethod(
            web3_or_provider, contract_address, functions.register, validator
        )

        self.add_sub_account = AddSubAccountMethod(
            web3_or_provider, contract_address, functions.addSubAccount, validator,
        )

        self.suspend_account = SuspendAccountMethod(
            web3_or_provider, contract_address, functions.suspendAccount, validator,
        )

        self.reactivate_account = ReactivateAccountMethod(
            web3_or_provider, contract_address, functions.reactivateAccount, validator,
        )

        self.blacklist_account = BlacklistAccountMethod(
            web3_or_provider, contract_address, functions.blacklistAccount, validator,
        )

        self.recover_account = RecoverAccountMethod(
            web3_or_provider, contract_address, functions.recoverAccount, validator,
        )

        self.authorize_operator = AuthorizeOperatorMethod(
            web3_or_provider, contract_address, functions.authorizeOperator, validator,
        )

        self.revoke_operator = RevokeOperatorMethod(
            web3_or_provider, contract_address, functions.revokeOperator, validator,
        )

        self.create = CreateMethod(
            web3_or_provider, contract_address, functions.create, validator
        )

        self.mint_fungible = MintFungibleMethod(
            web3_or_provider, contract_address, functions.mintFungible, validator,
        )

        self.mint_non_fungible = MintNonFungibleMethod(
            web3_or_provider, contract_address, functions.mintNonFungible, validator,
        )

        self.send = SendMethod(
            web3_or_provider, contract_address, functions.send, validator
        )

        self.operator_send = OperatorSendMethod(
            web3_or_provider, contract_address, functions.operatorSend, validator,
        )

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

        self.operator_burn = OperatorBurnMethod(
            web3_or_provider, contract_address, functions.operatorBurn, validator,
        )

        self.swap = SwapMethod(
            web3_or_provider, contract_address, functions.swap, validator
        )

    def get_ownership_transferred_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnershipTransferred event.

        :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Implementation.abi(),
            )
            .events.OwnershipTransferred()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address","name":"_token","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[],"name":"EIP712_DOMAIN_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[],"name":"SWAP_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"signerNonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"}],"name":"register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"},{"internalType":"string","name":"_name","type":"string"}],"name":"addSubAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"suspendAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"reactivateAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"blacklistAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_acc","type":"address"}],"name":"recoverAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"authorizeOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"revokeOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"},{"internalType":"bool","name":"_isNF","type":"bool"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"create","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_to","type":"address[]"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"mintFungible","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_to","type":"address[]"},{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"mintNonFungible","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"send","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"operatorSend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"operatorBurn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256[]","name":"senderTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"senderTokenAmounts","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenAmounts","type":"uint256[]"}],"internalType":"struct SwapLib.Swap","name":"_swap","type":"tuple"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"uint256","name":"_expiry","type":"uint256"},{"internalType":"uint8","name":"_v","type":"uint8"},{"internalType":"bytes32","name":"_r","type":"bytes32"},{"internalType":"bytes32","name":"_s","type":"bytes32"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
