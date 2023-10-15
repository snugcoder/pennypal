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
from openapi_client.model.report import Report
from openapi_client.model.report_summaries import ReportSummaries


class ReportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_report_by_consumer_endpoint = _Endpoint(
            settings={
                'response_type': (Report,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v3/consumers/{consumerId}/reports/{reportId}',
                'operation_id': 'get_report_by_consumer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'consumer_id',
                    'report_id',
                    'purpose',
                    'on_behalf_of',
                ],
                'required': [
                    'consumer_id',
                    'report_id',
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
                    'consumer_id':
                        (str,),
                    'report_id':
                        (str,),
                    'purpose':
                        (str,),
                    'on_behalf_of':
                        (str,),
                },
                'attribute_map': {
                    'consumer_id': 'consumerId',
                    'report_id': 'reportId',
                    'purpose': 'purpose',
                    'on_behalf_of': 'onBehalfOf',
                },
                'location_map': {
                    'consumer_id': 'path',
                    'report_id': 'path',
                    'purpose': 'query',
                    'on_behalf_of': 'query',
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
        self.get_report_by_customer_endpoint = _Endpoint(
            settings={
                'response_type': (Report,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v3/customers/{customerId}/reports/{reportId}',
                'operation_id': 'get_report_by_customer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'report_id',
                    'on_behalf_of',
                    'purpose',
                ],
                'required': [
                    'customer_id',
                    'report_id',
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
                    'report_id':
                        (str,),
                    'on_behalf_of':
                        (str,),
                    'purpose':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'report_id': 'reportId',
                    'on_behalf_of': 'onBehalfOf',
                    'purpose': 'purpose',
                },
                'location_map': {
                    'customer_id': 'path',
                    'report_id': 'path',
                    'on_behalf_of': 'query',
                    'purpose': 'query',
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
        self.get_reports_by_consumer_id_endpoint = _Endpoint(
            settings={
                'response_type': (ReportSummaries,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v1/consumers/{consumerId}/reports',
                'operation_id': 'get_reports_by_consumer_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'consumer_id',
                    'purpose',
                ],
                'required': [
                    'consumer_id',
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
                    'consumer_id':
                        (str,),
                    'purpose':
                        (str,),
                },
                'attribute_map': {
                    'consumer_id': 'consumerId',
                    'purpose': 'purpose',
                },
                'location_map': {
                    'consumer_id': 'path',
                    'purpose': 'query',
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
        self.get_reports_by_customer_id_endpoint = _Endpoint(
            settings={
                'response_type': (ReportSummaries,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v1/customers/{customerId}/reports',
                'operation_id': 'get_reports_by_customer_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'purpose',
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
                    'purpose':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'purpose': 'purpose',
                },
                'location_map': {
                    'customer_id': 'path',
                    'purpose': 'query',
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

    def get_report_by_consumer(
        self,
        consumer_id,
        report_id,
        **kwargs
    ):
        """Get Report by Consumer and ID  # noqa: E501

        Get a report that has been generated by a previous call to one of the Generate Report services.  The report's `status` field contains \"inProgress\", \"failure\", or \"success\". If the status shows \"inProgress\", the client app should wait 20 seconds and then call this API again.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_report_by_consumer(consumer_id, report_id, async_req=True)
        >>> result = thread.get()

        Args:
            consumer_id (str): The consumer ID
            report_id (str): ID of the report

        Keyword Args:
            purpose (str): 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.. [optional]
            on_behalf_of (str): The name of the entity you are retrieving the report on behalf of. [optional]
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
            Report
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
        kwargs['consumer_id'] = \
            consumer_id
        kwargs['report_id'] = \
            report_id
        return self.get_report_by_consumer_endpoint.call_with_http_info(**kwargs)

    def get_report_by_customer(
        self,
        customer_id,
        report_id,
        **kwargs
    ):
        """Get Report by Customer and ID  # noqa: E501

        Get a report that has been generated by a previous call to one of the Generate Report services.  The report's `status` field contains \"inProgress\", \"failure\", or \"success\". If the status shows \"inProgress\", the client app should wait 20 seconds and then call this API again.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_report_by_customer(customer_id, report_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            report_id (str): ID of the report

        Keyword Args:
            on_behalf_of (str): The name of the entity you are retrieving the report on behalf of. [optional]
            purpose (str): 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.. [optional]
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
            Report
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
        kwargs['report_id'] = \
            report_id
        return self.get_report_by_customer_endpoint.call_with_http_info(**kwargs)

    def get_reports_by_consumer_id(
        self,
        consumer_id,
        **kwargs
    ):
        """Get Reports by Consumer ID  # noqa: E501

        Get all reports that have been generated by previous calls to Generate Report services for the given consumer.  The `status` fields in the returned list contain \"inProgress\", \"failure\", or \"success\". If the status shows \"inProgress\", the client app should wait 20 seconds and then call this API again.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_reports_by_consumer_id(consumer_id, async_req=True)
        >>> result = thread.get()

        Args:
            consumer_id (str): The consumer ID

        Keyword Args:
            purpose (str): 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.. [optional]
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
            ReportSummaries
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
        kwargs['consumer_id'] = \
            consumer_id
        return self.get_reports_by_consumer_id_endpoint.call_with_http_info(**kwargs)

    def get_reports_by_customer_id(
        self,
        customer_id,
        **kwargs
    ):
        """Get Reports by Customer ID  # noqa: E501

        Get all reports that have been generated by previous calls to Generate Report services for the given customer.  The `status` fields in the returned list contain \"inProgress\", \"failure\", or \"success\". If the status shows \"inProgress\", the client app should wait 20 seconds and then call this API again.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_reports_by_customer_id(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID

        Keyword Args:
            purpose (str): 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.. [optional]
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
            ReportSummaries
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
        return self.get_reports_by_customer_id_endpoint.call_with_http_info(**kwargs)

