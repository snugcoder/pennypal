# openapi_client.PayStatementsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_customer_pay_statement**](PayStatementsApi.md#store_customer_pay_statement) | **POST** /aggregation/v1/customers/{customerId}/payStatements | Store Customer Pay Statement


# **store_customer_pay_statement**
> Asset store_customer_pay_statement(customer_id, pay_statement)

Store Customer Pay Statement

Upload pay statements for a customer.  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppKey):
* Api Key Authentication (FinicityAppToken):

```python
import time
import openapi_client
from openapi_client.api import pay_statements_api
from openapi_client.model.pay_statement import PayStatement
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.asset import Asset
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
    api_instance = pay_statements_api.PayStatementsApi(api_client)
    customer_id = "1005061234" # str | A customer ID
    pay_statement = PayStatement(
        label="lastPayPeriod",
        statement="VGhpcyBtdXN0IGJlIGFuIGltYWdl",
    ) # PayStatement | 

    # example passing only required values which don't have defaults set
    try:
        # Store Customer Pay Statement
        api_response = api_instance.store_customer_pay_statement(customer_id, pay_statement)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PayStatementsApi->store_customer_pay_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID |
 **pay_statement** | [**PayStatement**](PayStatement.md)|  |

### Return type

[**Asset**](Asset.md)

### Authorization

[FinicityAppKey](../README.md#FinicityAppKey), [FinicityAppToken](../README.md#FinicityAppToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pay statement was successfully uploaded |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

