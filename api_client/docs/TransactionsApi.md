# openapi_client.TransactionsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_transactions_report**](TransactionsApi.md#generate_transactions_report) | **POST** /decisioning/v2/customers/{customerId}/transactions | Generate Transactions Report
[**get_all_customer_transactions**](TransactionsApi.md#get_all_customer_transactions) | **GET** /aggregation/v3/customers/{customerId}/transactions | Get All Customer Transactions
[**get_customer_account_transactions**](TransactionsApi.md#get_customer_account_transactions) | **GET** /aggregation/v4/customers/{customerId}/accounts/{accountId}/transactions | Get Customer Account Transactions
[**get_customer_transaction**](TransactionsApi.md#get_customer_transaction) | **GET** /aggregation/v2/customers/{customerId}/transactions/{transactionId} | Get Customer Transaction by ID
[**load_historic_transactions_for_customer_account**](TransactionsApi.md#load_historic_transactions_for_customer_account) | **POST** /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic | Load Historic Transactions for Customer Account


# **generate_transactions_report**
> TransactionsReportAck generate_transactions_report(customer_id, to_date, transactions_report_constraints)

Generate Transactions Report

Generate a Transaction Report for the given accounts under the given customer. This service retrieves up to 24 months of transaction history for the given customer. It then uses this information to generate the Transaction Report.  This is a premium service. A billable event will be created upon the successful generation of the Transactions Report.   Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).  There cannot be more than 24 months between `fromDate` and `toDate`.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transactions_report_ack import TransactionsReportAck
from openapi_client.model.transactions_report_constraints import TransactionsReportConstraints
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
    api_instance = transactions_api.TransactionsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    to_date = 1607450357 # int | A end date
    transactions_report_constraints = TransactionsReportConstraints(
        account_ids="5011648377 5011648378 5011648379",
        from_date=1607450357,
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
    ) # TransactionsReportConstraints | 
    callback_url = "https://finicity-test/webhook" # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)
    include_pending = False # bool | If pending transactions must be included (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Generate Transactions Report
        api_response = api_instance.generate_transactions_report(customer_id, to_date, transactions_report_constraints)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->generate_transactions_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Transactions Report
        api_response = api_instance.generate_transactions_report(customer_id, to_date, transactions_report_constraints, callback_url=callback_url, include_pending=include_pending)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->generate_transactions_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **to_date** | **int**| A end date |
 **transactions_report_constraints** | [**TransactionsReportConstraints**](TransactionsReportConstraints.md)|  |
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional]
 **include_pending** | **bool**| If pending transactions must be included | [optional] if omitted the server will use the default value of False

### Return type

[**TransactionsReportAck**](TransactionsReportAck.md)

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

# **get_all_customer_transactions**
> Transactions get_all_customer_transactions(customer_id, from_date, to_date)

Get All Customer Transactions

Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.  Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the service Load Historic Transactions for Account.  There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transactions import Transactions
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
    api_instance = transactions_api.TransactionsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    from_date = 1607450357 # int | A start date
    to_date = 1607450357 # int | A end date
    start = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    limit = 1 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 25
    sort = "desc" # str | Date sort order: \"asc\" for ascending, \"desc\" for descending (optional) if omitted the server will use the default value of "desc"
    include_pending = False # bool | If pending transactions must be included (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get All Customer Transactions
        api_response = api_instance.get_all_customer_transactions(customer_id, from_date, to_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_all_customer_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Customer Transactions
        api_response = api_instance.get_all_customer_transactions(customer_id, from_date, to_date, start=start, limit=limit, sort=sort, include_pending=include_pending)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_all_customer_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **from_date** | **int**| A start date |
 **to_date** | **int**| A end date |
 **start** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| Date sort order: \&quot;asc\&quot; for ascending, \&quot;desc\&quot; for descending | [optional] if omitted the server will use the default value of "desc"
 **include_pending** | **bool**| If pending transactions must be included | [optional] if omitted the server will use the default value of False

### Return type

[**Transactions**](Transactions.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transactions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_account_transactions**
> Transactions get_customer_account_transactions(customer_id, account_id, from_date, to_date)

Get Customer Account Transactions

Get all transactions available for this customer account within the given date range. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.  Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.  There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transactions import Transactions
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
    api_instance = transactions_api.TransactionsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    account_id = "5011648377" # str | The account ID
    from_date = 1607450357 # int | A start date
    to_date = 1607450357 # int | A end date
    start = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    limit = 1 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 25
    sort = "desc" # str | Date sort order: \"asc\" for ascending, \"desc\" for descending (optional) if omitted the server will use the default value of "desc"
    include_pending = False # bool | If pending transactions must be included (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Customer Account Transactions
        api_response = api_instance.get_customer_account_transactions(customer_id, account_id, from_date, to_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_customer_account_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customer Account Transactions
        api_response = api_instance.get_customer_account_transactions(customer_id, account_id, from_date, to_date, start=start, limit=limit, sort=sort, include_pending=include_pending)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_customer_account_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **account_id** | **str**| The account ID |
 **from_date** | **int**| A start date |
 **to_date** | **int**| A end date |
 **start** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| Date sort order: \&quot;asc\&quot; for ascending, \&quot;desc\&quot; for descending | [optional] if omitted the server will use the default value of "desc"
 **include_pending** | **bool**| If pending transactions must be included | [optional] if omitted the server will use the default value of False

### Return type

[**Transactions**](Transactions.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transactions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_transaction**
> Transaction get_customer_transaction(customer_id, transaction_id)

Get Customer Transaction by ID

Get details for the given transaction.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
from openapi_client.model.transaction import Transaction
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
    api_instance = transactions_api.TransactionsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    transaction_id = 21284820852 # int | A transaction ID

    # example passing only required values which don't have defaults set
    try:
        # Get Customer Transaction by ID
        api_response = api_instance.get_customer_transaction(customer_id, transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_customer_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **transaction_id** | **int**| A transaction ID |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_historic_transactions_for_customer_account**
> load_historic_transactions_for_customer_account(customer_id, account_id)

Load Historic Transactions for Customer Account

Connect to the account's financial institution and load up to 24 months of historic transactions for the account. Length of history varies by institution.  This is a premium service. The billable event is a call to this service specifying a customer ID that has not been seen before by this service. (If this service is called multiple times with the same customer ID, to load transactions from multiple accounts, only one billable event has occurred.)  The recommended timeout setting for this request is 180 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.  The date range sent to the institution is calculated from the account's `createdDate`. This means that calling this service a second time for the same account normally will not add any new transactions for the account. For this reason, a second call to this service for a known account ID will usually return immediately.  In a few specific scenarios, it may be desirable to force a second connection to the institution for a known account ID. Some examples are:  * The institution's policy has changed, making more transactions available * Finicity has now added a longer transaction history support for the institution * The first call encountered an error, and the resulting Aggregation Ticket has now been fixed by the Finicity Support Team  In these cases, the POST request can contain the parameter `force=true` in the request body to force the second connection.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import transactions_api
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
    api_instance = transactions_api.TransactionsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    account_id = "5011648377" # str | The account ID

    # example passing only required values which don't have defaults set
    try:
        # Load Historic Transactions for Customer Account
        api_instance.load_historic_transactions_for_customer_account(customer_id, account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->load_historic_transactions_for_customer_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **account_id** | **str**| The account ID |

### Return type

void (empty response body)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**203** | The response contains an MFA challenge in XML or JSON format. Contact your Account Manager or Systems Engineers to determine the best route to handle this error. |  -  |
**204** | Historic transactions have been loaded successfully. The transactions are now available by calling the Get Customer Account Transactions API. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

