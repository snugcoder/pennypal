# openapi_client.CashFlowAnalyticsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cash_flow_analytics**](CashFlowAnalyticsApi.md#generate_cash_flow_analytics) | **POST** /analytics/cashflow/v1/customer/{customerId} | Generate Cash Flow Analytics
[**generate_cash_flow_analytics_fcra**](CashFlowAnalyticsApi.md#generate_cash_flow_analytics_fcra) | **POST** /analytics/cashflow/v1/customer/{customerId}/fcra | Generate Cash Flow Analytics - FCRA
[**get_obb_analytics_report**](CashFlowAnalyticsApi.md#get_obb_analytics_report) | **GET** /analytics/data/v1/{obb_report_id} | Get OBB Analytics Report
[**get_obb_analytics_report_fcra**](CashFlowAnalyticsApi.md#get_obb_analytics_report_fcra) | **GET** /analytics/data/v1/{obb_report_id}/fcra | Get OBB Analytics Report - FCRA


# **generate_cash_flow_analytics**
> BalanceAndCashFlowAnalyticsReportAck generate_cash_flow_analytics(customer_id, balance_and_cash_flow_analytics_report_constraints)

Generate Cash Flow Analytics

Cash Flow Analytics for Business analyzes cash flow over time to report metrics and identify behavior that may indicate risk.  Calculated metrics include: * Average transaction value by month over the requested time period * Net cash flow over the requested time period and broken down by month * Count and report of weeks in the requested time period where there   were zero transactions posted to the customer's accounts  * Minimum/maximum/average/sum/count of deposits by month * Minimum/maximum/average/sum/count of withdrawals by month * Estimated amount of deposits that can be classified as business   revenue  * Number of transactions posted incurring a non-sufficient funds (NSF)   fee, and net amount charged in NSF fees   This version of the API is intended for piloting and integration testing your application with the Cash Flow Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Cash Flow Analytics - FCRA_ for the FCRA compliant version of this API.  A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Cash Flow Analytics Report_ (operation: _GetCashFlowAnalyticsReport_).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import cash_flow_analytics_api
from openapi_client.model.balance_and_cash_flow_analytics_report_ack import BalanceAndCashFlowAnalyticsReportAck
from openapi_client.model.obb_error_message import ObbErrorMessage
from openapi_client.model.balance_and_cash_flow_analytics_report_constraints import BalanceAndCashFlowAnalyticsReportConstraints
from pprint import pprint
# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cash_flow_analytics_api.CashFlowAnalyticsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    balance_and_cash_flow_analytics_report_constraints = BalanceAndCashFlowAnalyticsReportConstraints(
        account_ids=[
            5011648377,
        ],
        length_of_report=730,
    ) # BalanceAndCashFlowAnalyticsReportConstraints | 
    reference_number = "abc123" # str | Partner-provided reference number to correlate reports. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Cash Flow Analytics
        api_response = api_instance.generate_cash_flow_analytics(customer_id, balance_and_cash_flow_analytics_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowAnalyticsApi->generate_cash_flow_analytics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Cash Flow Analytics
        api_response = api_instance.generate_cash_flow_analytics(customer_id, balance_and_cash_flow_analytics_report_constraints, reference_number=reference_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowAnalyticsApi->generate_cash_flow_analytics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **balance_and_cash_flow_analytics_report_constraints** | [**BalanceAndCashFlowAnalyticsReportConstraints**](BalanceAndCashFlowAnalyticsReportConstraints.md)|  |
 **reference_number** | **str**| Partner-provided reference number to correlate reports. | [optional]

### Return type

[**BalanceAndCashFlowAnalyticsReportAck**](BalanceAndCashFlowAnalyticsReportAck.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response given when cash flow analytics were generated successfully, providing the caller with a report ID which can be used to retrieve the report as JSON or a PDF. |  -  |
**400** | A bad request was provided |  -  |
**401** | Unauthorized request |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Resource conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_cash_flow_analytics_fcra**
> BalanceAndCashFlowAnalyticsReportAck generate_cash_flow_analytics_fcra(customer_id, balance_and_cash_flow_analytics_report_constraints)

Generate Cash Flow Analytics - FCRA

Cash Flow Analytics for Business analyzes cash flow over time to report metrics and identify behavior that may indicate risk.  Calculated metrics include: * Average transaction value by month over the requested time period * Net cash flow over the requested time period and broken down by month * Count and report of weeks in the requested time period where there   were zero transactions posted to the customer's accounts  * Minimum/maximum/average/sum/count of deposits by month * Minimum/maximum/average/sum/count of withdrawals by month * Estimated amount of deposits that can be classified as business   revenue  * Number of transactions posted incurring a non-sufficient funds (NSF)   fee, and net amount charged in NSF fees   This version of the API is intended for production use. It maintains and enforces all compliance with FCRA rules and requirements.  *Note:* this is a premium service, billable per every successful API call for non-testing customers.  A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Cash Flow Analytics Report - FCRA_ (operation: _GetCashFlowAnalyticsReportFCRA_).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import cash_flow_analytics_api
from openapi_client.model.balance_and_cash_flow_analytics_report_ack import BalanceAndCashFlowAnalyticsReportAck
from openapi_client.model.obb_error_message import ObbErrorMessage
from openapi_client.model.balance_and_cash_flow_analytics_report_constraints import BalanceAndCashFlowAnalyticsReportConstraints
from pprint import pprint
# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cash_flow_analytics_api.CashFlowAnalyticsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    balance_and_cash_flow_analytics_report_constraints = BalanceAndCashFlowAnalyticsReportConstraints(
        account_ids=[
            5011648377,
        ],
        length_of_report=730,
    ) # BalanceAndCashFlowAnalyticsReportConstraints | 
    reference_number = "abc123" # str | Partner-provided reference number to correlate reports. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Cash Flow Analytics - FCRA
        api_response = api_instance.generate_cash_flow_analytics_fcra(customer_id, balance_and_cash_flow_analytics_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowAnalyticsApi->generate_cash_flow_analytics_fcra: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Cash Flow Analytics - FCRA
        api_response = api_instance.generate_cash_flow_analytics_fcra(customer_id, balance_and_cash_flow_analytics_report_constraints, reference_number=reference_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowAnalyticsApi->generate_cash_flow_analytics_fcra: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **balance_and_cash_flow_analytics_report_constraints** | [**BalanceAndCashFlowAnalyticsReportConstraints**](BalanceAndCashFlowAnalyticsReportConstraints.md)|  |
 **reference_number** | **str**| Partner-provided reference number to correlate reports. | [optional]

### Return type

[**BalanceAndCashFlowAnalyticsReportAck**](BalanceAndCashFlowAnalyticsReportAck.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response given when cash flow analytics (FCRA) were generated successfully, providing the caller with a report ID which can be used to retrieve the report as JSON or a PDF. |  -  |
**400** | A bad request was provided |  -  |
**401** | Unauthorized request |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Resource conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obb_analytics_report**
> ObbAnalyticsReport get_obb_analytics_report(obb_report_id)

Get OBB Analytics Report

Retrieve the report saved by _Generate Balance Analytics_ or _Generate Cash Flow Analytics_. Requires the report ID generated by the previous call.  Report data can either be retrieved as a JSON document or PDF file.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import cash_flow_analytics_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.obb_analytics_report import ObbAnalyticsReport
from pprint import pprint
# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cash_flow_analytics_api.CashFlowAnalyticsApi(api_client)
    obb_report_id = "bcab9592-e032-4e7b-b737-0380619a0573" # str | Report ID generated and returned by OBB products

    # example passing only required values which don't have defaults set
    try:
        # Get OBB Analytics Report
        api_response = api_instance.get_obb_analytics_report(obb_report_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowAnalyticsApi->get_obb_analytics_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obb_report_id** | **str**| Report ID generated and returned by OBB products |

### Return type

[**ObbAnalyticsReport**](ObbAnalyticsReport.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OBB Analytics report data as JSON or PDF |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obb_analytics_report_fcra**
> ObbAnalyticsReport get_obb_analytics_report_fcra(obb_report_id, purpose)

Get OBB Analytics Report - FCRA

Retrieve the report saved by _Generate Balance Analytics - FCRA_ or _Generate Cash Flow Analytics - FCRA_. Requires the report ID generated by the previous call.  Report data can either be retrieved as a JSON document or PDF file.  *Note:* this is a premium service, billable per every successful API call for non-testing customers.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import cash_flow_analytics_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.obb_analytics_report import ObbAnalyticsReport
from pprint import pprint
# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cash_flow_analytics_api.CashFlowAnalyticsApi(api_client)
    obb_report_id = "bcab9592-e032-4e7b-b737-0380619a0573" # str | Report ID generated and returned by OBB products
    purpose = "3F" # str | 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

    # example passing only required values which don't have defaults set
    try:
        # Get OBB Analytics Report - FCRA
        api_response = api_instance.get_obb_analytics_report_fcra(obb_report_id, purpose)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowAnalyticsApi->get_obb_analytics_report_fcra: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obb_report_id** | **str**| Report ID generated and returned by OBB products |
 **purpose** | **str**| 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports. |

### Return type

[**ObbAnalyticsReport**](ObbAnalyticsReport.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OBB Analytics FCRA report data as JSON or PDF |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

