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
from openapi_client.model.cash_flow_report_ack import CashFlowReportAck
from openapi_client.model.cash_flow_report_constraints import CashFlowReportConstraints
from openapi_client.model.error_message import ErrorMessage


class CashFlowApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.generate_cash_flow_business_report_endpoint = _Endpoint(
            settings={
                'response_type': (CashFlowReportAck,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v2/customers/{customerId}/cashFlowBusiness',
                'operation_id': 'generate_cash_flow_business_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'cash_flow_report_constraints',
                    'callback_url',
                ],
                'required': [
                    'customer_id',
                    'cash_flow_report_constraints',
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
                    'cash_flow_report_constraints':
                        (CashFlowReportConstraints,),
                    'callback_url':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'callback_url': 'callbackUrl',
                },
                'location_map': {
                    'customer_id': 'path',
                    'cash_flow_report_constraints': 'body',
                    'callback_url': 'query',
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
        self.generate_cash_flow_personal_report_endpoint = _Endpoint(
            settings={
                'response_type': (CashFlowReportAck,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/decisioning/v2/customers/{customerId}/cashFlowPersonal',
                'operation_id': 'generate_cash_flow_personal_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'cash_flow_report_constraints',
                    'callback_url',
                ],
                'required': [
                    'customer_id',
                    'cash_flow_report_constraints',
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
                    'cash_flow_report_constraints':
                        (CashFlowReportConstraints,),
                    'callback_url':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'callback_url': 'callbackUrl',
                },
                'location_map': {
                    'customer_id': 'path',
                    'cash_flow_report_constraints': 'body',
                    'callback_url': 'query',
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

    def generate_cash_flow_business_report(
        self,
        customer_id,
        cash_flow_report_constraints,
        **kwargs
    ):
        """Generate Cash Flow Report - Business  # noqa: E501

        Generate a Cash Flow Report (Business) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report. A consumer is not required to generate this report.  This report is not provided under FCRA rules, and this report is not available in the Finicity Consumer Portal for the borrower to view.  If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_cash_flow_business_report(customer_id, cash_flow_report_constraints, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            cash_flow_report_constraints (CashFlowReportConstraints):

        Keyword Args:
            callback_url (str): A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.. [optional]
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
            CashFlowReportAck
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
        kwargs['cash_flow_report_constraints'] = \
            cash_flow_report_constraints
        return self.generate_cash_flow_business_report_endpoint.call_with_http_info(**kwargs)

    def generate_cash_flow_personal_report(
        self,
        customer_id,
        cash_flow_report_constraints,
        **kwargs
    ):
        """Generate Cash Flow Report - Personal  # noqa: E501

        Generate a Cash Flow Report (Personal) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report.  This report is provided under FCRA rules, with Finicity acting as the CRA (Consumer Reporting Agency). If an individual account is included in the report - for example, with an individual acting as an personal guarantor on the loan - then this version of the report should be used. In case of an adverse action on the loan where the decision was based on this report, then the borrower can be referred to the [Finicity Consumer Portal](https://consumer.finicityreports.com) where they can view this report and submit a dispute if they feel any information in this report is inaccurate.  Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_cash_flow_personal_report(customer_id, cash_flow_report_constraints, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): A customer ID
            cash_flow_report_constraints (CashFlowReportConstraints):

        Keyword Args:
            callback_url (str): A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.. [optional]
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
            CashFlowReportAck
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
        kwargs['cash_flow_report_constraints'] = \
            cash_flow_report_constraints
        return self.generate_cash_flow_personal_report_endpoint.call_with_http_info(**kwargs)

