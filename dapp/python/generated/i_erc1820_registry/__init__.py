"""Generated wrapper for IERC1820Registry Solidity contract."""

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
# constructor for IERC1820Registry below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IERC1820RegistryValidator,
    )
except ImportError:

    class IERC1820RegistryValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class SetManagerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setManager method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, new_manager: str):
        """Validate the inputs to the setManager method."""
        self.validator.assert_valid(
            method_name='setManager',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='setManager',
            parameter_name='newManager',
            argument_value=new_manager,
        )
        new_manager = self.validate_and_checksum_address(new_manager)
        return (account, new_manager)

    def call(self, account: str, new_manager: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, new_manager) = self.validate_and_normalize_inputs(account, new_manager)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, new_manager).call(tx_params.as_dict())

    def send_transaction(self, account: str, new_manager: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, new_manager) = self.validate_and_normalize_inputs(account, new_manager)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, new_manager).transact(tx_params.as_dict())

    def build_transaction(self, account: str, new_manager: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, new_manager) = self.validate_and_normalize_inputs(account, new_manager)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, new_manager).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, new_manager: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, new_manager) = self.validate_and_normalize_inputs(account, new_manager)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, new_manager).estimateGas(tx_params.as_dict())

class GetManagerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getManager method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the getManager method."""
        self.validator.assert_valid(
            method_name='getManager',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())

class SetInterfaceImplementerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setInterfaceImplementer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, interface_hash: Union[bytes, str], implementer: str):
        """Validate the inputs to the setInterfaceImplementer method."""
        self.validator.assert_valid(
            method_name='setInterfaceImplementer',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='setInterfaceImplementer',
            parameter_name='interfaceHash',
            argument_value=interface_hash,
        )
        self.validator.assert_valid(
            method_name='setInterfaceImplementer',
            parameter_name='implementer',
            argument_value=implementer,
        )
        implementer = self.validate_and_checksum_address(implementer)
        return (account, interface_hash, implementer)

    def call(self, account: str, interface_hash: Union[bytes, str], implementer: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, interface_hash, implementer) = self.validate_and_normalize_inputs(account, interface_hash, implementer)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, interface_hash, implementer).call(tx_params.as_dict())

    def send_transaction(self, account: str, interface_hash: Union[bytes, str], implementer: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, interface_hash, implementer) = self.validate_and_normalize_inputs(account, interface_hash, implementer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_hash, implementer).transact(tx_params.as_dict())

    def build_transaction(self, account: str, interface_hash: Union[bytes, str], implementer: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, interface_hash, implementer) = self.validate_and_normalize_inputs(account, interface_hash, implementer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_hash, implementer).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, interface_hash: Union[bytes, str], implementer: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, interface_hash, implementer) = self.validate_and_normalize_inputs(account, interface_hash, implementer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_hash, implementer).estimateGas(tx_params.as_dict())

class GetInterfaceImplementerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getInterfaceImplementer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, interface_hash: Union[bytes, str]):
        """Validate the inputs to the getInterfaceImplementer method."""
        self.validator.assert_valid(
            method_name='getInterfaceImplementer',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='getInterfaceImplementer',
            parameter_name='interfaceHash',
            argument_value=interface_hash,
        )
        return (account, interface_hash)

    def call(self, account: str, interface_hash: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, interface_hash) = self.validate_and_normalize_inputs(account, interface_hash)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, interface_hash).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, account: str, interface_hash: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, interface_hash) = self.validate_and_normalize_inputs(account, interface_hash)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_hash).transact(tx_params.as_dict())

    def build_transaction(self, account: str, interface_hash: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, interface_hash) = self.validate_and_normalize_inputs(account, interface_hash)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_hash).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, interface_hash: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, interface_hash) = self.validate_and_normalize_inputs(account, interface_hash)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_hash).estimateGas(tx_params.as_dict())

class InterfaceHashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the interfaceHash method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, interface_name: str):
        """Validate the inputs to the interfaceHash method."""
        self.validator.assert_valid(
            method_name='interfaceHash',
            parameter_name='interfaceName',
            argument_value=interface_name,
        )
        return (interface_name)

    def call(self, interface_name: str, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (interface_name) = self.validate_and_normalize_inputs(interface_name)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(interface_name).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, interface_name: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (interface_name) = self.validate_and_normalize_inputs(interface_name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_name).transact(tx_params.as_dict())

    def build_transaction(self, interface_name: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (interface_name) = self.validate_and_normalize_inputs(interface_name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_name).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, interface_name: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (interface_name) = self.validate_and_normalize_inputs(interface_name)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_name).estimateGas(tx_params.as_dict())

class UpdateErc165CacheMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the updateERC165Cache method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, interface_id: Union[bytes, str]):
        """Validate the inputs to the updateERC165Cache method."""
        self.validator.assert_valid(
            method_name='updateERC165Cache',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='updateERC165Cache',
            parameter_name='interfaceId',
            argument_value=interface_id,
        )
        return (account, interface_id)

    def call(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, interface_id).call(tx_params.as_dict())

    def send_transaction(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).transact(tx_params.as_dict())

    def build_transaction(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).estimateGas(tx_params.as_dict())

class ImplementsErc165InterfaceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the implementsERC165Interface method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, interface_id: Union[bytes, str]):
        """Validate the inputs to the implementsERC165Interface method."""
        self.validator.assert_valid(
            method_name='implementsERC165Interface',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='implementsERC165Interface',
            parameter_name='interfaceId',
            argument_value=interface_id,
        )
        return (account, interface_id)

    def call(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, interface_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).transact(tx_params.as_dict())

    def build_transaction(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).estimateGas(tx_params.as_dict())

class ImplementsErc165InterfaceNoCacheMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the implementsERC165InterfaceNoCache method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, interface_id: Union[bytes, str]):
        """Validate the inputs to the implementsERC165InterfaceNoCache method."""
        self.validator.assert_valid(
            method_name='implementsERC165InterfaceNoCache',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='implementsERC165InterfaceNoCache',
            parameter_name='interfaceId',
            argument_value=interface_id,
        )
        return (account, interface_id)

    def call(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, interface_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).transact(tx_params.as_dict())

    def build_transaction(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, interface_id) = self.validate_and_normalize_inputs(account, interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, interface_id).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IERC1820Registry:
    """Wrapper class for IERC1820Registry Solidity contract."""
    set_manager: SetManagerMethod
    """Constructor-initialized instance of
    :class:`SetManagerMethod`.
    """

    get_manager: GetManagerMethod
    """Constructor-initialized instance of
    :class:`GetManagerMethod`.
    """

    set_interface_implementer: SetInterfaceImplementerMethod
    """Constructor-initialized instance of
    :class:`SetInterfaceImplementerMethod`.
    """

    get_interface_implementer: GetInterfaceImplementerMethod
    """Constructor-initialized instance of
    :class:`GetInterfaceImplementerMethod`.
    """

    interface_hash: InterfaceHashMethod
    """Constructor-initialized instance of
    :class:`InterfaceHashMethod`.
    """

    update_erc165_cache: UpdateErc165CacheMethod
    """Constructor-initialized instance of
    :class:`UpdateErc165CacheMethod`.
    """

    implements_erc165_interface: ImplementsErc165InterfaceMethod
    """Constructor-initialized instance of
    :class:`ImplementsErc165InterfaceMethod`.
    """

    implements_erc165_interface_no_cache: ImplementsErc165InterfaceNoCacheMethod
    """Constructor-initialized instance of
    :class:`ImplementsErc165InterfaceNoCacheMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IERC1820RegistryValidator = None,
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
            validator = IERC1820RegistryValidator(web3_or_provider, contract_address)

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

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=IERC1820Registry.abi()).functions

        self.set_manager = SetManagerMethod(web3_or_provider, contract_address, functions.setManager, validator)

        self.get_manager = GetManagerMethod(web3_or_provider, contract_address, functions.getManager, validator)

        self.set_interface_implementer = SetInterfaceImplementerMethod(web3_or_provider, contract_address, functions.setInterfaceImplementer, validator)

        self.get_interface_implementer = GetInterfaceImplementerMethod(web3_or_provider, contract_address, functions.getInterfaceImplementer, validator)

        self.interface_hash = InterfaceHashMethod(web3_or_provider, contract_address, functions.interfaceHash, validator)

        self.update_erc165_cache = UpdateErc165CacheMethod(web3_or_provider, contract_address, functions.updateERC165Cache, validator)

        self.implements_erc165_interface = ImplementsErc165InterfaceMethod(web3_or_provider, contract_address, functions.implementsERC165Interface, validator)

        self.implements_erc165_interface_no_cache = ImplementsErc165InterfaceNoCacheMethod(web3_or_provider, contract_address, functions.implementsERC165InterfaceNoCache, validator)

    def get_interface_implementer_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for InterfaceImplementerSet event.

        :param tx_hash: hash of transaction emitting InterfaceImplementerSet
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=IERC1820Registry.abi()).events.InterfaceImplementerSet().processReceipt(tx_receipt)
    def get_manager_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ManagerChanged event.

        :param tx_hash: hash of transaction emitting ManagerChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=IERC1820Registry.abi()).events.ManagerChanged().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"bytes32","name":"interfaceHash","type":"bytes32"},{"indexed":true,"internalType":"address","name":"implementer","type":"address"}],"name":"InterfaceImplementerSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"newManager","type":"address"}],"name":"ManagerChanged","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"newManager","type":"address"}],"name":"setManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getManager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"interfaceHash","type":"bytes32"},{"internalType":"address","name":"implementer","type":"address"}],"name":"setInterfaceImplementer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"interfaceHash","type":"bytes32"}],"name":"getInterfaceImplementer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"interfaceName","type":"string"}],"name":"interfaceHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"updateERC165Cache","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"implementsERC165Interface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"implementsERC165InterfaceNoCache","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
