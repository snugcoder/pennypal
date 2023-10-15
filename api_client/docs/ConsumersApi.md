# openapi_client.ConsumersApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consumer**](ConsumersApi.md#create_consumer) | **POST** /decisioning/v1/customers/{customerId}/consumer | Create Consumer
[**get_consumer**](ConsumersApi.md#get_consumer) | **GET** /decisioning/v1/consumers/{consumerId} | Get Consumer by ID
[**get_consumer_for_customer**](ConsumersApi.md#get_consumer_for_customer) | **GET** /decisioning/v1/customers/{customerId}/consumer | Get Consumer For Customer
[**modify_consumer**](ConsumersApi.md#modify_consumer) | **PUT** /decisioning/v1/consumers/{consumerId} | Modify Consumer by ID


# **create_consumer**
> CreatedConsumer create_consumer(customer_id, new_consumer)

Create Consumer

Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system.  A consumer must be created for the given customer before calling any of the Generate Report services.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import consumers_api
from openapi_client.model.created_consumer import CreatedConsumer
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.new_consumer import NewConsumer
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
    api_instance = consumers_api.ConsumersApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    new_consumer = NewConsumer(
        first_name="John",
        last_name="Smith",
        address="434 W Ascension Way",
        city="Murray",
        state="UT",
        zip="84123",
        phone="1-801-984-4200",
        ssn="999-99-9999",
        birthday=Birthday(
            year=1989,
            month=8,
            day_of_month=13,
        ),
        email="myname@mycompany.com",
        suffix="PhD",
    ) # NewConsumer | 

    # example passing only required values which don't have defaults set
    try:
        # Create Consumer
        api_response = api_instance.create_consumer(customer_id, new_consumer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumersApi->create_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **new_consumer** | [**NewConsumer**](NewConsumer.md)|  |

### Return type

[**CreatedConsumer**](CreatedConsumer.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The consumer was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |
**409** | The resource already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer**
> Consumer get_consumer(consumer_id)

Get Consumer by ID

Get the details of a consumer record by consumer ID.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import consumers_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.consumer import Consumer
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
    api_instance = consumers_api.ConsumersApi(api_client)
    consumer_id = "0bf46322c167b562e6cbed9d40e19a4c" # str | The consumer ID

    # example passing only required values which don't have defaults set
    try:
        # Get Consumer by ID
        api_response = api_instance.get_consumer(consumer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumersApi->get_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| The consumer ID |

### Return type

[**Consumer**](Consumer.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consumer was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_for_customer**
> Consumer get_consumer_for_customer(customer_id)

Get Consumer For Customer

Get the details of a consumer record by customer ID.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import consumers_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.consumer import Consumer
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
    api_instance = consumers_api.ConsumersApi(api_client)
    customer_id = "1005061234" # str | A customer ID

    # example passing only required values which don't have defaults set
    try:
        # Get Consumer For Customer
        api_response = api_instance.get_consumer_for_customer(customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumersApi->get_consumer_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |

### Return type

[**Consumer**](Consumer.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consumer was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_consumer**
> modify_consumer(consumer_id, consumer_update)

Modify Consumer by ID

Modify an existing consumer. All fields are required for a consumer record, but individual fields for this call are optional because fields that are not specified will be left unchanged.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import consumers_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.consumer_update import ConsumerUpdate
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
    api_instance = consumers_api.ConsumersApi(api_client)
    consumer_id = "0bf46322c167b562e6cbed9d40e19a4c" # str | The consumer ID
    consumer_update = ConsumerUpdate(
        first_name="John",
        last_name="Smith",
        address="434 W Ascension Way",
        city="Murray",
        state="UT",
        zip="84123",
        phone="1-801-984-4200",
        ssn="999-99-9999",
        birthday=Birthday(
            year=1989,
            month=8,
            day_of_month=13,
        ),
        email="myname@mycompany.com",
        suffix="PhD",
    ) # ConsumerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Modify Consumer by ID
        api_instance.modify_consumer(consumer_id, consumer_update)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumersApi->modify_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| The consumer ID |
 **consumer_update** | [**ConsumerUpdate**](ConsumerUpdate.md)|  |

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
**204** | The consumer was successfully updated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

