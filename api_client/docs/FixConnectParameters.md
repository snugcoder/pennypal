# FixConnectParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.finicity.com/admin) | 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**institution_login_id** | **str** | An institution login ID (from the account record) | 
**language** | **str** | Generate a translated Connect URL link.   Supported languages:  * English (default) * Spanish (United States): &#x60;es&#x60; * French (Canada): &#x60;fr&#x60; or &#x60;fr-CA&#x60;  | [optional] 
**redirect_uri** | **str** | The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe). | [optional] 
**webhook** | **str** | The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details. | [optional] 
**webhook_content_type** | **str** | The content type the webhook events will be sent in. Supported types: \&quot;application/json\&quot; and \&quot;application/xml\&quot;. | [optional]  if omitted the server will use the default value of "application/json"
**webhook_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**webhook_headers** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**experience** | **str** | The &#x60;experience&#x60; field allows you to customize: * Brand: color and logo * Icon: displayed on the \&quot;Share your data\&quot; page  * Popular institutions: displayed on the Bank Search page  * Report: the credit decisioning report to send when Connect completes.  * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they&#39;ll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options:  * \&quot;default\&quot;: your default experience (must be defined)  * GUID: the code for a different experience * Not defined: If you don&#39;t pass the experience parameter, then Connect&#39;s out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run. | [optional] 
**single_use_url** | **bool** | \&quot;true\&quot;: The URL link expires after a Connect session successfully completes.  Note: when the &#x60;singleUseUrl&#x60; and the &#x60;experience&#x60; parameters are passed in the same call, the &#x60;singleUseUrl&#x60; value overrides the &#x60;singleUseUrl&#x60; value configured in the &#x60;experience&#x60; parameter. | [optional] 
**is_web_view** | **bool** | \&quot;true\&quot;: Indicates that the Connect Session will be displayed within a WebView. Note: when the &#x60;isWebView&#x60; parameter is &#x60;true&#x60; the &#x60;redirectUri&#x60; parameter is required. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


