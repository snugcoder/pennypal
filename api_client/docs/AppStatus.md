# AppStatus

Registration status details for the application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.finicity.com/admin) | 
**pre_app_id** | **str** | Identifier to track the application registration from the App Registration and Get App Registration Status APIs | 
**app_name** | **str** | The name of the application assigned to the customer | 
**submitted_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**modified_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**status** | **str** | The status of an app registration request. \&quot;A\&quot; means approved. \&quot;P\&quot; means pending which is the status when initially submitted or when the app is modified and awaiting approval. \&quot;R\&quot; means rejected. If it is rejected there will be a note with the rejected reason. | 
**note** | **str** | A note on the registration. Typically used to indicate reasons for rejected apps. | [optional] 
**application_id** | **str** | &#x60;applicationId&#x60; value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved. | [optional] 
**scopes** | **str** | Indicates scopes of data accessible to the app | [optional] 
**institution_details** | [**[AppFinancialInstitutionStatus]**](AppFinancialInstitutionStatus.md) | A list of the registration status for each FI for the application | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


