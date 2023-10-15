# openapi_client.VerifyAssetsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_prequalification_cra_report**](VerifyAssetsApi.md#generate_prequalification_cra_report) | **POST** /decisioning/v2/customers/{customerId}/preQualVoa | Generate Prequalification (CRA) Report
[**generate_prequalification_non_cra_report**](VerifyAssetsApi.md#generate_prequalification_non_cra_report) | **POST** /decisioning/v2/customers/{customerId}/assetSummary | Generate Prequalification (Non-CRA) Report
[**generate_voa_report**](VerifyAssetsApi.md#generate_voa_report) | **POST** /decisioning/v2/customers/{customerId}/voa | Generate VOA Report
[**generate_voa_with_income_report**](VerifyAssetsApi.md#generate_voa_with_income_report) | **POST** /decisioning/v2/customers/{customerId}/voaHistory | Generate VOA With Income Report


# **generate_prequalification_cra_report**
> PrequalificationReportAck generate_prequalification_cra_report(customer_id, prequalification_report_constraints)

Generate Prequalification (CRA) Report

Retrieve all checking, savings, money market, and investment accounts for a consumer. The account, owner information, and the number of insufficient funds (NSFs) for checking accounts are also provided.  If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import verify_assets_api
from openapi_client.model.prequalification_report_ack import PrequalificationReportAck
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.prequalification_report_constraints import PrequalificationReportConstraints
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
    api_instance = verify_assets_api.VerifyAssetsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    prequalification_report_constraints = PrequalificationReportConstraints(
        account_ids="5011648377 5011648378 5011648379",
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        show_nsf=False,
        from_date=1607450357,
    ) # PrequalificationReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Prequalification (CRA) Report
        api_response = api_instance.generate_prequalification_cra_report(customer_id, prequalification_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_prequalification_cra_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Prequalification (CRA) Report
        api_response = api_instance.generate_prequalification_cra_report(customer_id, prequalification_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_prequalification_cra_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **prequalification_report_constraints** | [**PrequalificationReportConstraints**](PrequalificationReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**PrequalificationReportAck**](PrequalificationReportAck.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The report is being generated. When finished, a notification will be sent to the specified callback URL (Report Listener Service) and the report can be fetched using Get Report APIs. If you don&#39;t use a callback URL, Get Report returns a minimal report with the following status: &#39;inProgress&#39;. Repeat the call every 20 seconds until Get Report returns a different status. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_prequalification_non_cra_report**
> PrequalificationReportAck generate_prequalification_non_cra_report(customer_id, prequalification_report_constraints)

Generate Prequalification (Non-CRA) Report

Retrieve all checking, savings, money market, and investment accounts for a customer. The account, owner information, and the number of insufficient funds (NSFs) for checking accounts are also provided.  If no account type of checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import verify_assets_api
from openapi_client.model.prequalification_report_ack import PrequalificationReportAck
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.prequalification_report_constraints import PrequalificationReportConstraints
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
    api_instance = verify_assets_api.VerifyAssetsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    prequalification_report_constraints = PrequalificationReportConstraints(
        account_ids="5011648377 5011648378 5011648379",
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        show_nsf=False,
        from_date=1607450357,
    ) # PrequalificationReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Prequalification (Non-CRA) Report
        api_response = api_instance.generate_prequalification_non_cra_report(customer_id, prequalification_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_prequalification_non_cra_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Prequalification (Non-CRA) Report
        api_response = api_instance.generate_prequalification_non_cra_report(customer_id, prequalification_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_prequalification_non_cra_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **prequalification_report_constraints** | [**PrequalificationReportConstraints**](PrequalificationReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**PrequalificationReportAck**](PrequalificationReportAck.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The report is being generated. When finished, a notification will be sent to the specified callback URL (Report Listener Service) and the report can be fetched using Get Report APIs. If you don&#39;t use a callback URL, Get Report returns a minimal report with the following status: &#39;inProgress&#39;. Repeat the call every 20 seconds until Get Report returns a different status. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_voa_report**
> VOAReportAck generate_voa_report(customer_id, voa_report_constraints)

Generate VOA Report

Generate a Verification of Assets (VOA) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to twelve months of transaction history for each account and uses this information to generate the VOA report.  This is a premium service. The billing rate is the variable rate for Verification of Assets under the current subscription plan. The billable event is the successful generation of a VOA report.  Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import verify_assets_api
from openapi_client.model.voa_report_ack import VOAReportAck
from openapi_client.model.voa_report_constraints import VOAReportConstraints
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = verify_assets_api.VerifyAssetsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    voa_report_constraints = VOAReportConstraints(
        account_ids="5011648377 5011648378 5011648379",
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        show_nsf=False,
        from_date=1607450357,
    ) # VOAReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate VOA Report
        api_response = api_instance.generate_voa_report(customer_id, voa_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_voa_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate VOA Report
        api_response = api_instance.generate_voa_report(customer_id, voa_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_voa_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **voa_report_constraints** | [**VOAReportConstraints**](VOAReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**VOAReportAck**](VOAReportAck.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The report is being generated. When finished, a notification will be sent to the specified callback URL (Report Listener Service) and the report can be fetched using Get Report APIs. If you don&#39;t use a callback URL, Get Report returns a minimal report with the following status: &#39;inProgress&#39;. Repeat the call every 20 seconds until Get Report returns a different status. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_voa_with_income_report**
> VOAWithIncomeReportAck generate_voa_with_income_report(customer_id, voa_with_income_report_constraints)

Generate VOA With Income Report

Generate a Verification of Assets with Income (VOAI) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to 24 months of transaction history for each account and uses this information to generate the VOAI report. The report includes 1 - 6 months of all debit and credit transactions for asset verification. By default, the history is set to 61 days, however, you can change the transaction history in this section by setting the `fromDate` parameter. The report also includes up to 24 months of income credit transactions (ordered by account and confidence level) regardless of `fromDate` for income verification.  This is a premium service. The billable event is the successful generation of a VOAI report.  Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import verify_assets_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.voa_with_income_report_constraints import VOAWithIncomeReportConstraints
from openapi_client.model.voa_with_income_report_ack import VOAWithIncomeReportAck
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
    api_instance = verify_assets_api.VerifyAssetsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    voa_with_income_report_constraints = VOAWithIncomeReportConstraints(
        account_ids="5011648377 5011648378 5011648379",
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        show_nsf=False,
        from_date=1607450357,
        income_stream_confidence_minimum=50,
    ) # VOAWithIncomeReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate VOA With Income Report
        api_response = api_instance.generate_voa_with_income_report(customer_id, voa_with_income_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_voa_with_income_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate VOA With Income Report
        api_response = api_instance.generate_voa_with_income_report(customer_id, voa_with_income_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerifyAssetsApi->generate_voa_with_income_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **voa_with_income_report_constraints** | [**VOAWithIncomeReportConstraints**](VOAWithIncomeReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**VOAWithIncomeReportAck**](VOAWithIncomeReportAck.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The report is being generated. When finished, a notification will be sent to the specified callback URL (Report Listener Service) and the report can be fetched using Get Report APIs. If you don&#39;t use a callback URL, Get Report returns a minimal report with the following status: &#39;inProgress&#39;. Repeat the call every 20 seconds until Get Report returns a different status. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

