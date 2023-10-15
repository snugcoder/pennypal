# openapi_client.CashFlowApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cash_flow_business_report**](CashFlowApi.md#generate_cash_flow_business_report) | **POST** /decisioning/v2/customers/{customerId}/cashFlowBusiness | Generate Cash Flow Report - Business
[**generate_cash_flow_personal_report**](CashFlowApi.md#generate_cash_flow_personal_report) | **POST** /decisioning/v2/customers/{customerId}/cashFlowPersonal | Generate Cash Flow Report - Personal


# **generate_cash_flow_business_report**
> CashFlowReportAck generate_cash_flow_business_report(customer_id, cash_flow_report_constraints)

Generate Cash Flow Report - Business

Generate a Cash Flow Report (Business) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report. A consumer is not required to generate this report.  This report is not provided under FCRA rules, and this report is not available in the Finicity Consumer Portal for the borrower to view.  If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import cash_flow_api
from openapi_client.model.cash_flow_report_ack import CashFlowReportAck
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.cash_flow_report_constraints import CashFlowReportConstraints
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
    api_instance = cash_flow_api.CashFlowApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    cash_flow_report_constraints = CashFlowReportConstraints(
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
    ) # CashFlowReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Cash Flow Report - Business
        api_response = api_instance.generate_cash_flow_business_report(customer_id, cash_flow_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowApi->generate_cash_flow_business_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Cash Flow Report - Business
        api_response = api_instance.generate_cash_flow_business_report(customer_id, cash_flow_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowApi->generate_cash_flow_business_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **cash_flow_report_constraints** | [**CashFlowReportConstraints**](CashFlowReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**CashFlowReportAck**](CashFlowReportAck.md)

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

# **generate_cash_flow_personal_report**
> CashFlowReportAck generate_cash_flow_personal_report(customer_id, cash_flow_report_constraints)

Generate Cash Flow Report - Personal

Generate a Cash Flow Report (Personal) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report.  This report is provided under FCRA rules, with Finicity acting as the CRA (Consumer Reporting Agency). If an individual account is included in the report - for example, with an individual acting as an personal guarantor on the loan - then this version of the report should be used. In case of an adverse action on the loan where the decision was based on this report, then the borrower can be referred to the [Finicity Consumer Portal](https://consumer.finicityreports.com) where they can view this report and submit a dispute if they feel any information in this report is inaccurate.  Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import cash_flow_api
from openapi_client.model.cash_flow_report_ack import CashFlowReportAck
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.cash_flow_report_constraints import CashFlowReportConstraints
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
    api_instance = cash_flow_api.CashFlowApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    cash_flow_report_constraints = CashFlowReportConstraints(
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
    ) # CashFlowReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Cash Flow Report - Personal
        api_response = api_instance.generate_cash_flow_personal_report(customer_id, cash_flow_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowApi->generate_cash_flow_personal_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Cash Flow Report - Personal
        api_response = api_instance.generate_cash_flow_personal_report(customer_id, cash_flow_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CashFlowApi->generate_cash_flow_personal_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **cash_flow_report_constraints** | [**CashFlowReportConstraints**](CashFlowReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**CashFlowReportAck**](CashFlowReportAck.md)

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

