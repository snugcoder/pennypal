# AppStatuses

The response for the Get App Registration Status API which returns an array of status objects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_records** | **int** | The total number of results | 
**total_pages** | **int** | The total number of pages | 
**page_number** | **int** | The current page number | 
**number_of_records_per_page** | **int** | The number of results per page | 
**applications** | [**[AppStatus]**](AppStatus.md) | A list of applications with their statuses | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


