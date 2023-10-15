# PrequalificationReportAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** | The &#x60;postedDate&#x60; of the earliest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**end_date** | **int** | The &#x60;postedDate&#x60; of the latest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**days** | **int** | The number of days covered by the report | [optional] 
**seasoned** | **bool** | \&quot;true\&quot; if the report covers more than 180 days | [optional] 
**consolidated_available_balance** | **float** | The sum of available balance for all of the accounts included in the report | [optional] 
**institutions** | [**[ReportInstitution]**](ReportInstitution.md) | A list of institution records, including information about the individual accounts in this report | [optional] 
**assets** | [**PrequalificationReportAssetSummary**](PrequalificationReportAssetSummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


