# AppFinancialInstitutionStatus

The registration status fields for each specific OAuth financial institution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of a financial institution, represented as a number | 
**decryption_key_activated** | **bool** | Status of decryption keys for financial institution app registration | 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**last_modified_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**status** | **bool** | \&quot;false\&quot; indicates registration is still pending | 
**abbrv_name** | **str** | The application&#39;s abbreviated name | [optional] 
**logo_url** | **str** | An URL to a logo file | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


