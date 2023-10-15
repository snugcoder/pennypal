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
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.transaction import Transaction
from openapi_client.model.transactions import Transactions
from openapi_client.model.transactions_report_ack import TransactionsReportAck
from openapi_client.model.transactions_report_constraints import TransactionsReportConstraints


class TransactionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.generate_transactions_report_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionsReportAck,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v2/customers/{customerId}/transactions',
                'operation_id': 'generate_transactions_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'to_date',
                    'transactions_report_constraints',
                    'callback_url',
                    'include_pending',
                ],
                'required': [
                    'customer_id',
                    'to_date',
                    'transactions_report_constraints',
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
                    'to_date':
                        (int,),
                    'transactions_report_constraints':
                        (TransactionsReportConstraints,),
                    'callback_url':
                        (str,),
                    'include_pending':
                        (bool,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'to_date': 'toDate',
                    'callback_url': 'callbackUrl',
                    'include_pending': 'includePending',
                },
                'location_map': {
                    'customer_id': 'path',
                    'to_date': 'query',
                    'transactions_report_constraints': 'body',
                    'callback_url': 'query',
                    'include_pending': 'query',
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
        self.get_all_customer_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (Transactions,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v3/customers/{customerId}/transactions',
                'operation_id': 'get_all_customer_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'from_date',
                    'to_date',
                    'start',
                    'limit',
                    'sort',
                    'include_pending',
                ],
                'required': [
                    'customer_id',
                    'from_date',
                    'to_date',
                ],
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
                    'customer_id':
                        (str,),
                    'from_date':
                        (int,),
                    'to_date':
                        (int,),
                    'start':
                        (int,),
                    'limit':
                        (int,),
                    'sort':
                        (str,),
                    'include_pending':
                        (bool,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'start': 'start',
                    'limit': 'limit',
                    'sort': 'sort',
                    'include_pending': 'includePending',
                },
                'location_map': {
                    'customer_id': 'path',
                    'from_date': 'query',
                    'to_date': 'query',
                    'start': 'query',
                    'limit': 'query',
                    'sort': 'query',
                    'include_pending': 'query',
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
        self.get_customer_account_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (Transactions,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v4/customers/{customerId}/accounts/{accountId}/transactions',
                'operation_id': 'get_customer_account_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                    'from_date',
                    'to_date',
                    'start',
                    'limit',
                    'sort',
                    'include_pending',
                ],
                'required': [
                    'customer_id',
                    'account_id',
                    'from_date',
                    'to_date',
                ],
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
                    'customer_id':
                        (str,),
                    'account_id':
                        (str,),
                    'from_date':
                        (int,),
                    'to_date':
                        (int,),
                    'start':
                        (int,),
                    'limit':
                        (int,),
                    'sort':
                        (str,),
                    'include_pending':
                        (bool,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'start': 'start',
                    'limit': 'limit',
                    'sort': 'sort',
                    'include_pending': 'includePending',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
                    'from_date': 'query',
                    'to_date': 'query',
                    'start': 'query',
                    'limit': 'query',
                    'sort': 'query',
                    'include_pending': 'query',
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
        self.get_customer_transaction_endpoint = _Endpoint(
            settings={
                'response_type': (Transaction,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v2/customers/{customerId}/transactions/{transactionId}',
                'operation_id': 'get_customer_transaction',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'transaction_id',
                ],
                'required': [
                    'customer_id',
                    'transaction_id',
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
                    'transaction_id':
                        (int,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'transaction_id': 'transactionId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'transaction_id': 'path',
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
        self.load_historic_transactions_for_customer_account_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic',
                'operation_id': 'load_historic_transactions_for_customer_account',
                'http_method': 'POST',
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

    def generate_transactions_report(
        self,
        customer_id,
        to_date,
        transactions_report_constraints,
        **kwargs
    ):
        """Generate Transactions Report  # noqa: E501

        Generate a Transaction Report for the given accounts under the given customer. This service retrieves up to 24 months of transaction history for the given customer. It then uses this information to generate the Transaction Report.  This is a premium service. A billable event will be created upon the successful generation of the Transactions Report.   Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  There cannot be more than 24 months between `fromDate` and `toDate`.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_transactions_report(customer_id, to_date, transactions_report_constraints, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            to_date (int): A end date
            transactions_report_constraints (TransactionsReportConstraints):

        Keyword Args:
            callback_url (str): A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.. [optional]
            include_pending (bool): If pending transactions must be included. [optional] if omitted the server will use the default value of False
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
            TransactionsReportAck
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
        kwargs['to_date'] = \
            to_date
        kwargs['transactions_report_constraints'] = \
            transactions_report_constraints
        return self.generate_transactions_report_endpoint.call_with_http_info(**kwargs)

    def get_all_customer_transactions(
        self,
        customer_id,
        from_date,
        to_date,
        **kwargs
    ):
        """Get All Customer Transactions  # noqa: E501

        Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.  Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the service Load Historic Transactions for Account.  There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_customer_transactions(customer_id, from_date, to_date, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            from_date (int): A start date
            to_date (int): A end date

        Keyword Args:
            start (int): Index of the page of results to return. [optional] if omitted the server will use the default value of 1
            limit (int): Maximum number of results per page. [optional] if omitted the server will use the default value of 25
            sort (str): Date sort order: \"asc\" for ascending, \"desc\" for descending. [optional] if omitted the server will use the default value of "desc"
            include_pending (bool): If pending transactions must be included. [optional] if omitted the server will use the default value of False
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
            Transactions
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
        kwargs['from_date'] = \
            from_date
        kwargs['to_date'] = \
            to_date
        return self.get_all_customer_transactions_endpoint.call_with_http_info(**kwargs)

    def get_customer_account_transactions(
        self,
        customer_id,
        account_id,
        from_date,
        to_date,
        **kwargs
    ):
        """Get Customer Account Transactions  # noqa: E501

        Get all transactions available for this customer account within the given date range. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.  Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.  There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customer_account_transactions(customer_id, account_id, from_date, to_date, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID
            from_date (int): A start date
            to_date (int): A end date

        Keyword Args:
            start (int): Index of the page of results to return. [optional] if omitted the server will use the default value of 1
            limit (int): Maximum number of results per page. [optional] if omitted the server will use the default value of 25
            sort (str): Date sort order: \"asc\" for ascending, \"desc\" for descending. [optional] if omitted the server will use the default value of "desc"
            include_pending (bool): If pending transactions must be included. [optional] if omitted the server will use the default value of False
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
            Transactions
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
        kwargs['from_date'] = \
            from_date
        kwargs['to_date'] = \
            to_date
        return self.get_customer_account_transactions_endpoint.call_with_http_info(**kwargs)

    def get_customer_transaction(
        self,
        customer_id,
        transaction_id,
        **kwargs
    ):
        """Get Customer Transaction by ID  # noqa: E501

        Get details for the given transaction.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customer_transaction(customer_id, transaction_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            transaction_id (int): A transaction ID

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
            Transaction
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
        kwargs['transaction_id'] = \
            transaction_id
        return self.get_customer_transaction_endpoint.call_with_http_info(**kwargs)

    def load_historic_transactions_for_customer_account(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Load Historic Transactions for Customer Account  # noqa: E501

        Connect to the account's financial institution and load up to 24 months of historic transactions for the account. Length of history varies by institution.  This is a premium service. The billable event is a call to this service specifying a customer ID that has not been seen before by this service. (If this service is called multiple times with the same customer ID, to load transactions from multiple accounts, only one billable event has occurred.)  The recommended timeout setting for this request is 180 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.  The date range sent to the institution is calculated from the account's `createdDate`. This means that calling this service a second time for the same account normally will not add any new transactions for the account. For this reason, a second call to this service for a known account ID will usually return immediately.  In a few specific scenarios, it may be desirable to force a second connection to the institution for a known account ID. Some examples are:  * The institution's policy has changed, making more transactions available * Finicity has now added a longer transaction history support for the institution * The first call encountered an error, and the resulting Aggregation Ticket has now been fixed by the Finicity Support Team  In these cases, the POST request can contain the parameter `force=true` in the request body to force the second connection.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.load_historic_transactions_for_customer_account(customer_id, account_id, async_req=True)
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
        kwargs['account_id'] = \
            account_id
        return self.load_historic_transactions_for_customer_account_endpoint.call_with_http_info(**kwargs)
