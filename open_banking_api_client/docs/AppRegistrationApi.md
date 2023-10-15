# openapi_client.AppRegistrationApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_registration_status**](AppRegistrationApi.md#get_app_registration_status) | **GET** /aggregation/v2/partners/applications | Get App Registration Status
[**migrate_institution_login_accounts**](AppRegistrationApi.md#migrate_institution_login_accounts) | **PUT** /aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/migration | Migrate Institution Login Accounts
[**modify_app_registration**](AppRegistrationApi.md#modify_app_registration) | **PUT** /aggregation/v1/partners/applications/{preAppId} | Modify App Registration
[**register_app**](AppRegistrationApi.md#register_app) | **POST** /aggregation/v1/partners/applications | Register App
[**set_customer_app_id**](AppRegistrationApi.md#set_customer_app_id) | **PUT** /aggregation/v1/customers/{customerId}/applications/{applicationId} | Set Customer App ID


# **get_app_registration_status**
> AppStatuses get_app_registration_status()

Get App Registration Status

Get the status of your application registration(s).  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import app_registration_api
from openapi_client.model.app_statuses import AppStatuses
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
    api_instance = app_registration_api.AppRegistrationApi(api_client)
    pre_app_id = "2581" # str | The application registration tracking ID (optional)
    application_id = "123456789" # str | The application ID (optional)
    status = "P" # str | Look up app registration requests by status (optional)
    app_name = "Awesome Budget App" # str | Look up app registration requests by app name (optional)
    submitted_date = 1607450357 # int | Look up app registration requests by the date they were submitted (optional)
    modified_date = 1607450357 # int | Look up app registration requests by the date the request was updated. This can be used to determine when a request was updated to \"A\" or \"R\". (optional)
    page = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    page_size = 20 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get App Registration Status
        api_response = api_instance.get_app_registration_status(pre_app_id=pre_app_id, application_id=application_id, status=status, app_name=app_name, submitted_date=submitted_date, modified_date=modified_date, page=page, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppRegistrationApi->get_app_registration_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_app_id** | **str**| The application registration tracking ID | [optional]
 **application_id** | **str**| The application ID | [optional]
 **status** | **str**| Look up app registration requests by status | [optional]
 **app_name** | **str**| Look up app registration requests by app name | [optional]
 **submitted_date** | **int**| Look up app registration requests by the date they were submitted | [optional]
 **modified_date** | **int**| Look up app registration requests by the date the request was updated. This can be used to determine when a request was updated to \&quot;A\&quot; or \&quot;R\&quot;. | [optional]
 **page** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 1

### Return type

[**AppStatuses**](AppStatuses.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app registration statuses were returned |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_institution_login_accounts**
> CustomerAccounts migrate_institution_login_accounts(customer_id, institution_login_id)

Migrate Institution Login Accounts

The `institutionLoginId` parameter uses Finicity's internal FI mapping to move accounts from the current FI legacy connection to the new OAuth FI connection.  This API returns a list of accounts for the given institution login ID.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import app_registration_api
from openapi_client.model.customer_accounts import CustomerAccounts
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
    api_instance = app_registration_api.AppRegistrationApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    institution_login_id = "1007302745" # str | The institution login ID

    # example passing only required values which don't have defaults set
    try:
        # Migrate Institution Login Accounts
        api_response = api_instance.migrate_institution_login_accounts(customer_id, institution_login_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppRegistrationApi->migrate_institution_login_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **institution_login_id** | **str**| The institution login ID |

### Return type

[**CustomerAccounts**](CustomerAccounts.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The migration succeeded |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_app_registration**
> RegisteredApplication modify_app_registration(pre_app_id, application)

Modify App Registration

Update a registered application.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import app_registration_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.application import Application
from openapi_client.model.registered_application import RegisteredApplication
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
    api_instance = app_registration_api.AppRegistrationApi(api_client)
    pre_app_id = "2581" # str | The application registration tracking ID
    application = Application(
        app_description="The app that makes your budgeting experience awesome",
        app_name="Awesome Budget App",
        app_url="https://www.finicity.com/",
        owner_address_line1="434 W Ascension Way",
        owner_address_line2="Suite #200",
        owner_city="Murray",
        owner_country="USA",
        owner_name="Finicity",
        owner_postal_code="84123",
        owner_state="UT",
        image="PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgICAKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB2ZXJzaW9uPSIxLjEiCiAgIHZpZXdCb3g9IjAgMCAwIDAiCiAgIGhlaWdodD0iMCIKICAgd2lkdGg9IjAiPgogICAgPGcvPgo8L3N2Zz4K",
    ) # Application | 

    # example passing only required values which don't have defaults set
    try:
        # Modify App Registration
        api_response = api_instance.modify_app_registration(pre_app_id, application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppRegistrationApi->modify_app_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_app_id** | **str**| The application registration tracking ID |
 **application** | [**Application**](Application.md)|  |

### Return type

[**RegisteredApplication**](RegisteredApplication.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app registration was updated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_app**
> RegisteredApplication register_app(application)

Register App

Register a new application to access financial institutions using OAuth connections.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import app_registration_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.application import Application
from openapi_client.model.registered_application import RegisteredApplication
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
    api_instance = app_registration_api.AppRegistrationApi(api_client)
    application = Application(
        app_description="The app that makes your budgeting experience awesome",
        app_name="Awesome Budget App",
        app_url="https://www.finicity.com/",
        owner_address_line1="434 W Ascension Way",
        owner_address_line2="Suite #200",
        owner_city="Murray",
        owner_country="USA",
        owner_name="Finicity",
        owner_postal_code="84123",
        owner_state="UT",
        image="PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgICAKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB2ZXJzaW9uPSIxLjEiCiAgIHZpZXdCb3g9IjAgMCAwIDAiCiAgIGhlaWdodD0iMCIKICAgd2lkdGg9IjAiPgogICAgPGcvPgo8L3N2Zz4K",
    ) # Application | 

    # example passing only required values which don't have defaults set
    try:
        # Register App
        api_response = api_instance.register_app(application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppRegistrationApi->register_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)|  |

### Return type

[**RegisteredApplication**](RegisteredApplication.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The app registration was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_customer_app_id**
> set_customer_app_id(customer_id, application_id)

Set Customer App ID

If you have multiple applications for a single client, and you want to register their applications to access financial institutions using OAuth connections, then use this API to assign applications to an existing customer.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import app_registration_api
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
    api_instance = app_registration_api.AppRegistrationApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    application_id = "123456789" # str | The application ID

    # example passing only required values which don't have defaults set
    try:
        # Set Customer App ID
        api_instance.set_customer_app_id(customer_id, application_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AppRegistrationApi->set_customer_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **application_id** | **str**| The application ID |

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
**200** | The app was successfully assigned |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

