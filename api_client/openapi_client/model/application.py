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



class Application(ModelNormal):
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
        return {
            'app_description': (str,),  # noqa: E501
            'app_name': (str,),  # noqa: E501
            'app_url': (str,),  # noqa: E501
            'owner_address_line1': (str,),  # noqa: E501
            'owner_address_line2': (str,),  # noqa: E501
            'owner_city': (str,),  # noqa: E501
            'owner_country': (str,),  # noqa: E501
            'owner_name': (str,),  # noqa: E501
            'owner_postal_code': (str,),  # noqa: E501
            'owner_state': (str,),  # noqa: E501
            'image': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'app_description': 'appDescription',  # noqa: E501
        'app_name': 'appName',  # noqa: E501
        'app_url': 'appUrl',  # noqa: E501
        'owner_address_line1': 'ownerAddressLine1',  # noqa: E501
        'owner_address_line2': 'ownerAddressLine2',  # noqa: E501
        'owner_city': 'ownerCity',  # noqa: E501
        'owner_country': 'ownerCountry',  # noqa: E501
        'owner_name': 'ownerName',  # noqa: E501
        'owner_postal_code': 'ownerPostalCode',  # noqa: E501
        'owner_state': 'ownerState',  # noqa: E501
        'image': 'image',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, app_description, app_name, app_url, owner_address_line1, owner_address_line2, owner_city, owner_country, owner_name, owner_postal_code, owner_state, image, *args, **kwargs):  # noqa: E501
        """Application - a model defined in OpenAPI

        Args:
            app_description (str): A short description of the app. This will be visible to end users in the FI interface.
            app_name (str): The name of the application assigned to the customer
            app_url (str): An URL for the app. This will be visible to end users in the FI interface.
            owner_address_line1 (str): Address line 1
            owner_address_line2 (str): Address line 2
            owner_city (str): City for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_country (str): Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_name (str): Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_postal_code (str): Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_state (str): State for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            image (str): An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB)

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

        self.app_description = app_description
        self.app_name = app_name
        self.app_url = app_url
        self.owner_address_line1 = owner_address_line1
        self.owner_address_line2 = owner_address_line2
        self.owner_city = owner_city
        self.owner_country = owner_country
        self.owner_name = owner_name
        self.owner_postal_code = owner_postal_code
        self.owner_state = owner_state
        self.image = image
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
    def __init__(self, app_description, app_name, app_url, owner_address_line1, owner_address_line2, owner_city, owner_country, owner_name, owner_postal_code, owner_state, image, *args, **kwargs):  # noqa: E501
        """Application - a model defined in OpenAPI

        Args:
            app_description (str): A short description of the app. This will be visible to end users in the FI interface.
            app_name (str): The name of the application assigned to the customer
            app_url (str): An URL for the app. This will be visible to end users in the FI interface.
            owner_address_line1 (str): Address line 1
            owner_address_line2 (str): Address line 2
            owner_city (str): City for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_country (str): Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_name (str): Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_postal_code (str): Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            owner_state (str): State for the business entity that owns the app. Information for registration purposes only and not given to the end user.
            image (str): An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB)

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

        self.app_description = app_description
        self.app_name = app_name
        self.app_url = app_url
        self.owner_address_line1 = owner_address_line1
        self.owner_address_line2 = owner_address_line2
        self.owner_city = owner_city
        self.owner_country = owner_country
        self.owner_name = owner_name
        self.owner_postal_code = owner_postal_code
        self.owner_state = owner_state
        self.image = image
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
