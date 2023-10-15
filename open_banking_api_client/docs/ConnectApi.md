# openapi_client.ConnectApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_connect_url**](ConnectApi.md#generate_connect_url) | **POST** /connect/v2/generate | Generate Connect URL
[**generate_fix_connect_url**](ConnectApi.md#generate_fix_connect_url) | **POST** /connect/v2/generate/fix | Generate Fix Connect URL
[**generate_joint_borrower_connect_url**](ConnectApi.md#generate_joint_borrower_connect_url) | **POST** /connect/v2/generate/jointBorrower | Generate Connect URL - Joint Borrower
[**generate_lite_connect_url**](ConnectApi.md#generate_lite_connect_url) | **POST** /connect/v2/generate/lite | Generate Lite Connect URL
[**send_connect_email**](ConnectApi.md#send_connect_email) | **POST** /connect/v2/send/email | Send Connect Email
[**send_joint_borrower_connect_email**](ConnectApi.md#send_joint_borrower_connect_email) | **POST** /connect/v2/send/email/jointBorrower | Send Connect Email - Joint Borrower
[**verify_micro_entry_microdeposit**](ConnectApi.md#verify_micro_entry_microdeposit) | **POST** /connect/v2/generate/microentry/verify | Account Validation Assistant User verification of microdeposits


# **generate_connect_url**
> ConnectUrl generate_connect_url(connect_parameters)

Generate Connect URL

Generate a Connect 2.0 URL link to add within your own applications.  In option, use the `experience` parameter to call Connect (per session) in the body of the request. Configure the `experience` parameter to change the brand color, logo, icon, which credit decisioning report to generate when the Connect application completes, and more.  Note: contact your Sales Account Team to set up the `experience` parameter.  MVS Developers: You can pre-populate the consumer's SSN on the \"Find employment records\" page at the beginning of the MVS payroll app. Pass the SSN value for the consumer in the body of the request call.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.connect_url import ConnectUrl
from openapi_client.model.connect_parameters import ConnectParameters
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
    api_instance = connect__api.ConnectApi(api_client)
    connect_parameters = ConnectParameters(
        language="fr-CA",
        partner_id="1234583871234",
        customer_id="1005061234",
        consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        optional_consumer_info=ConsumerInfo(
            ssn="999999999",
            dob=1607450357,
        ),
        single_use_url=True,
        experience="default",
        institution_settings={},
        from_date=1607450357,
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        is_web_view=True,
    ) # ConnectParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Connect URL
        api_response = api_instance.generate_connect_url(connect_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->generate_connect_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_parameters** | [**ConnectParameters**](ConnectParameters.md)|  |

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_fix_connect_url**
> ConnectUrl generate_fix_connect_url(fix_connect_parameters)

Generate Fix Connect URL

Use the Connect Fix API when the following conditions occur: * The connection to the user's financial institution is lost * The user's credentials were updated (for any number of reasons) * The user's MFA challenge has expired  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.connect_url import ConnectUrl
from openapi_client.model.fix_connect_parameters import FixConnectParameters
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
    api_instance = connect__api.ConnectApi(api_client)
    fix_connect_parameters = FixConnectParameters(
        language="fr-CA",
        partner_id="1234583871234",
        customer_id="1005061234",
        institution_login_id="1007302745",
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        experience="default",
        single_use_url=True,
        is_web_view=True,
    ) # FixConnectParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Fix Connect URL
        api_response = api_instance.generate_fix_connect_url(fix_connect_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->generate_fix_connect_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fix_connect_parameters** | [**FixConnectParameters**](FixConnectParameters.md)|  |

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_joint_borrower_connect_url**
> ConnectUrl generate_joint_borrower_connect_url(connect_joint_borrower_parameters)

Generate Connect URL - Joint Borrower

Same as Connect Full (`POST /connect/v2/generate`) but for joint borrowers.  MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Connect session.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.connect_url import ConnectUrl
from openapi_client.model.connect_joint_borrower_parameters import ConnectJointBorrowerParameters
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
    api_instance = connect__api.ConnectApi(api_client)
    connect_joint_borrower_parameters = ConnectJointBorrowerParameters(
        language="fr-CA",
        partner_id="1234583871234",
        borrowers=Borrowers([
            Borrower(
                customer_id="1005061234",
                consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
                type="primary",
                optional_consumer_info=ConsumerInfo(
                    ssn="999999999",
                    dob=1607450357,
                ),
            ),
        ]),
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        institution_settings={},
        experience="default",
        from_date=1607450357,
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        single_use_url=True,
    ) # ConnectJointBorrowerParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Connect URL - Joint Borrower
        api_response = api_instance.generate_joint_borrower_connect_url(connect_joint_borrower_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->generate_joint_borrower_connect_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_joint_borrower_parameters** | [**ConnectJointBorrowerParameters**](ConnectJointBorrowerParameters.md)|  |

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_lite_connect_url**
> ConnectUrl generate_lite_connect_url(lite_connect_parameters)

Generate Lite Connect URL

Connect Lite is a variation of Connect Full (`POST /connect/v2/generate`), which has a limited set of features. * Sign in, user's credentials, and Multi-Factor Authentication (MFA) * No user account management  The Connect Web SDK isn't a requirement when using Connect lite. However, if you want to use the SDK events, routes, and user events, then you must integrate with the Connect Web SDK.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.connect_url import ConnectUrl
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.lite_connect_parameters import LiteConnectParameters
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
    api_instance = connect__api.ConnectApi(api_client)
    lite_connect_parameters = LiteConnectParameters(
        language="fr-CA",
        partner_id="1234583871234",
        customer_id="1005061234",
        institution_id=4222,
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        experience="default",
        single_use_url=True,
        is_web_view=True,
    ) # LiteConnectParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Lite Connect URL
        api_response = api_instance.generate_lite_connect_url(lite_connect_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->generate_lite_connect_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lite_connect_parameters** | [**LiteConnectParameters**](LiteConnectParameters.md)|  |

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_connect_email**
> ConnectEmailUrl send_connect_email(connect_email_parameters)

Send Connect Email

Same as Connect Full (`POST /connect/v2/generate`) but send a Connect email to a consumer.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.connect_email_url import ConnectEmailUrl
from openapi_client.model.connect_email_parameters import ConnectEmailParameters
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
    api_instance = connect__api.ConnectApi(api_client)
    connect_email_parameters = ConnectEmailParameters(
        language="fr-CA",
        partner_id="1234583871234",
        customer_id="1005061234",
        consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        institution_settings={},
        email=EmailOptions(
            to="bob@example.com",
            _from="test.lender@test.com",
            support_phone="800-555-5555",
            subject="Verify your income",
            first_name="Bob",
            institution_name="Acme Lending",
            institution_address="222 Winipeg Drive SLC UT, 84109",
            signature=["Cindy Mayfield","Senior Loan Officer","Direct 123-456-7890"],
        ),
        experience="default",
        single_use_url=True,
        from_date=1607450357,
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        optional_consumer_info=ConsumerInfo(
            ssn="999999999",
            dob=1607450357,
        ),
    ) # ConnectEmailParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Send Connect Email
        api_response = api_instance.send_connect_email(connect_email_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->send_connect_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_email_parameters** | [**ConnectEmailParameters**](ConnectEmailParameters.md)|  |

### Return type

[**ConnectEmailUrl**](ConnectEmailUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated and the email sent |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_joint_borrower_connect_email**
> ConnectEmailUrl send_joint_borrower_connect_email(connect_joint_borrower_email_parameters)

Send Connect Email - Joint Borrower

Same as Connect Joint Borrower (`POST /connect/v2/generate/jointBorrower`) but send a Connect email  to at least one of the joint borrower's email addresses.   When the consumer opens the email, MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Connect session.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.connect_email_url import ConnectEmailUrl
from openapi_client.model.connect_joint_borrower_email_parameters import ConnectJointBorrowerEmailParameters
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
    api_instance = connect__api.ConnectApi(api_client)
    connect_joint_borrower_email_parameters = ConnectJointBorrowerEmailParameters(
        language="fr-CA",
        partner_id="1234583871234",
        borrowers=Borrowers([
            Borrower(
                customer_id="1005061234",
                consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
                type="primary",
                optional_consumer_info=ConsumerInfo(
                    ssn="999999999",
                    dob=1607450357,
                ),
            ),
        ]),
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        institution_settings={},
        email=EmailOptions(
            to="bob@example.com",
            _from="test.lender@test.com",
            support_phone="800-555-5555",
            subject="Verify your income",
            first_name="Bob",
            institution_name="Acme Lending",
            institution_address="222 Winipeg Drive SLC UT, 84109",
            signature=["Cindy Mayfield","Senior Loan Officer","Direct 123-456-7890"],
        ),
        experience="default",
        from_date=1607450357,
        report_custom_fields=ReportCustomFields([
            ReportCustomField(
                label="loanID",
                value="123456",
                shown=True,
            ),
        ]),
        single_use_url=True,
    ) # ConnectJointBorrowerEmailParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Send Connect Email - Joint Borrower
        api_response = api_instance.send_joint_borrower_connect_email(connect_joint_borrower_email_parameters)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->send_joint_borrower_connect_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_joint_borrower_email_parameters** | [**ConnectJointBorrowerEmailParameters**](ConnectJointBorrowerEmailParameters.md)|  |

### Return type

[**ConnectEmailUrl**](ConnectEmailUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated and the email sent |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_micro_entry_microdeposit**
> ConnectUrl verify_micro_entry_microdeposit(micro_entry_verify_request_parameter)

Account Validation Assistant User verification of microdeposits

The UI re-engages the consumer to enter two microdeposit amounts found in their account and validates them.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import connect__api
from openapi_client.model.connect_url import ConnectUrl
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.micro_entry_verify_request_parameter import MicroEntryVerifyRequestParameter
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
    api_instance = connect__api.ConnectApi(api_client)
    micro_entry_verify_request_parameter = MicroEntryVerifyRequestParameter(
        partner_id="1234583871234",
        customer_id="1005061234",
        redirect_uri="https://www.finicity.com/connect/",
        webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        webhook_content_type="application/json",
        webhook_data={},
        webhook_headers={},
        experience="default",
        account_id="5011648377",
    ) # MicroEntryVerifyRequestParameter | 

    # example passing only required values which don't have defaults set
    try:
        # Account Validation Assistant User verification of microdeposits
        api_response = api_instance.verify_micro_entry_microdeposit(micro_entry_verify_request_parameter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectApi->verify_micro_entry_microdeposit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **micro_entry_verify_request_parameter** | [**MicroEntryVerifyRequestParameter**](MicroEntryVerifyRequestParameter.md)|  |

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

