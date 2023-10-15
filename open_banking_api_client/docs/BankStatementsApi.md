# openapi_client.BankStatementsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_statement_report**](BankStatementsApi.md#generate_statement_report) | **POST** /decisioning/v2/customers/{customerId}/statement | Generate Statement Report
[**get_customer_account_statement**](BankStatementsApi.md#get_customer_account_statement) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement | Get Customer Account Statement


# **generate_statement_report**
> StatementReportAck generate_statement_report(customer_id, statement_report_constraints)

Generate Statement Report

Generate a Statement Report report for the given accounts under the given customer.  This is a premium service. A billable event will be created upon the successful generation of the Statement Report.   Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import bank_statements_api
from openapi_client.model.statement_report_constraints import StatementReportConstraints
from openapi_client.model.statement_report_ack import StatementReportAck
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
    api_instance = bank_statements_api.BankStatementsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    statement_report_constraints = StatementReportConstraints(
        statement_report_data=StatementData(
            account_id=5011648377,
            statement_index=1,
        ),
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
    ) # StatementReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Statement Report
        api_response = api_instance.generate_statement_report(customer_id, statement_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankStatementsApi->generate_statement_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Statement Report
        api_response = api_instance.generate_statement_report(customer_id, statement_report_constraints, callback_url=callback_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankStatementsApi->generate_statement_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **statement_report_constraints** | [**StatementReportConstraints**](StatementReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]

### Return type

[**StatementReportAck**](StatementReportAck.md)

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

# **get_customer_account_statement**
> file_type get_customer_account_statement(customer_id, account_id)

Get Customer Account Statement

Retrieve the customer's bank statements in PDF format. Up to 24 months of history is available depending on the financial institution. Since this is a premium service, charges incur per each successful statement retrieved.   For certified financial institutions, statements are available for the following account types: * Checking * Savings * Money market * CDs * Investments * Mortgage * Credit cards * Loans * Line of credit * Student Loans  Note: setting the timeout to 180 seconds is recommended to allow enough time for a response.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import bank_statements_api
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
    api_instance = bank_statements_api.BankStatementsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    account_id = "5011648377" # str | The account ID
    index = 1 # int | Request statements from 1-24. By default, 1 is the most recent statement. Increase the index value to count back (by month) and retrieve its most recent statement. (optional) if omitted the server will use the default value of 1
    type = "taxStatement" # str | The type of statement to retrieve (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Customer Account Statement
        api_response = api_instance.get_customer_account_statement(customer_id, account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankStatementsApi->get_customer_account_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customer Account Statement
        api_response = api_instance.get_customer_account_statement(customer_id, account_id, index=index, type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankStatementsApi->get_customer_account_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **account_id** | **str**| The account ID |
 **index** | **int**| Request statements from 1-24. By default, 1 is the most recent statement. Increase the index value to count back (by month) and retrieve its most recent statement. | [optional] if omitted the server will use the default value of 1
 **type** | **str**| The type of statement to retrieve | [optional]

### Return type

**file_type**

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The statement was successfully downloaded as a PDF file |  -  |
**203** | The response contains an MFA challenge in XML or JSON format. Contact your Account Manager or Systems Engineers to determine the best route to handle this error. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

