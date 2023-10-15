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
from openapi_client.model.created_test_tx_push_transaction import CreatedTestTxPushTransaction
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.test_tx_push_transaction import TestTxPushTransaction
from openapi_client.model.tx_push_subscription_parameters import TxPushSubscriptionParameters
from openapi_client.model.tx_push_subscriptions import TxPushSubscriptions


class TxPushApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_tx_push_test_transaction_endpoint = _Endpoint(
            settings={
                'response_type': (CreatedTestTxPushTransaction,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions',
                'operation_id': 'create_tx_push_test_transaction',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                    'test_tx_push_transaction',
                ],
                'required': [
                    'customer_id',
                    'account_id',
                    'test_tx_push_transaction',
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
                    'test_tx_push_transaction':
                        (TestTxPushTransaction,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
                    'test_tx_push_transaction': 'body',
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
        self.delete_tx_push_subscription_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}',
                'operation_id': 'delete_tx_push_subscription',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'subscription_id',
                ],
                'required': [
                    'customer_id',
                    'subscription_id',
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
                    'subscription_id':
                        (int,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'subscription_id': 'subscriptionId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'subscription_id': 'path',
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
        self.disable_tx_push_notifications_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush',
                'operation_id': 'disable_tx_push_notifications',
                'http_method': 'DELETE',
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
        self.subscribe_to_tx_push_notifications_endpoint = _Endpoint(
            settings={
                'response_type': (TxPushSubscriptions,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush',
                'operation_id': 'subscribe_to_tx_push_notifications',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'account_id',
                    'tx_push_subscription_parameters',
                ],
                'required': [
                    'customer_id',
                    'account_id',
                    'tx_push_subscription_parameters',
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
                    'tx_push_subscription_parameters':
                        (TxPushSubscriptionParameters,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'account_id': 'accountId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'account_id': 'path',
                    'tx_push_subscription_parameters': 'body',
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

    def create_tx_push_test_transaction(
        self,
        customer_id,
        account_id,
        test_tx_push_transaction,
        **kwargs
    ):
        """Create TxPush Test Transaction  # noqa: E501

        Inject a transaction into the transaction list for a testing account. This allows an app to trigger TxPush notifications for the account in order to test the app's TxPush Listener service. This causes the platform to send one transaction event and one account event (showing that the account balance has changed). This service is only supported for testing accounts.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_tx_push_test_transaction(customer_id, account_id, test_tx_push_transaction, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID
            test_tx_push_transaction (TestTxPushTransaction):

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
            CreatedTestTxPushTransaction
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
        kwargs['test_tx_push_transaction'] = \
            test_tx_push_transaction
        return self.create_tx_push_test_transaction_endpoint.call_with_http_info(**kwargs)

    def delete_tx_push_subscription(
        self,
        customer_id,
        subscription_id,
        **kwargs
    ):
        """Delete TxPush Subscription  # noqa: E501

        Delete a specific subscription to TxPush notifications for the given account. This could be individual deleting the account or transactions events. No more events will be sent for that specific subscription.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_tx_push_subscription(customer_id, subscription_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            subscription_id (int): The subscription ID

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
        kwargs['subscription_id'] = \
            subscription_id
        return self.delete_tx_push_subscription_endpoint.call_with_http_info(**kwargs)

    def disable_tx_push_notifications(
        self,
        customer_id,
        account_id,
        **kwargs
    ):
        """Disable TxPush Notifications  # noqa: E501

        Delete all TxPush subscriptions with their notifications for the given account. No more notifications will be sent for account or transaction events.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_tx_push_notifications(customer_id, account_id, async_req=True)
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
        return self.disable_tx_push_notifications_endpoint.call_with_http_info(**kwargs)

    def subscribe_to_tx_push_notifications(
        self,
        customer_id,
        account_id,
        tx_push_subscription_parameters,
        **kwargs
    ):
        """Subscribe to TxPush Notifications  # noqa: E501

        Register a client app's TxPush Listener to receive TxPush notifications related to the given account.  Each call to this service will return two records, one with class account and one with class transaction. Account events are sent when values change in the account's fields (such as `balance` or `interestRate`). Transaction events are sent whenever a new transaction is posted for the account. For institutions that do not provide TxPush services, notifications are sent as soon as Finicity finds a new transaction or new account data through regular aggregation processes.  The listener's URL must be secure (HTTPS) for any real-world account. In addition, the client's TxPush Listener will need to be verified. HTTP and HTTPS connections are only allowed on the standard ports 80 (HTTP) and 443 (HTTPS). The use of other ports will result with the call failing.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscribe_to_tx_push_notifications(customer_id, account_id, tx_push_subscription_parameters, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            account_id (str): The account ID
            tx_push_subscription_parameters (TxPushSubscriptionParameters):

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
            TxPushSubscriptions
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
        kwargs['tx_push_subscription_parameters'] = \
            tx_push_subscription_parameters
        return self.subscribe_to_tx_push_notifications_endpoint.call_with_http_info(**kwargs)

