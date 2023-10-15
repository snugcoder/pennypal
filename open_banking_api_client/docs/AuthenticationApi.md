# openapi_client.AuthenticationApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](AuthenticationApi.md#create_token) | **POST** /aggregation/v2/partners/authentication | Create Access Token
[**modify_partner_secret**](AuthenticationApi.md#modify_partner_secret) | **PUT** /aggregation/v2/partners/authentication | Modify Partner Secret


# **create_token**
> AccessToken create_token(partner_credentials)

Create Access Token

Send Partner ID and Partner Secret to the Partner Authentication service to obtain a token for accessing Finicity APIs. * The token is valid for two hours and is required on all calls to the Finicity APIs * As a best practice, use a single token for all calls. Assign a timestamp for each token, and then check the current timestamp before making any calls. If the token is greater than 90 minutes, generate a new one. * ⚠️ After five failed attempts to authenticate, your account will be locked. Contact [support@finicity.com](mailto:support@finicity.com) to get help resetting your account.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.access_token import AccessToken
from openapi_client.model.partner_credentials import PartnerCredentials
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    partner_credentials = PartnerCredentials(
        partner_id="1234583871234",
        partner_secret="aqJ5Ic4SEVx2IgDQ6oR4",
    ) # PartnerCredentials | 

    # example passing only required values which don't have defaults set
    try:
        # Create Access Token
        api_response = api_instance.create_token(partner_credentials)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_credentials** | [**PartnerCredentials**](PartnerCredentials.md)|  |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access token was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check Partner ID, Partner Secret or Finicity-App-Key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_partner_secret**
> modify_partner_secret(partner_credentials_with_new_secret)

Modify Partner Secret

Change the Partner Secret used to authenticate this partner.  The secret does not expire, but can be changed by calling this API. A valid Partner Secret may contain upper and lowercase characters, numbers, and the characters !, @, #, $, %, &, *, _, -, +. It must include at least one number and at least one letter, and its length should be between 12 and 255 characters.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.partner_credentials_with_new_secret import PartnerCredentialsWithNewSecret
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    partner_credentials_with_new_secret = PartnerCredentialsWithNewSecret() # PartnerCredentialsWithNewSecret | 

    # example passing only required values which don't have defaults set
    try:
        # Modify Partner Secret
        api_instance.modify_partner_secret(partner_credentials_with_new_secret)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->modify_partner_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_credentials_with_new_secret** | [**PartnerCredentialsWithNewSecret**](PartnerCredentialsWithNewSecret.md)|  |

### Return type

void (empty response body)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Partner Secret was successfully updated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check Partner ID, Partner Secret or Finicity-App-Key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

