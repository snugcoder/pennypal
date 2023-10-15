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
from openapi_client.model.third_party_access_key_data import ThirdPartyAccessKeyData
from openapi_client.model.third_party_access_key_receipt_data import ThirdPartyAccessKeyReceiptData


class ThirdPartyAccessApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.generate_third_party_access_key_endpoint = _Endpoint(
            settings={
                'response_type': (ThirdPartyAccessKeyReceiptData,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/partners/accessKey',
                'operation_id': 'generate_third_party_access_key',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'third_party_access_key_data',
                ],
                'required': [
                    'third_party_access_key_data',
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
                    'third_party_access_key_data':
                        (ThirdPartyAccessKeyData,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'third_party_access_key_data': 'body',
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
        self.revoke_third_party_access_key_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/partners/accessKey/{consentReceiptId}',
                'operation_id': 'revoke_third_party_access_key',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'consent_receipt_id',
                ],
                'required': [
                    'consent_receipt_id',
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
                    'consent_receipt_id':
                        (str,),
                },
                'attribute_map': {
                    'consent_receipt_id': 'consentReceiptId',
                },
                'location_map': {
                    'consent_receipt_id': 'path',
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
        self.update_third_party_access_key_endpoint = _Endpoint(
            settings={
                'response_type': (ThirdPartyAccessKeyReceiptData,),
                'auth': [
                    'FinicityAppKey',
                    'FinicityAppToken'
                ],
                'endpoint_path': '/aggregation/v1/partners/accessKey/{consentReceiptId}',
                'operation_id': 'update_third_party_access_key',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'consent_receipt_id',
                    'third_party_access_key_data',
                ],
                'required': [
                    'consent_receipt_id',
                    'third_party_access_key_data',
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
                    'consent_receipt_id':
                        (str,),
                    'third_party_access_key_data':
                        (ThirdPartyAccessKeyData,),
                },
                'attribute_map': {
                    'consent_receipt_id': 'consentReceiptId',
                },
                'location_map': {
                    'consent_receipt_id': 'path',
                    'third_party_access_key_data': 'body',
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

    def generate_third_party_access_key(
        self,
        third_party_access_key_data,
        **kwargs
    ):
        """Generate Third Party Access Key  # noqa: E501

        Generate access key for third party partners. A partner can provide access to third party partners with this access key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_third_party_access_key(third_party_access_key_data, async_req=True)
        >>> result = thread.get()

        Args:
            third_party_access_key_data (ThirdPartyAccessKeyData):

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
            ThirdPartyAccessKeyReceiptData
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
        kwargs['third_party_access_key_data'] = \
            third_party_access_key_data
        return self.generate_third_party_access_key_endpoint.call_with_http_info(**kwargs)

    def revoke_third_party_access_key(
        self,
        consent_receipt_id,
        **kwargs
    ):
        """Revoke Third Party Access  # noqa: E501

        Revoke access of third party partners  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.revoke_third_party_access_key(consent_receipt_id, async_req=True)
        >>> result = thread.get()

        Args:
            consent_receipt_id (str): Third party access key receipt ID

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
        kwargs['consent_receipt_id'] = \
            consent_receipt_id
        return self.revoke_third_party_access_key_endpoint.call_with_http_info(**kwargs)

    def update_third_party_access_key(
        self,
        consent_receipt_id,
        third_party_access_key_data,
        **kwargs
    ):
        """Update Third Party Access  # noqa: E501

        Update access for third party partners  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_third_party_access_key(consent_receipt_id, third_party_access_key_data, async_req=True)
        >>> result = thread.get()

        Args:
            consent_receipt_id (str): Third party access key receipt ID
            third_party_access_key_data (ThirdPartyAccessKeyData):

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
            ThirdPartyAccessKeyReceiptData
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
        kwargs['consent_receipt_id'] = \
            consent_receipt_id
        kwargs['third_party_access_key_data'] = \
            third_party_access_key_data
        return self.update_third_party_access_key_endpoint.call_with_http_info(**kwargs)
