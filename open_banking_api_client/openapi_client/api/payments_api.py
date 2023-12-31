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
from openapi_client.model.ach_details import ACHDetails
from openapi_client.model.account_owner import AccountOwner
from openapi_client.model.account_owner_holders import AccountOwnerHolders
from openapi_client.model.available_balance import AvailableBalance
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.loan_payment_details import LoanPaymentDetails


class PaymentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_account_ach_details_endpoint = _Endpoint(
            settings={
                'response_type': (ACHDetails,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/details',
                'operation_id': 'get_account_ach_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                ],
                'required': [
                    'customer_id',
                    'account_id',
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
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
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
        self.get_account_owner_endpoint = _Endpoint(
            settings={
                'response_type': (AccountOwner,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/owner',
                'operation_id': 'get_account_owner',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                ],
                'required': [
                    'customer_id',
                    'account_id',
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
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
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
        self.get_account_owner_details_endpoint = _Endpoint(
            settings={
                'response_type': (AccountOwnerHolders,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v3/customers/{customerId}/accounts/{accountId}/owner',
                'operation_id': 'get_account_owner_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                    'with_insights',
                ],
                'required': [
                    'customer_id',
                    'account_id',
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
                    'account_id':
                        (str,),
                    'with_insights':
                        (bool,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                    'with_insights': 'withInsights',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
                    'with_insights': 'query',
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
        self.get_available_balance_endpoint = _Endpoint(
            settings={
                'response_type': (AvailableBalance,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance',
                'operation_id': 'get_available_balance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                ],
                'required': [
                    'customer_id',
                    'account_id',
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
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
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
        self.get_available_balance_live_endpoint = _Endpoint(
            settings={
                'response_type': (AvailableBalance,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance/live',
                'operation_id': 'get_available_balance_live',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                ],
                'required': [
                    'customer_id',
                    'account_id',
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
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
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
        self.get_loan_payment_details_endpoint = _Endpoint(
            settings={
                'response_type': (LoanPaymentDetails,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v2/customers/{customerId}/accounts/{accountId}/loanDetails',
                'operation_id': 'get_loan_payment_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                ],
                'required': [
                    'customer_id',
                    'account_id',
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
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
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

    def get_account_ach_details(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Get Account ACH Details  # noqa: E501

        Return the real account number and routing number details for an ACH payment.  Note: this is a premium service, billable per every successful API call.  _Supported account types_: \"checking\", \"savings\", \"moneyMarket\", \"loan\"  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_ach_details(customer_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID

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
            ACHDetails
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
        kwargs['account_id'] = \
            account_id
        return self.get_account_ach_details_endpoint.call_with_http_info(**kwargs)

    def get_account_owner(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Get Account Owner  # noqa: E501

        Retrieve the names and addresses of the account owner from a financial institution.  Note: this is a premium service, billable per every successful API call.  This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. In the event of a timeout condition, retry the call.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_owner(customer_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID

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
            AccountOwner
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
        kwargs['account_id'] = \
            account_id
        return self.get_account_owner_endpoint.call_with_http_info(**kwargs)

    def get_account_owner_details(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Get Account Owner Details  # noqa: E501

        This service retrieves the account details for an account holder from an institution. The following data objects are available.  * Account holders  * Addresses  * Emails  * Phones  * Documentations  * Identity Insights   Note: The data returned varies from institution to institution as not all of them make the same data available. This is a premium service, billable per each successful API call.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_owner_details(customer_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID

        Keyword Args:
            with_insights (bool): If this parameter is true, Identity Insights data will be returned along with the account owner information. [optional]
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
            AccountOwnerHolders
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
        kwargs['account_id'] = \
            account_id
        return self.get_account_owner_details_endpoint.call_with_http_info(**kwargs)

    def get_available_balance(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Get Available Balance  # noqa: E501

        Retrieve the latest cached available and cleared account balances for a customer. Since we update and store balances throughout the day, this is the most accurate balance information available when a connection to a financial institution is unavailable or when a faster response is needed. Only deposit account types are supported: Checking, Savings, Money Market, and CD.  Note: this is a premium service, billable per every successful API call. Enrollment is required.  _Supported account types_: \"checking\", \"savings\", \"moneyMarket\", \"cd\"  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_balance(customer_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID

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
            AvailableBalance
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
        kwargs['account_id'] = \
            account_id
        return self.get_available_balance_endpoint.call_with_http_info(**kwargs)

    def get_available_balance_live(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Get Available Balance - Live  # noqa: E501

        Retrieve the available and cleared account balances for a single account in real-time directly from a financial institution.  Note: this is a premium service, billable per every successful API call.  _Supported account types_: \"checking\", \"savings\", \"moneyMarket\", \"cd\"  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_balance_live(customer_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID

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
            AvailableBalance
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
        kwargs['account_id'] = \
            account_id
        return self.get_available_balance_live_endpoint.call_with_http_info(**kwargs)

    def get_loan_payment_details(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Get Loan Payment Details  # noqa: E501

        Return the loan payment details of the customer for a loan-type account.  Note: this is a premium service, billable per every successful API call.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_loan_payment_details(customer_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID

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
            LoanPaymentDetails
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
        kwargs['account_id'] = \
            account_id
        return self.get_loan_payment_details_endpoint.call_with_http_info(**kwargs)

