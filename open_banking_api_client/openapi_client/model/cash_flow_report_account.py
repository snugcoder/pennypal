"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.cash_flow_cash_flow_balance import CashFlowCashFlowBalance
    from openapi_client.model.cash_flow_cash_flow_characteristic import CashFlowCashFlowCharacteristic
    from openapi_client.model.cash_flow_cash_flow_credit import CashFlowCashFlowCredit
    from openapi_client.model.cash_flow_cash_flow_debit import CashFlowCashFlowDebit
    from openapi_client.model.report_transaction import ReportTransaction
    globals()['CashFlowCashFlowBalance'] = CashFlowCashFlowBalance
    globals()['CashFlowCashFlowCharacteristic'] = CashFlowCashFlowCharacteristic
    globals()['CashFlowCashFlowCredit'] = CashFlowCashFlowCredit
    globals()['CashFlowCashFlowDebit'] = CashFlowCashFlowDebit
    globals()['ReportTransaction'] = ReportTransaction


class CashFlowReportAccount(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (int,),  # noqa: E501
            'owner_name': (str,),  # noqa: E501
            'owner_address': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'number': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'aggregation_status_code': (int,),  # noqa: E501
            'current_balance': (float,),  # noqa: E501
            'available_balance': (float,),  # noqa: E501
            'balance_date': (int,),  # noqa: E501
            'transactions': ([ReportTransaction],),  # noqa: E501
            'cash_flow_balance': (CashFlowCashFlowBalance,),  # noqa: E501
            'cash_flow_credit': (CashFlowCashFlowCredit,),  # noqa: E501
            'cash_flow_debit': (CashFlowCashFlowDebit,),  # noqa: E501
            'cash_flow_characteristic': (CashFlowCashFlowCharacteristic,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'owner_name': 'ownerName',  # noqa: E501
        'owner_address': 'ownerAddress',  # noqa: E501
        'name': 'name',  # noqa: E501
        'number': 'number',  # noqa: E501
        'type': 'type',  # noqa: E501
        'aggregation_status_code': 'aggregationStatusCode',  # noqa: E501
        'current_balance': 'currentBalance',  # noqa: E501
        'available_balance': 'availableBalance',  # noqa: E501
        'balance_date': 'balanceDate',  # noqa: E501
        'transactions': 'transactions',  # noqa: E501
        'cash_flow_balance': 'cashFlowBalance',  # noqa: E501
        'cash_flow_credit': 'cashFlowCredit',  # noqa: E501
        'cash_flow_debit': 'cashFlowDebit',  # noqa: E501
        'cash_flow_characteristic': 'cashFlowCharacteristic',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CashFlowReportAccount - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): Finicity account ID. [optional]  # noqa: E501
            owner_name (str): The name(s) of the account owner(s), retrieved from the institution.. [optional]  # noqa: E501
            owner_address (str): The mailing address of the account owner, retrieved from the institution.. [optional]  # noqa: E501
            name (str): The account name from the institution. [optional]  # noqa: E501
            number (str): The account number from the institution (obfuscated). [optional]  # noqa: E501
            type (str): CFR: `ALL` (`checking` / `savings` / `loan` / `mortgage` / `credit card` / `CD` / `MM` / `investment`...). [optional]  # noqa: E501
            aggregation_status_code (int): The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable). [optional]  # noqa: E501
            current_balance (float): The cleared balance of the account as-of `balanceDate`. [optional]  # noqa: E501
            available_balance (float): Available balance. [optional]  # noqa: E501
            balance_date (int): A timestamp showing when the `balance` was captured. [optional]  # noqa: E501
            transactions ([ReportTransaction]): a list of transaction records. [optional]  # noqa: E501
            cash_flow_balance (CashFlowCashFlowBalance): [optional]  # noqa: E501
            cash_flow_credit (CashFlowCashFlowCredit): [optional]  # noqa: E501
            cash_flow_debit (CashFlowCashFlowDebit): [optional]  # noqa: E501
            cash_flow_characteristic (CashFlowCashFlowCharacteristic): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """CashFlowReportAccount - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): Finicity account ID. [optional]  # noqa: E501
            owner_name (str): The name(s) of the account owner(s), retrieved from the institution.. [optional]  # noqa: E501
            owner_address (str): The mailing address of the account owner, retrieved from the institution.. [optional]  # noqa: E501
            name (str): The account name from the institution. [optional]  # noqa: E501
            number (str): The account number from the institution (obfuscated). [optional]  # noqa: E501
            type (str): CFR: `ALL` (`checking` / `savings` / `loan` / `mortgage` / `credit card` / `CD` / `MM` / `investment`...). [optional]  # noqa: E501
            aggregation_status_code (int): The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable). [optional]  # noqa: E501
            current_balance (float): The cleared balance of the account as-of `balanceDate`. [optional]  # noqa: E501
            available_balance (float): Available balance. [optional]  # noqa: E501
            balance_date (int): A timestamp showing when the `balance` was captured. [optional]  # noqa: E501
            transactions ([ReportTransaction]): a list of transaction records. [optional]  # noqa: E501
            cash_flow_balance (CashFlowCashFlowBalance): [optional]  # noqa: E501
            cash_flow_credit (CashFlowCashFlowCredit): [optional]  # noqa: E501
            cash_flow_debit (CashFlowCashFlowDebit): [optional]  # noqa: E501
            cash_flow_characteristic (CashFlowCashFlowCharacteristic): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
