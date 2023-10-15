# openapi_client.TxPushApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tx_push_test_transaction**](TxPushApi.md#create_tx_push_test_transaction) | **POST** /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions | Create TxPush Test Transaction
[**delete_tx_push_subscription**](TxPushApi.md#delete_tx_push_subscription) | **DELETE** /aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId} | Delete TxPush Subscription
[**disable_tx_push_notifications**](TxPushApi.md#disable_tx_push_notifications) | **DELETE** /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush | Disable TxPush Notifications
[**subscribe_to_tx_push_notifications**](TxPushApi.md#subscribe_to_tx_push_notifications) | **POST** /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush | Subscribe to TxPush Notifications


# **create_tx_push_test_transaction**
> CreatedTestTxPushTransaction create_tx_push_test_transaction(customer_id, account_id, test_tx_push_transaction)

Create TxPush Test Transaction

Inject a transaction into the transaction list for a testing account. This allows an app to trigger TxPush notifications for the account in order to test the app's TxPush Listener service. This causes the platform to send one transaction event and one account event (showing that the account balance has changed). This service is only supported for testing accounts.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import tx_push_api
from openapi_client.model.test_tx_push_transaction import TestTxPushTransaction
from openapi_client.model.created_test_tx_push_transaction import CreatedTestTxPushTransaction
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
    api_instance = tx_push_api.TxPushApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    account_id = "5011648377" # str | The account ID
    test_tx_push_transaction = TestTxPushTransaction(
        amount=-4.25,
        description="a testing transaction description",
        status="pending",
        posted_date=1607450357,
        transaction_date=1607450357,
    ) # TestTxPushTransaction | 

    # example passing only required values which don't have defaults set
    try:
        # Create TxPush Test Transaction
        api_response = api_instance.create_tx_push_test_transaction(customer_id, account_id, test_tx_push_transaction)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TxPushApi->create_tx_push_test_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **account_id** | **str**| The account ID |
 **test_tx_push_transaction** | [**TestTxPushTransaction**](TestTxPushTransaction.md)|  |

### Return type

[**CreatedTestTxPushTransaction**](CreatedTestTxPushTransaction.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The test notification was successfully sent |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tx_push_subscription**
> delete_tx_push_subscription(customer_id, subscription_id)

Delete TxPush Subscription

Delete a specific subscription to TxPush notifications for the given account. This could be individual deleting the account or transactions events. No more events will be sent for that specific subscription.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import tx_push_api
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
    api_instance = tx_push_api.TxPushApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    subscription_id = 17554874 # int | The subscription ID

    # example passing only required values which don't have defaults set
    try:
        # Delete TxPush Subscription
        api_instance.delete_tx_push_subscription(customer_id, subscription_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TxPushApi->delete_tx_push_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **subscription_id** | **int**| The subscription ID |

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
**204** | The subscription was successfully deleted |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_tx_push_notifications**
> disable_tx_push_notifications(customer_id, account_id)

Disable TxPush Notifications

Delete all TxPush subscriptions with their notifications for the given account. No more notifications will be sent for account or transaction events.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import tx_push_api
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
    api_instance = tx_push_api.TxPushApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    account_id = "5011648377" # str | The account ID

    # example passing only required values which don't have defaults set
    try:
        # Disable TxPush Notifications
        api_instance.disable_tx_push_notifications(customer_id, account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TxPushApi->disable_tx_push_notifications: %s\n" % e)
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
**204** | Subscriptions were successfully deleted for the given account |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_tx_push_notifications**
> TxPushSubscriptions subscribe_to_tx_push_notifications(customer_id, account_id, tx_push_subscription_parameters)

Subscribe to TxPush Notifications

Register a client app's TxPush Listener to receive TxPush notifications related to the given account.  Each call to this service will return two records, one with class account and one with class transaction. Account events are sent when values change in the account's fields (such as `balance` or `interestRate`). Transaction events are sent whenever a new transaction is posted for the account. For institutions that do not provide TxPush services, notifications are sent as soon as Finicity finds a new transaction or new account data through regular aggregation processes.  The listener's URL must be secure (HTTPS) for any real-world account. In addition, the client's TxPush Listener will need to be verified. HTTP and HTTPS connections are only allowed on the standard ports 80 (HTTP) and 443 (HTTPS). The use of other ports will result with the call failing.  For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import tx_push_api
from openapi_client.model.tx_push_subscription_parameters import TxPushSubscriptionParameters
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.tx_push_subscriptions import TxPushSubscriptions
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
    api_instance = tx_push_api.TxPushApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    account_id = "5011648377" # str | The account ID
    tx_push_subscription_parameters = TxPushSubscriptionParameters(
        callback_url="https://www.mydomain.com/txpush/listener",
    ) # TxPushSubscriptionParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Subscribe to TxPush Notifications
        api_response = api_instance.subscribe_to_tx_push_notifications(customer_id, account_id, tx_push_subscription_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TxPushApi->subscribe_to_tx_push_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **account_id** | **str**| The account ID |
 **tx_push_subscription_parameters** | [**TxPushSubscriptionParameters**](TxPushSubscriptionParameters.md)|  |

### Return type

[**TxPushSubscriptions**](TxPushSubscriptions.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The subscription was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

