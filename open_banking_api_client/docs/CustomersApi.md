# openapi_client.CustomersApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer**](CustomersApi.md#add_customer) | **POST** /aggregation/v2/customers/active | Add Customer
[**add_testing_customer**](CustomersApi.md#add_testing_customer) | **POST** /aggregation/v2/customers/testing | Add Testing Customer
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /aggregation/v1/customers/{customerId} | Delete Customer by ID
[**get_customer**](CustomersApi.md#get_customer) | **GET** /aggregation/v1/customers/{customerId} | Get Customer by ID
[**get_customer_with_app_data**](CustomersApi.md#get_customer_with_app_data) | **GET** /aggregation/v1/customers/{customerId}/application | Get Customer With App Data by ID
[**get_customers**](CustomersApi.md#get_customers) | **GET** /aggregation/v1/customers | Get Customers
[**modify_customer**](CustomersApi.md#modify_customer) | **PUT** /aggregation/v1/customers/{customerId} | Modify Customer by ID


# **add_customer**
> CreatedCustomer add_customer(new_customer)

Add Customer

Enroll an active customer, which is the actual owner of one or more real-world accounts. This is a billable customer.  Active customers must use the \"FinBank Billable\" profiles for testing purposes.   _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.created_customer import CreatedCustomer
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.new_customer import NewCustomer
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
    api_instance = customers_api.CustomersApi(api_client)
    new_customer = NewCustomer(
        username="customerusername1",
        first_name="John",
        last_name="Smith",
        application_id="123456789",
        phone="1-801-984-4200",
        email="myname@mycompany.com",
    ) # NewCustomer | 

    # example passing only required values which don't have defaults set
    try:
        # Add Customer
        api_response = api_instance.add_customer(new_customer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->add_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_customer** | [**NewCustomer**](NewCustomer.md)|  |

### Return type

[**CreatedCustomer**](CreatedCustomer.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The customer was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**429** | The service can&#39;t accept more requests or is not available from the [Test Drive](https://signup.finicity.com/). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_testing_customer**
> CreatedCustomer add_testing_customer(new_customer)

Add Testing Customer

Enroll a testing customer ([Test Drive](https://signup.finicity.com/) accounts).  For using testing customers with FinBank OAuth, you must register a test application with your systems engineer or account manager. Then, use that testing `applicationId` when creating testing customers.  Testing Customers can access FinBank profiles (except \"FinBank Billable\" profiles), and cannot access live financial institutions.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.created_customer import CreatedCustomer
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.new_customer import NewCustomer
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
    api_instance = customers_api.CustomersApi(api_client)
    new_customer = NewCustomer(
        username="customerusername1",
        first_name="John",
        last_name="Smith",
        application_id="123456789",
        phone="1-801-984-4200",
        email="myname@mycompany.com",
    ) # NewCustomer | 

    # example passing only required values which don't have defaults set
    try:
        # Add Testing Customer
        api_response = api_instance.add_testing_customer(new_customer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->add_testing_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_customer** | [**NewCustomer**](NewCustomer.md)|  |

### Return type

[**CreatedCustomer**](CreatedCustomer.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The customer was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(customer_id)

Delete Customer by ID

Completely remove a customer from the system. This will remove the customer and all associated accounts and transactions.  ⚠️ Use this service carefully! It will not pause for confirmation before performing the operation!  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
    customer_id = "1005061234" # str | A customer ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Customer by ID
        api_instance.delete_customer(customer_id)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |

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
**204** | The customer was successfully deleted |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> Customer get_customer(customer_id)

Get Customer by ID

Retrieve a customer by ID.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.customer import Customer
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
    api_instance = customers_api.CustomersApi(api_client)
    customer_id = "1005061234" # str | A customer ID

    # example passing only required values which don't have defaults set
    try:
        # Get Customer by ID
        api_response = api_instance.get_customer(customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |

### Return type

[**Customer**](Customer.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The customer was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_with_app_data**
> CustomerWithAppData get_customer_with_app_data(customer_id)

Get Customer With App Data by ID

Retrieve a customer along with additional details about the OAuth application.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.customer_with_app_data import CustomerWithAppData
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
    api_instance = customers_api.CustomersApi(api_client)
    customer_id = "1005061234" # str | A customer ID

    # example passing only required values which don't have defaults set
    try:
        # Get Customer With App Data by ID
        api_response = api_instance.get_customer_with_app_data(customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_customer_with_app_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |

### Return type

[**CustomerWithAppData**](CustomerWithAppData.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The customer was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers**
> Customers get_customers()

Get Customers

Find all customers enrolled by the current partner, where the search text is found in the customer's username or any combination of `firstName` and `lastName` fields. If no search text is provided, all customers will be returned.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.customers import Customers
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
    api_instance = customers_api.CustomersApi(api_client)
    username = "customerusername1" # str | Username for exact match (will return 0 or 1 record) (optional)
    type = "active" # str | \"testing\" or \"active\" to return only customers of that type, or leave empty to return all customers (optional)
    search = "searchvalue" # str | The text you wish to match. Leave this empty if you wish to return all customers. Must be URL-encoded (see: [Handling Spaces in Queries](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/)). (optional)
    start = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    limit = 1 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customers
        api_response = api_instance.get_customers(username=username, type=type, search=search, start=start, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for exact match (will return 0 or 1 record) | [optional]
 **type** | **str**| \&quot;testing\&quot; or \&quot;active\&quot; to return only customers of that type, or leave empty to return all customers | [optional]
 **search** | **str**| The text you wish to match. Leave this empty if you wish to return all customers. Must be URL-encoded (see: [Handling Spaces in Queries](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/)). | [optional]
 **start** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 25

### Return type

[**Customers**](Customers.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customers were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_customer**
> modify_customer(customer_id, customer_update)

Modify Customer by ID

Modify an enrolled customer by ID.  You must specify either `firstName`, `lastName`, or both in the request.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.customer_update import CustomerUpdate
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
    api_instance = customers_api.CustomersApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    customer_update = CustomerUpdate(
        first_name="John",
        last_name="Smith",
    ) # CustomerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Modify Customer by ID
        api_instance.modify_customer(customer_id, customer_update)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->modify_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **customer_update** | [**CustomerUpdate**](CustomerUpdate.md)|  |

### Return type

void (empty response body)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The customer was successfully updated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

