"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.created_customer import CreatedCustomer
from openapi_client.model.customer import Customer
from openapi_client.model.customer_update import CustomerUpdate
from openapi_client.model.customer_with_app_data import CustomerWithAppData
from openapi_client.model.customers import Customers
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.new_customer import NewCustomer


class CustomersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_customer_endpoint = _Endpoint(
            settings={
                'response_type': (CreatedCustomer,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v2/customers/active',
                'operation_id': 'add_customer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'new_customer',
                ],
                'required': [
                    'new_customer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'new_customer':
                        (NewCustomer,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'new_customer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.add_testing_customer_endpoint = _Endpoint(
            settings={
                'response_type': (CreatedCustomer,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v2/customers/testing',
                'operation_id': 'add_testing_customer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'new_customer',
                ],
                'required': [
                    'new_customer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'new_customer':
                        (NewCustomer,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'new_customer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_customer_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}',
                'operation_id': 'delete_customer',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                ],
                'required': [
                    'customer_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                },
                'location_map': {
                    'customer_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_customer_endpoint = _Endpoint(
            settings={
                'response_type': (Customer,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}',
                'operation_id': 'get_customer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                ],
                'required': [
                    'customer_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                },
                'location_map': {
                    'customer_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_customer_with_app_data_endpoint = _Endpoint(
            settings={
                'response_type': (CustomerWithAppData,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/application',
                'operation_id': 'get_customer_with_app_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                ],
                'required': [
                    'customer_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                },
                'location_map': {
                    'customer_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_customers_endpoint = _Endpoint(
            settings={
                'response_type': (Customers,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers',
                'operation_id': 'get_customers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'username',
                    'type',
                    'search',
                    'start',
                    'limit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 1000,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'username':
                        (str,),
                    'type':
                        (str,),
                    'search':
                        (str,),
                    'start':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'username': 'username',
                    'type': 'type',
                    'search': 'search',
                    'start': 'start',
                    'limit': 'limit',
                },
                'location_map': {
                    'username': 'query',
                    'type': 'query',
                    'search': 'query',
                    'start': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.modify_customer_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}',
                'operation_id': 'modify_customer',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'customer_update',
                ],
                'required': [
                    'customer_id',
                    'customer_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'customer_update':
                        (CustomerUpdate,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'customer_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def add_customer(
        self,
        new_customer,
        **kwargs
    ):
        """Add Customer  # noqa: E501

        Enroll an active customer, which is the actual owner of one or more real-world accounts. This is a billable customer.  Active customers must use the \"FinBank Billable\" profiles for testing purposes.   _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_customer(new_customer, async_req=True)
        >>> result = thread.get()

        Args:
            new_customer (NewCustomer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreatedCustomer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['new_customer'] = \
            new_customer
        return self.add_customer_endpoint.call_with_http_info(**kwargs)

    def add_testing_customer(
        self,
        new_customer,
        **kwargs
    ):
        """Add Testing Customer  # noqa: E501

        Enroll a testing customer ([Test Drive](https://signup.finicity.com/) accounts).  For using testing customers with FinBank OAuth, you must register a test application with your systems engineer or account manager. Then, use that testing `applicationId` when creating testing customers.  Testing Customers can access FinBank profiles (except \"FinBank Billable\" profiles), and cannot access live financial institutions.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_testing_customer(new_customer, async_req=True)
        >>> result = thread.get()

        Args:
            new_customer (NewCustomer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreatedCustomer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['new_customer'] = \
            new_customer
        return self.add_testing_customer_endpoint.call_with_http_info(**kwargs)

    def delete_customer(
        self,
        customer_id,
        **kwargs
    ):
        """Delete Customer by ID  # noqa: E501

        Completely remove a customer from the system. This will remove the customer and all associated accounts and transactions.  ⚠️ Use this service carefully! It will not pause for confirmation before performing the operation!  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_customer(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['customer_id'] = \
            customer_id
        return self.delete_customer_endpoint.call_with_http_info(**kwargs)

    def get_customer(
        self,
        customer_id,
        **kwargs
    ):
        """Get Customer by ID  # noqa: E501

        Retrieve a customer by ID.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customer(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Customer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['customer_id'] = \
            customer_id
        return self.get_customer_endpoint.call_with_http_info(**kwargs)

    def get_customer_with_app_data(
        self,
        customer_id,
        **kwargs
    ):
        """Get Customer With App Data by ID  # noqa: E501

        Retrieve a customer along with additional details about the OAuth application.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customer_with_app_data(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CustomerWithAppData
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['customer_id'] = \
            customer_id
        return self.get_customer_with_app_data_endpoint.call_with_http_info(**kwargs)

    def get_customers(
        self,
        **kwargs
    ):
        """Get Customers  # noqa: E501

        Find all customers enrolled by the current partner, where the search text is found in the customer's username or any combination of `firstName` and `lastName` fields. If no search text is provided, all customers will be returned.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customers(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            username (str): Username for exact match (will return 0 or 1 record). [optional]
            type (str): \"testing\" or \"active\" to return only customers of that type, or leave empty to return all customers. [optional]
            search (str): The text you wish to match. Leave this empty if you wish to return all customers. Must be URL-encoded (see: [Handling Spaces in Queries](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/)).. [optional]
            start (int): Index of the page of results to return. [optional] if omitted the server will use the default value of 1
            limit (int): Maximum number of results per page. [optional] if omitted the server will use the default value of 25
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Customers
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_customers_endpoint.call_with_http_info(**kwargs)

    def modify_customer(
        self,
        customer_id,
        customer_update,
        **kwargs
    ):
        """Modify Customer by ID  # noqa: E501

        Modify an enrolled customer by ID.  You must specify either `firstName`, `lastName`, or both in the request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_customer(customer_id, customer_update, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            customer_update (CustomerUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['customer_id'] = \
            customer_id
        kwargs['customer_update'] = \
            customer_update
        return self.modify_customer_endpoint.call_with_http_info(**kwargs)

