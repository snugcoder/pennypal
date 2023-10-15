# openapi_client.InstitutionsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certified_institutions**](InstitutionsApi.md#get_certified_institutions) | **GET** /institution/v2/certifiedInstitutions | Get Certified Institutions
[**get_certified_institutions_with_rssd**](InstitutionsApi.md#get_certified_institutions_with_rssd) | **GET** /institution/v2/certifiedInstitutions/rssd | Get Certified Institutions With RSSD
[**get_institution**](InstitutionsApi.md#get_institution) | **GET** /institution/v2/institutions/{institutionId} | Get Institution by ID
[**get_institution_branding**](InstitutionsApi.md#get_institution_branding) | **GET** /institution/v2/institutions/{institutionId}/branding | Get Institution Branding by ID
[**get_institutions**](InstitutionsApi.md#get_institutions) | **GET** /institution/v2/institutions | Get Institutions


# **get_certified_institutions**
> CertifiedInstitutions get_certified_institutions()

Get Certified Institutions

Search for financial institutions by certified product.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import institutions_api
from openapi_client.model.certified_institutions import CertifiedInstitutions
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
    api_instance = institutions_api.InstitutionsApi(api_client)
    search = "finbank" # str | Search term (financial institution `name` field). Leave empty for all FIs. (optional)
    start = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    limit = 1 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 25
    type = "voa" # str | A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\" (optional)
    supported_countries = [
        "us",
    ] # [str] | A list of country codes, '*' for all countries. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Certified Institutions
        api_response = api_instance.get_certified_institutions(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstitutionsApi->get_certified_institutions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term (financial institution &#x60;name&#x60; field). Leave empty for all FIs. | [optional]
 **start** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 25
 **type** | **str**| A product type: \&quot;transAgg\&quot;, \&quot;ach\&quot;, \&quot;stateAgg\&quot;, \&quot;voi\&quot;, \&quot;voa\&quot;, \&quot;aha\&quot;, \&quot;availBalance\&quot;, \&quot;accountOwner\&quot; | [optional]
 **supported_countries** | **[str]**| A list of country codes, &#39;*&#39; for all countries. | [optional]

### Return type

[**CertifiedInstitutions**](CertifiedInstitutions.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institutions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certified_institutions_with_rssd**
> CertifiedInstitutions get_certified_institutions_with_rssd()

Get Certified Institutions With RSSD

Search for certified financial institutions w/RSSD.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import institutions_api
from openapi_client.model.certified_institutions import CertifiedInstitutions
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
    api_instance = institutions_api.InstitutionsApi(api_client)
    search = "finbank" # str | Search term (financial institution `name` field). Leave empty for all FIs. (optional)
    start = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    limit = 1 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 25
    type = "voa" # str | A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\" (optional)
    supported_countries = [
        "us",
    ] # [str] | A list of country codes, '*' for all countries. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Certified Institutions With RSSD
        api_response = api_instance.get_certified_institutions_with_rssd(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstitutionsApi->get_certified_institutions_with_rssd: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term (financial institution &#x60;name&#x60; field). Leave empty for all FIs. | [optional]
 **start** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 25
 **type** | **str**| A product type: \&quot;transAgg\&quot;, \&quot;ach\&quot;, \&quot;stateAgg\&quot;, \&quot;voi\&quot;, \&quot;voa\&quot;, \&quot;aha\&quot;, \&quot;availBalance\&quot;, \&quot;accountOwner\&quot; | [optional]
 **supported_countries** | **[str]**| A list of country codes, &#39;*&#39; for all countries. | [optional]

### Return type

[**CertifiedInstitutions**](CertifiedInstitutions.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institutions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institution**
> InstitutionWrapper get_institution(institution_id)

Get Institution by ID

Get financial institution details by ID.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import institutions_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.institution_wrapper import InstitutionWrapper
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
    api_instance = institutions_api.InstitutionsApi(api_client)
    institution_id = 4222 # int | The institution ID

    # example passing only required values which don't have defaults set
    try:
        # Get Institution by ID
        api_response = api_instance.get_institution(institution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstitutionsApi->get_institution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **int**| The institution ID |

### Return type

[**InstitutionWrapper**](InstitutionWrapper.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institution was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institution_branding**
> BrandingWrapper get_institution_branding(institution_id)

Get Institution Branding by ID

Return the branding information for a financial institution.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import institutions_api
from openapi_client.model.branding_wrapper import BrandingWrapper
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
    api_instance = institutions_api.InstitutionsApi(api_client)
    institution_id = 4222 # int | The institution ID

    # example passing only required values which don't have defaults set
    try:
        # Get Institution Branding by ID
        api_response = api_instance.get_institution_branding(institution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstitutionsApi->get_institution_branding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **int**| The institution ID |

### Return type

[**BrandingWrapper**](BrandingWrapper.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institution branding was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institutions**
> Institutions get_institutions()

Get Institutions

Search for financial institutions.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import institutions_api
from openapi_client.model.institutions import Institutions
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
    api_instance = institutions_api.InstitutionsApi(api_client)
    search = "finbank" # str | Search term (financial institution `name` field). Leave empty for all FIs. (optional)
    start = 1 # int | Index of the page of results to return (optional) if omitted the server will use the default value of 1
    limit = 1 # int | Maximum number of results per page (optional) if omitted the server will use the default value of 25
    type = "voa" # str | A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\" (optional)
    supported_countries = [
        "us",
    ] # [str] | A list of country codes, '*' for all countries. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Institutions
        api_response = api_instance.get_institutions(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstitutionsApi->get_institutions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term (financial institution &#x60;name&#x60; field). Leave empty for all FIs. | [optional]
 **start** | **int**| Index of the page of results to return | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Maximum number of results per page | [optional] if omitted the server will use the default value of 25
 **type** | **str**| A product type: \&quot;transAgg\&quot;, \&quot;ach\&quot;, \&quot;stateAgg\&quot;, \&quot;voi\&quot;, \&quot;voa\&quot;, \&quot;aha\&quot;, \&quot;availBalance\&quot;, \&quot;accountOwner\&quot; | [optional]
 **supported_countries** | **[str]**| A list of country codes, &#39;*&#39; for all countries. | [optional]

### Return type

[**Institutions**](Institutions.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institutions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

