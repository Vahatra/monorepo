"""Generated wrapper for Token Solidity contract."""

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


class CreatorsMethod(ContractMethod):
    """Various interfaces to the creators method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the creators method."""
        self.validator.assert_valid(
            method_name="creators", parameter_name="index_0", argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())


class GetNonFungibleBaseTypeMethod(ContractMethod):
    """Various interfaces to the getNonFungibleBaseType method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getNonFungibleBaseType method."""
        self.validator.assert_valid(
            method_name="getNonFungibleBaseType",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class GetNonFungibleIndexMethod(ContractMethod):
    """Various interfaces to the getNonFungibleIndex method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getNonFungibleIndex method."""
        self.validator.assert_valid(
            method_name="getNonFungibleIndex", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


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


class IsFungibleMethod(ContractMethod):
    """Various interfaces to the isFungible method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isFungible method."""
        self.validator.assert_valid(
            method_name="isFungible", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsNonFungibleMethod(ContractMethod):
    """Various interfaces to the isNonFungible method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungible method."""
        self.validator.assert_valid(
            method_name="isNonFungible", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsNonFungibleBaseTypeMethod(ContractMethod):
    """Various interfaces to the isNonFungibleBaseType method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungibleBaseType method."""
        self.validator.assert_valid(
            method_name="isNonFungibleBaseType",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsNonFungibleItemMethod(ContractMethod):
    """Various interfaces to the isNonFungibleItem method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungibleItem method."""
        self.validator.assert_valid(
            method_name="isNonFungibleItem", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class MaxIndexMethod(ContractMethod):
    """Various interfaces to the maxIndex method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the maxIndex method."""
        self.validator.assert_valid(
            method_name="maxIndex", parameter_name="index_0", argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())


class OwnerOfMethod(ContractMethod):
    """Various interfaces to the ownerOf method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the ownerOf method."""
        self.validator.assert_valid(
            method_name="ownerOf", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


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
        self, sender: str, uri: str, is_nf: bool, data: Union[bytes, str]
    ):
        """Validate the inputs to the create method."""
        self.validator.assert_valid(
            method_name="create", parameter_name="_sender", argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
        self.validator.assert_valid(
            method_name="create", parameter_name="_uri", argument_value=uri,
        )
        self.validator.assert_valid(
            method_name="create", parameter_name="_isNF", argument_value=is_nf,
        )
        self.validator.assert_valid(
            method_name="create", parameter_name="_data", argument_value=data,
        )
        return (sender, uri, is_nf, data)

    def call(
        self,
        sender: str,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sender, uri, is_nf, data) = self.validate_and_normalize_inputs(
            sender, uri, is_nf, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(sender, uri, is_nf, data).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        sender: str,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, uri, is_nf, data) = self.validate_and_normalize_inputs(
            sender, uri, is_nf, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, uri, is_nf, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        sender: str,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, uri, is_nf, data) = self.validate_and_normalize_inputs(
            sender, uri, is_nf, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, uri, is_nf, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        sender: str,
        uri: str,
        is_nf: bool,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (sender, uri, is_nf, data) = self.validate_and_normalize_inputs(
            sender, uri, is_nf, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, uri, is_nf, data).estimateGas(
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
        self,
        sender: str,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the mintFungible method."""
        self.validator.assert_valid(
            method_name="mintFungible", parameter_name="_sender", argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
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
        return (sender, to, _id, amounts, data)

    def call(
        self,
        sender: str,
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
        (sender, to, _id, amounts, data) = self.validate_and_normalize_inputs(
            sender, to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sender, to, _id, amounts, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        sender: str,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, to, _id, amounts, data) = self.validate_and_normalize_inputs(
            sender, to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, to, _id, amounts, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        sender: str,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, to, _id, amounts, data) = self.validate_and_normalize_inputs(
            sender, to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, to, _id, amounts, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        sender: str,
        to: List[str],
        _id: int,
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (sender, to, _id, amounts, data) = self.validate_and_normalize_inputs(
            sender, to, _id, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, to, _id, amounts, data).estimateGas(
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
        self, sender: str, to: List[str], _type: int, data: Union[bytes, str]
    ):
        """Validate the inputs to the mintNonFungible method."""
        self.validator.assert_valid(
            method_name="mintNonFungible",
            parameter_name="_sender",
            argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
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
        return (sender, to, _type, data)

    def call(
        self,
        sender: str,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sender, to, _type, data) = self.validate_and_normalize_inputs(
            sender, to, _type, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sender, to, _type, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        sender: str,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, to, _type, data) = self.validate_and_normalize_inputs(
            sender, to, _type, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, to, _type, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        sender: str,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, to, _type, data) = self.validate_and_normalize_inputs(
            sender, to, _type, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, to, _type, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        sender: str,
        to: List[str],
        _type: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (sender, to, _type, data) = self.validate_and_normalize_inputs(
            sender, to, _type, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, to, _type, data).estimateGas(
            tx_params.as_dict()
        )


class BalanceOfMethod(ContractMethod):
    """Various interfaces to the balanceOf method."""

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

    def validate_and_normalize_inputs(self, owner: str, _id: int):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf", parameter_name="_owner", argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="balanceOf", parameter_name="_id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (owner, _id)

    def call(self, owner: str, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, _id).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, owner: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, _id).estimateGas(tx_params.as_dict())


class BalanceOfBatchMethod(ContractMethod):
    """Various interfaces to the balanceOfBatch method."""

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

    def validate_and_normalize_inputs(self, owners: List[str], ids: List[int]):
        """Validate the inputs to the balanceOfBatch method."""
        self.validator.assert_valid(
            method_name="balanceOfBatch",
            parameter_name="_owners",
            argument_value=owners,
        )
        self.validator.assert_valid(
            method_name="balanceOfBatch", parameter_name="_ids", argument_value=ids,
        )
        return (owners, ids)

    def call(
        self, owners: List[str], ids: List[int], tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owners, ids).call(tx_params.as_dict())
        return [int(element) for element in returned]

    def estimate_gas(
        self, owners: List[str], ids: List[int], tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owners, ids).estimateGas(tx_params.as_dict())


class GranularityMethod(ContractMethod):
    """Various interfaces to the granularity method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


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
        self, sender: str, signer: str, swap: SwapLibSwap, data: Union[bytes, str],
    ):
        """Validate the inputs to the swap method."""
        self.validator.assert_valid(
            method_name="swap", parameter_name="_sender", argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
        self.validator.assert_valid(
            method_name="swap", parameter_name="_signer", argument_value=signer,
        )
        signer = self.validate_and_checksum_address(signer)
        self.validator.assert_valid(
            method_name="swap", parameter_name="_swap", argument_value=swap,
        )
        self.validator.assert_valid(
            method_name="swap", parameter_name="_data", argument_value=data,
        )
        return (sender, signer, swap, data)

    def call(
        self,
        sender: str,
        signer: str,
        swap: SwapLibSwap,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sender, signer, swap, data) = self.validate_and_normalize_inputs(
            sender, signer, swap, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sender, signer, swap, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        sender: str,
        signer: str,
        swap: SwapLibSwap,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, signer, swap, data) = self.validate_and_normalize_inputs(
            sender, signer, swap, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, signer, swap, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        sender: str,
        signer: str,
        swap: SwapLibSwap,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, signer, swap, data) = self.validate_and_normalize_inputs(
            sender, signer, swap, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, signer, swap, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        sender: str,
        signer: str,
        swap: SwapLibSwap,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (sender, signer, swap, data) = self.validate_and_normalize_inputs(
            sender, signer, swap, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, signer, swap, data).estimateGas(
            tx_params.as_dict()
        )


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
        self,
        operator: str,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
    ):
        """Validate the inputs to the send method."""
        self.validator.assert_valid(
            method_name="send", parameter_name="_operator", argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="send", parameter_name="_from", argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
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
        self.validator.assert_valid(
            method_name="send",
            parameter_name="_operatorData",
            argument_value=operator_data,
        )
        return (operator, _from, to, ids, amounts, data, operator_data)

    def call(
        self,
        operator: str,
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
            operator,
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            operator, _from, to, ids, amounts, data, operator_data
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        operator: str,
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
            operator,
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, to, ids, amounts, data, operator_data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator: str,
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
            operator,
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, to, ids, amounts, data, operator_data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
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
            operator,
            _from,
            to,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, to, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, to, ids, amounts, data, operator_data
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
        self,
        operator: str,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
    ):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn", parameter_name="_operator", argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="burn", parameter_name="_from", argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="burn", parameter_name="_ids", argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="burn", parameter_name="_amounts", argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="burn", parameter_name="_data", argument_value=data,
        )
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="_operatorData",
            argument_value=operator_data,
        )
        return (operator, _from, ids, amounts, data, operator_data)

    def call(
        self,
        operator: str,
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
            operator,
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            operator, _from, ids, amounts, data, operator_data
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        operator: str,
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
            operator,
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, amounts, data, operator_data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            operator,
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, amounts, data, operator_data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        operator_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            operator,
            _from,
            ids,
            amounts,
            data,
            operator_data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, amounts, data, operator_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, amounts, data, operator_data
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Token:
    """Wrapper class for Token Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
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

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
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

    owner_of: OwnerOfMethod
    """Constructor-initialized instance of
    :class:`OwnerOfMethod`.
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

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    balance_of_batch: BalanceOfBatchMethod
    """Constructor-initialized instance of
    :class:`BalanceOfBatchMethod`.
    """

    granularity: GranularityMethod
    """Constructor-initialized instance of
    :class:`GranularityMethod`.
    """

    swap: SwapMethod
    """Constructor-initialized instance of
    :class:`SwapMethod`.
    """

    send: SendMethod
    """Constructor-initialized instance of
    :class:`SendMethod`.
    """

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
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
                        middleware["function"], layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address), abi=Token.abi()
        ).functions

        self.creators = CreatorsMethod(
            web3_or_provider, contract_address, functions.creators, validator
        )

        self.get_non_fungible_base_type = GetNonFungibleBaseTypeMethod(
            web3_or_provider,
            contract_address,
            functions.getNonFungibleBaseType,
            validator,
        )

        self.get_non_fungible_index = GetNonFungibleIndexMethod(
            web3_or_provider,
            contract_address,
            functions.getNonFungibleIndex,
            validator,
        )

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize, validator
        )

        self.is_fungible = IsFungibleMethod(
            web3_or_provider, contract_address, functions.isFungible, validator
        )

        self.is_non_fungible = IsNonFungibleMethod(
            web3_or_provider, contract_address, functions.isNonFungible, validator,
        )

        self.is_non_fungible_base_type = IsNonFungibleBaseTypeMethod(
            web3_or_provider,
            contract_address,
            functions.isNonFungibleBaseType,
            validator,
        )

        self.is_non_fungible_item = IsNonFungibleItemMethod(
            web3_or_provider, contract_address, functions.isNonFungibleItem, validator,
        )

        self.max_index = MaxIndexMethod(
            web3_or_provider, contract_address, functions.maxIndex, validator
        )

        self.owner_of = OwnerOfMethod(
            web3_or_provider, contract_address, functions.ownerOf, validator
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

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.balance_of_batch = BalanceOfBatchMethod(
            web3_or_provider, contract_address, functions.balanceOfBatch, validator,
        )

        self.granularity = GranularityMethod(
            web3_or_provider, contract_address, functions.granularity
        )

        self.swap = SwapMethod(
            web3_or_provider, contract_address, functions.swap, validator
        )

        self.send = SendMethod(
            web3_or_provider, contract_address, functions.send, validator
        )

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

    def get_token_burned_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokenBurned event.

        :param tx_hash: hash of transaction emitting TokenBurned event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Token.abi(),
            )
            .events.TokenBurned()
            .processReceipt(tx_receipt)
        )

    def get_token_created_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokenCreated event.

        :param tx_hash: hash of transaction emitting TokenCreated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Token.abi(),
            )
            .events.TokenCreated()
            .processReceipt(tx_receipt)
        )

    def get_token_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokenMinted event.

        :param tx_hash: hash of transaction emitting TokenMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Token.abi(),
            )
            .events.TokenMinted()
            .processReceipt(tx_receipt)
        )

    def get_token_sent_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokenSent event.

        :param tx_hash: hash of transaction emitting TokenSent event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Token.abi(),
            )
            .events.TokenSent()
            .processReceipt(tx_receipt)
        )

    def get_token_uri_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokenURI event.

        :param tx_hash: hash of transaction emitting TokenURI event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address), abi=Token.abi(),
            )
            .events.TokenURI()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"uint256","name":"_granularity","type":"uint256"},{"internalType":"address","name":"_1820Registry","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"operatorData","type":"bytes"}],"name":"TokenBurned","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"creator","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"TokenCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"TokenMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"operatorData","type":"bytes"}],"name":"TokenSent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"TokenURI","type":"event"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"creators","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getNonFungibleBaseType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getNonFungibleIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isFungible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungibleBaseType","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungibleItem","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"maxIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"string","name":"_uri","type":"string"},{"internalType":"bool","name":"_isNF","type":"bool"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"create","outputs":[{"internalType":"uint256","name":"type_","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"address[]","name":"_to","type":"address[]"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"mintFungible","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"address[]","name":"_to","type":"address[]"},{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"mintNonFungible","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address[]","name":"_owners","type":"address[]"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"balances_","type":"uint256[]"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[],"name":"granularity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function","constant":true},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"address","name":"_signer","type":"address"},{"components":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256[]","name":"senderTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"senderTokenAmounts","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"signerTokenAmounts","type":"uint256[]"}],"internalType":"struct SwapLib.Swap","name":"_swap","type":"tuple"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"send","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_operatorData","type":"bytes"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
