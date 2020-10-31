"""Generated wrapper for Token Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for Token below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        TokenValidator,
    )
except ImportError:

    class TokenValidator(  # type: ignore
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


class BurnerRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the BURNER_ROLE method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class DefaultAdminRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the DEFAULT_ADMIN_ROLE method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class DomainSeparatorMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the DOMAIN_SEPARATOR method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class Eip712DomainTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the EIP712_DOMAIN_TYPEHASH method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class MinterRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the MINTER_ROLE method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class SwapTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the SWAP_TYPEHASH method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class SwapVerifyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the SwapVerify method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str]):
        """Validate the inputs to the SwapVerify method."""
        self.validator.assert_valid(
            method_name='SwapVerify',
            parameter_name='_swap',
            argument_value=swap,
        )
        self.validator.assert_valid(
            method_name='SwapVerify',
            parameter_name='_nonce',
            argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name='SwapVerify',
            parameter_name='_expiry',
            argument_value=expiry,
        )
        # safeguard against fractional inputs
        expiry = int(expiry)
        self.validator.assert_valid(
            method_name='SwapVerify',
            parameter_name='_v',
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name='SwapVerify',
            parameter_name='_r',
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name='SwapVerify',
            parameter_name='_s',
            argument_value=s,
        )
        return (swap, nonce, expiry, v, r, s)

    def call(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (swap, nonce, expiry, v, r, s) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(swap, nonce, expiry, v, r, s).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (swap, nonce, expiry, v, r, s) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s).transact(tx_params.as_dict())

    def build_transaction(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (swap, nonce, expiry, v, r, s) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (swap, nonce, expiry, v, r, s) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s).estimateGas(tx_params.as_dict())

class CreatorsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the creators method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the creators method."""
        self.validator.assert_valid(
            method_name='creators',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class GetNonFungibleBaseTypeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getNonFungibleBaseType method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getNonFungibleBaseType method."""
        self.validator.assert_valid(
            method_name='getNonFungibleBaseType',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class GetNonFungibleIndexMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getNonFungibleIndex method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getNonFungibleIndex method."""
        self.validator.assert_valid(
            method_name='getNonFungibleIndex',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class GetRoleAdminMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleAdmin method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleAdmin method."""
        self.validator.assert_valid(
            method_name='getRoleAdmin',
            parameter_name='role',
            argument_value=role,
        )
        return (role)

    def call(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())

class GetRoleMemberMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleMember method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], index: int):
        """Validate the inputs to the getRoleMember method."""
        self.validator.assert_valid(
            method_name='getRoleMember',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='getRoleMember',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (role, index)

    def call(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, index).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).estimateGas(tx_params.as_dict())

class GetRoleMemberCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleMemberCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleMemberCount method."""
        self.validator.assert_valid(
            method_name='getRoleMemberCount',
            parameter_name='role',
            argument_value=role,
        )
        return (role)

    def call(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())

class GrantRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the grantRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the grantRole method."""
        self.validator.assert_valid(
            method_name='grantRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='grantRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class HasRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the hasRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the hasRole method."""
        self.validator.assert_valid(
            method_name='hasRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='hasRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class IsFungibleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isFungible method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isFungible method."""
        self.validator.assert_valid(
            method_name='isFungible',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class IsNonFungibleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isNonFungible method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungible method."""
        self.validator.assert_valid(
            method_name='isNonFungible',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class IsNonFungibleBaseTypeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isNonFungibleBaseType method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungibleBaseType method."""
        self.validator.assert_valid(
            method_name='isNonFungibleBaseType',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class IsNonFungibleItemMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isNonFungibleItem method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungibleItem method."""
        self.validator.assert_valid(
            method_name='isNonFungibleItem',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class MaxIndexMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the maxIndex method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the maxIndex method."""
        self.validator.assert_valid(
            method_name='maxIndex',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class NameMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the name method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class OwnerOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the ownerOf method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the ownerOf method."""
        self.validator.assert_valid(
            method_name='ownerOf',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())

class PausedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the paused method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class RenounceRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounceRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the renounceRole method."""
        self.validator.assert_valid(
            method_name='renounceRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='renounceRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class RevokeRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the revokeRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the revokeRole method."""
        self.validator.assert_valid(
            method_name='revokeRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='revokeRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class SignerNoncesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the signerNonces method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the signerNonces method."""
        self.validator.assert_valid(
            method_name='signerNonces',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class InitializeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, granularity: int):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_granularity',
            argument_value=granularity,
        )
        # safeguard against fractional inputs
        granularity = int(granularity)
        return (granularity)

    def call(self, granularity: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (granularity) = self.validate_and_normalize_inputs(granularity)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(granularity).call(tx_params.as_dict())

    def send_transaction(self, granularity: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (granularity) = self.validate_and_normalize_inputs(granularity)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(granularity).transact(tx_params.as_dict())

    def build_transaction(self, granularity: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (granularity) = self.validate_and_normalize_inputs(granularity)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(granularity).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, granularity: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (granularity) = self.validate_and_normalize_inputs(granularity)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(granularity).estimateGas(tx_params.as_dict())

class CreateMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the create method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, uri: str, is_nf: bool, data: Union[bytes, str]):
        """Validate the inputs to the create method."""
        self.validator.assert_valid(
            method_name='create',
            parameter_name='uri',
            argument_value=uri,
        )
        self.validator.assert_valid(
            method_name='create',
            parameter_name='_isNF',
            argument_value=is_nf,
        )
        self.validator.assert_valid(
            method_name='create',
            parameter_name='_data',
            argument_value=data,
        )
        return (uri, is_nf, data)

    def call(self, uri: str, is_nf: bool, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(uri, is_nf, data).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, uri: str, is_nf: bool, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf, data).transact(tx_params.as_dict())

    def build_transaction(self, uri: str, is_nf: bool, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, uri: str, is_nf: bool, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (uri, is_nf, data) = self.validate_and_normalize_inputs(uri, is_nf, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf, data).estimateGas(tx_params.as_dict())

class MintFungibleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the mintFungible method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int, to: List[str], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str]):
        """Validate the inputs to the mintFungible method."""
        self.validator.assert_valid(
            method_name='mintFungible',
            parameter_name='_id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name='mintFungible',
            parameter_name='_to',
            argument_value=to,
        )
        self.validator.assert_valid(
            method_name='mintFungible',
            parameter_name='_amounts',
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name='mintFungible',
            parameter_name='_data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='mintFungible',
            parameter_name='_operatorData',
            argument_value=operator_data,
        )
        return (_id, to, amounts, data, operator_data)

    def call(self, _id: int, to: List[str], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id, to, amounts, data, operator_data) = self.validate_and_normalize_inputs(_id, to, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_id, to, amounts, data, operator_data).call(tx_params.as_dict())

    def send_transaction(self, _id: int, to: List[str], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id, to, amounts, data, operator_data) = self.validate_and_normalize_inputs(_id, to, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id, to, amounts, data, operator_data).transact(tx_params.as_dict())

    def build_transaction(self, _id: int, to: List[str], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id, to, amounts, data, operator_data) = self.validate_and_normalize_inputs(_id, to, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id, to, amounts, data, operator_data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _id: int, to: List[str], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id, to, amounts, data, operator_data) = self.validate_and_normalize_inputs(_id, to, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id, to, amounts, data, operator_data).estimateGas(tx_params.as_dict())

class MintNonFungibleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the mintNonFungible method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _type: int, to: List[str], data: Union[bytes, str], operator_data: Union[bytes, str]):
        """Validate the inputs to the mintNonFungible method."""
        self.validator.assert_valid(
            method_name='mintNonFungible',
            parameter_name='_type',
            argument_value=_type,
        )
        # safeguard against fractional inputs
        _type = int(_type)
        self.validator.assert_valid(
            method_name='mintNonFungible',
            parameter_name='_to',
            argument_value=to,
        )
        self.validator.assert_valid(
            method_name='mintNonFungible',
            parameter_name='_data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='mintNonFungible',
            parameter_name='_operatorData',
            argument_value=operator_data,
        )
        return (_type, to, data, operator_data)

    def call(self, _type: int, to: List[str], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type, to, data, operator_data) = self.validate_and_normalize_inputs(_type, to, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_type, to, data, operator_data).call(tx_params.as_dict())

    def send_transaction(self, _type: int, to: List[str], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_type, to, data, operator_data) = self.validate_and_normalize_inputs(_type, to, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, to, data, operator_data).transact(tx_params.as_dict())

    def build_transaction(self, _type: int, to: List[str], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type, to, data, operator_data) = self.validate_and_normalize_inputs(_type, to, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, to, data, operator_data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _type: int, to: List[str], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_type, to, data, operator_data) = self.validate_and_normalize_inputs(_type, to, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, to, data, operator_data).estimateGas(tx_params.as_dict())

class SendMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the send method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str]):
        """Validate the inputs to the send method."""
        self.validator.assert_valid(
            method_name='send',
            parameter_name='_to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='send',
            parameter_name='_ids',
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name='send',
            parameter_name='_amounts',
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name='send',
            parameter_name='_data',
            argument_value=data,
        )
        return (to, ids, amounts, data)

    def call(self, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, ids, amounts, data).call(tx_params.as_dict())

    def send_transaction(self, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).transact(tx_params.as_dict())

    def build_transaction(self, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).estimateGas(tx_params.as_dict())

class OperatorSendMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the operatorSend method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str]):
        """Validate the inputs to the operatorSend method."""
        self.validator.assert_valid(
            method_name='operatorSend',
            parameter_name='_from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='operatorSend',
            parameter_name='_to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='operatorSend',
            parameter_name='_ids',
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name='operatorSend',
            parameter_name='_amounts',
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name='operatorSend',
            parameter_name='_data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='operatorSend',
            parameter_name='_operatorData',
            argument_value=operator_data,
        )
        return (_from, to, ids, amounts, data, operator_data)

    def call(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, ids, amounts, data, operator_data).call(tx_params.as_dict())

    def send_transaction(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data, operator_data).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data, operator_data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data, operator_data).estimateGas(tx_params.as_dict())

class BurnMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, ids: List[int], amounts: List[int], data: Union[bytes, str]):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='_ids',
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='_amounts',
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='_data',
            argument_value=data,
        )
        return (ids, amounts, data)

    def call(self, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(ids, amounts, data).call(tx_params.as_dict())

    def send_transaction(self, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(ids, amounts, data).transact(tx_params.as_dict())

    def build_transaction(self, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(ids, amounts, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (ids, amounts, data) = self.validate_and_normalize_inputs(ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(ids, amounts, data).estimateGas(tx_params.as_dict())

class OperatorBurnMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the operatorBurn method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str]):
        """Validate the inputs to the operatorBurn method."""
        self.validator.assert_valid(
            method_name='operatorBurn',
            parameter_name='_from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='operatorBurn',
            parameter_name='_ids',
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name='operatorBurn',
            parameter_name='_amounts',
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name='operatorBurn',
            parameter_name='_data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='operatorBurn',
            parameter_name='_operatorData',
            argument_value=operator_data,
        )
        return (_from, ids, amounts, data, operator_data)

    def call(self, _from: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, ids, amounts, data, operator_data).call(tx_params.as_dict())

    def send_transaction(self, _from: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, ids, amounts, data, operator_data).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, ids, amounts, data, operator_data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, ids: List[int], amounts: List[int], data: Union[bytes, str], operator_data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, ids, amounts, data, operator_data) = self.validate_and_normalize_inputs(_from, ids, amounts, data, operator_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, ids, amounts, data, operator_data).estimateGas(tx_params.as_dict())

class AuthorizeOperatorMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the authorizeOperator method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the authorizeOperator method."""
        self.validator.assert_valid(
            method_name='authorizeOperator',
            parameter_name='_operator',
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (operator)

    def call(self, operator: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator).call(tx_params.as_dict())

    def send_transaction(self, operator: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(self, operator: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(tx_params.as_dict())

class RevokeOperatorMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the revokeOperator method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the revokeOperator method."""
        self.validator.assert_valid(
            method_name='revokeOperator',
            parameter_name='_operator',
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (operator)

    def call(self, operator: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator).call(tx_params.as_dict())

    def send_transaction(self, operator: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(self, operator: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(tx_params.as_dict())

class BalanceOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, owner: str, _id: int):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='_owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='_id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (owner, _id)

    def call(self, owner: str, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, _id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, owner: str, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, _id).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, _id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, _id).estimateGas(tx_params.as_dict())

class BalanceOfBatchMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOfBatch method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, owners: List[str], ids: List[int]):
        """Validate the inputs to the balanceOfBatch method."""
        self.validator.assert_valid(
            method_name='balanceOfBatch',
            parameter_name='_owners',
            argument_value=owners,
        )
        self.validator.assert_valid(
            method_name='balanceOfBatch',
            parameter_name='_ids',
            argument_value=ids,
        )
        return (owners, ids)

    def call(self, owners: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> List[int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owners, ids).call(tx_params.as_dict())
        return [int(element) for element in returned]

    def send_transaction(self, owners: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owners, ids).transact(tx_params.as_dict())

    def build_transaction(self, owners: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owners, ids).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owners: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owners, ids).estimateGas(tx_params.as_dict())

class IsOperatorForMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isOperatorFor method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str, holder: str):
        """Validate the inputs to the isOperatorFor method."""
        self.validator.assert_valid(
            method_name='isOperatorFor',
            parameter_name='_operator',
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name='isOperatorFor',
            parameter_name='_holder',
            argument_value=holder,
        )
        holder = self.validate_and_checksum_address(holder)
        return (operator, holder)

    def call(self, operator: str, holder: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator, holder) = self.validate_and_normalize_inputs(operator, holder)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(operator, holder).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, operator: str, holder: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator, holder) = self.validate_and_normalize_inputs(operator, holder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, holder).transact(tx_params.as_dict())

    def build_transaction(self, operator: str, holder: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator, holder) = self.validate_and_normalize_inputs(operator, holder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, holder).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, operator: str, holder: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (operator, holder) = self.validate_and_normalize_inputs(operator, holder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, holder).estimateGas(tx_params.as_dict())

class GranularityNfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the granularityNF method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class SwapMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the swap method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], data: Union[bytes, str]):
        """Validate the inputs to the swap method."""
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_swap',
            argument_value=swap,
        )
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_nonce',
            argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_expiry',
            argument_value=expiry,
        )
        # safeguard against fractional inputs
        expiry = int(expiry)
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_v',
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_r',
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_s',
            argument_value=s,
        )
        self.validator.assert_valid(
            method_name='swap',
            parameter_name='_data',
            argument_value=data,
        )
        return (swap, nonce, expiry, v, r, s, data)

    def call(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (swap, nonce, expiry, v, r, s, data) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(swap, nonce, expiry, v, r, s, data).call(tx_params.as_dict())

    def send_transaction(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (swap, nonce, expiry, v, r, s, data) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s, data).transact(tx_params.as_dict())

    def build_transaction(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (swap, nonce, expiry, v, r, s, data) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, swap: SwapLibSwap, nonce: int, expiry: int, v: int, r: Union[bytes, str], s: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (swap, nonce, expiry, v, r, s, data) = self.validate_and_normalize_inputs(swap, nonce, expiry, v, r, s, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(swap, nonce, expiry, v, r, s, data).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Token:
    """Wrapper class for Token Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    burner_role: BurnerRoleMethod
    """Constructor-initialized instance of
    :class:`BurnerRoleMethod`.
    """

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    domain_separator: DomainSeparatorMethod
    """Constructor-initialized instance of
    :class:`DomainSeparatorMethod`.
    """

    eip712_domain_typehash: Eip712DomainTypehashMethod
    """Constructor-initialized instance of
    :class:`Eip712DomainTypehashMethod`.
    """

    minter_role: MinterRoleMethod
    """Constructor-initialized instance of
    :class:`MinterRoleMethod`.
    """

    swap_typehash: SwapTypehashMethod
    """Constructor-initialized instance of
    :class:`SwapTypehashMethod`.
    """

    swap_verify: SwapVerifyMethod
    """Constructor-initialized instance of
    :class:`SwapVerifyMethod`.
    """

    creators: CreatorsMethod
    """Constructor-initialized instance of
    :class:`CreatorsMethod`.
    """

    get_non_fungible_base_type: GetNonFungibleBaseTypeMethod
    """Constructor-initialized instance of
    :class:`GetNonFungibleBaseTypeMethod`.
    """

    get_non_fungible_index: GetNonFungibleIndexMethod
    """Constructor-initialized instance of
    :class:`GetNonFungibleIndexMethod`.
    """

    get_role_admin: GetRoleAdminMethod
    """Constructor-initialized instance of
    :class:`GetRoleAdminMethod`.
    """

    get_role_member: GetRoleMemberMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberMethod`.
    """

    get_role_member_count: GetRoleMemberCountMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberCountMethod`.
    """

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
    """

    is_fungible: IsFungibleMethod
    """Constructor-initialized instance of
    :class:`IsFungibleMethod`.
    """

    is_non_fungible: IsNonFungibleMethod
    """Constructor-initialized instance of
    :class:`IsNonFungibleMethod`.
    """

    is_non_fungible_base_type: IsNonFungibleBaseTypeMethod
    """Constructor-initialized instance of
    :class:`IsNonFungibleBaseTypeMethod`.
    """

    is_non_fungible_item: IsNonFungibleItemMethod
    """Constructor-initialized instance of
    :class:`IsNonFungibleItemMethod`.
    """

    max_index: MaxIndexMethod
    """Constructor-initialized instance of
    :class:`MaxIndexMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    owner_of: OwnerOfMethod
    """Constructor-initialized instance of
    :class:`OwnerOfMethod`.
    """

    paused: PausedMethod
    """Constructor-initialized instance of
    :class:`PausedMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    signer_nonces: SignerNoncesMethod
    """Constructor-initialized instance of
    :class:`SignerNoncesMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
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

    authorize_operator: AuthorizeOperatorMethod
    """Constructor-initialized instance of
    :class:`AuthorizeOperatorMethod`.
    """

    revoke_operator: RevokeOperatorMethod
    """Constructor-initialized instance of
    :class:`RevokeOperatorMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    balance_of_batch: BalanceOfBatchMethod
    """Constructor-initialized instance of
    :class:`BalanceOfBatchMethod`.
    """

    is_operator_for: IsOperatorForMethod
    """Constructor-initialized instance of
    :class:`IsOperatorForMethod`.
    """

    granularity_nf: GranularityNfMethod
    """Constructor-initialized instance of
    :class:`GranularityNfMethod`.
    """

    swap: SwapMethod
    """Constructor-initialized instance of
    :class:`SwapMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: TokenValidator = None,
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
            validator = TokenValidator(web3_or_provider, contract_address)

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
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Token.abi()).functions

        self.burner_role = BurnerRoleMethod(web3_or_provider, contract_address, functions.BURNER_ROLE)

        self.default_admin_role = DefaultAdminRoleMethod(web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE)

        self.domain_separator = DomainSeparatorMethod(web3_or_provider, contract_address, functions.DOMAIN_SEPARATOR)

        self.eip712_domain_typehash = Eip712DomainTypehashMethod(web3_or_provider, contract_address, functions.EIP712_DOMAIN_TYPEHASH)

        self.minter_role = MinterRoleMethod(web3_or_provider, contract_address, functions.MINTER_ROLE)

        self.swap_typehash = SwapTypehashMethod(web3_or_provider, contract_address, functions.SWAP_TYPEHASH)

        self.swap_verify = SwapVerifyMethod(web3_or_provider, contract_address, functions.SwapVerify, validator)

        self.creators = CreatorsMethod(web3_or_provider, contract_address, functions.creators, validator)

        self.get_non_fungible_base_type = GetNonFungibleBaseTypeMethod(web3_or_provider, contract_address, functions.getNonFungibleBaseType, validator)

        self.get_non_fungible_index = GetNonFungibleIndexMethod(web3_or_provider, contract_address, functions.getNonFungibleIndex, validator)

        self.get_role_admin = GetRoleAdminMethod(web3_or_provider, contract_address, functions.getRoleAdmin, validator)

        self.get_role_member = GetRoleMemberMethod(web3_or_provider, contract_address, functions.getRoleMember, validator)

        self.get_role_member_count = GetRoleMemberCountMethod(web3_or_provider, contract_address, functions.getRoleMemberCount, validator)

        self.grant_role = GrantRoleMethod(web3_or_provider, contract_address, functions.grantRole, validator)

        self.has_role = HasRoleMethod(web3_or_provider, contract_address, functions.hasRole, validator)

        self.is_fungible = IsFungibleMethod(web3_or_provider, contract_address, functions.isFungible, validator)

        self.is_non_fungible = IsNonFungibleMethod(web3_or_provider, contract_address, functions.isNonFungible, validator)

        self.is_non_fungible_base_type = IsNonFungibleBaseTypeMethod(web3_or_provider, contract_address, functions.isNonFungibleBaseType, validator)

        self.is_non_fungible_item = IsNonFungibleItemMethod(web3_or_provider, contract_address, functions.isNonFungibleItem, validator)

        self.max_index = MaxIndexMethod(web3_or_provider, contract_address, functions.maxIndex, validator)

        self.name = NameMethod(web3_or_provider, contract_address, functions.name)

        self.owner_of = OwnerOfMethod(web3_or_provider, contract_address, functions.ownerOf, validator)

        self.paused = PausedMethod(web3_or_provider, contract_address, functions.paused)

        self.renounce_role = RenounceRoleMethod(web3_or_provider, contract_address, functions.renounceRole, validator)

        self.revoke_role = RevokeRoleMethod(web3_or_provider, contract_address, functions.revokeRole, validator)

        self.signer_nonces = SignerNoncesMethod(web3_or_provider, contract_address, functions.signerNonces, validator)

        self.initialize = InitializeMethod(web3_or_provider, contract_address, functions.initialize, validator)

        self.create = CreateMethod(web3_or_provider, contract_address, functions.create, validator)

        self.mint_fungible = MintFungibleMethod(web3_or_provider, contract_address, functions.mintFungible, validator)

        self.mint_non_fungible = MintNonFungibleMethod(web3_or_provider, contract_address, functions.mintNonFungible, validator)

        self.send = SendMethod(web3_or_provider, contract_address, functions.send, validator)

        self.operator_send = OperatorSendMethod(web3_or_provider, contract_address, functions.operatorSend, validator)

        self.burn = BurnMethod(web3_or_provider, contract_address, functions.burn, validator)

        self.operator_burn = OperatorBurnMethod(web3_or_provider, contract_address, functions.operatorBurn, validator)

        self.authorize_operator = AuthorizeOperatorMethod(web3_or_provider, contract_address, functions.authorizeOperator, validator)

        self.revoke_operator = RevokeOperatorMethod(web3_or_provider, contract_address, functions.revokeOperator, validator)

        self.balance_of = BalanceOfMethod(web3_or_provider, contract_address, functions.balanceOf, validator)

        self.balance_of_batch = BalanceOfBatchMethod(web3_or_provider, contract_address, functions.balanceOfBatch, validator)

        self.is_operator_for = IsOperatorForMethod(web3_or_provider, contract_address, functions.isOperatorFor, validator)

        self.granularity_nf = GranularityNfMethod(web3_or_provider, contract_address, functions.granularityNF)

        self.swap = SwapMethod(web3_or_provider, contract_address, functions.swap, validator)

    def get_authorized_operator_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuthorizedOperator event.

        :param tx_hash: hash of transaction emitting AuthorizedOperator event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.AuthorizedOperator().processReceipt(tx_receipt)
    def get_burned_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Burned event.

        :param tx_hash: hash of transaction emitting Burned event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.Burned().processReceipt(tx_receipt)
    def get_created_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Created event.

        :param tx_hash: hash of transaction emitting Created event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.Created().processReceipt(tx_receipt)
    def get_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Minted event.

        :param tx_hash: hash of transaction emitting Minted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.Minted().processReceipt(tx_receipt)
    def get_paused_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Paused event.

        :param tx_hash: hash of transaction emitting Paused event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.Paused().processReceipt(tx_receipt)
    def get_revoked_operator_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RevokedOperator event.

        :param tx_hash: hash of transaction emitting RevokedOperator event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.RevokedOperator().processReceipt(tx_receipt)
    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.RoleAdminChanged().processReceipt(tx_receipt)
    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.RoleGranted().processReceipt(tx_receipt)
    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.RoleRevoked().processReceipt(tx_receipt)
    def get_sent_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Sent event.

        :param tx_hash: hash of transaction emitting Sent event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.Sent().processReceipt(tx_receipt)
    def get_uri_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for URI event.

        :param tx_hash: hash of transaction emitting URI event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.URI().processReceipt(tx_receipt)
    def get_unpaused_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Unpaused event.

        :param tx_hash: hash of transaction emitting Unpaused event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Token.abi()).events.Unpaused().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"holder","type":"address"}],"name":"AuthorizedOperator","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"operatorData","type":"bytes"}],"name":"Burned","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"creator","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"Created","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"operatorData","type":"bytes"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"holder","type":"address"}],"name":"RevokedOperator","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"operatorData","type":"bytes"}],"name":"Sent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"BURNER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"EIP712_DOMAIN_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SWAP_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256[]","name":"senderTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"senderTokenAmounts","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenAmounts","type":"uint256[]"}],"internalType":"struct SwapLib.Swap","name":"_swap","type":"tuple"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"uint256","name":"_expiry","type":"uint256"},{"internalType":"uint8","name":"_v","type":"uint8"},{"internalType":"bytes32","name":"_r","type":"bytes32"},{"internalType":"bytes32","name":"_s","type":"bytes32"}],"name":"SwapVerify","outputs":[{"internalType":"address","name":"signer_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"creators","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getNonFungibleBaseType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getNonFungibleIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isFungible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungibleBaseType","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungibleItem","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"maxIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"signerNonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_granularity","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uri","type":"string"},{"internalType":"bool","name":"_isNF","type":"bool"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"create","outputs":[{"internalType":"uint256","name":"type_","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address[]","name":"_to","type":"address[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"mintFungible","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"address[]","name":"_to","type":"address[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"mintNonFungible","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"send","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"operatorSend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"operatorBurn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"authorizeOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"revokeOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_owners","type":"address[]"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"balances_","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"address","name":"_holder","type":"address"}],"name":"isOperatorFor","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"granularityNF","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256[]","name":"senderTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"senderTokenAmounts","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenAmounts","type":"uint256[]"}],"internalType":"struct SwapLib.Swap","name":"_swap","type":"tuple"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"uint256","name":"_expiry","type":"uint256"},{"internalType":"uint8","name":"_v","type":"uint8"},{"internalType":"bytes32","name":"_r","type":"bytes32"},{"internalType":"bytes32","name":"_s","type":"bytes32"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
