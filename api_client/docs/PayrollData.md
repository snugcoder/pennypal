# PayrollData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssn** | **str** | The consumer&#39;s full SSN without hyphens | 
**dob** | **int** | The consumer&#39;s date of birth in Unix epoch time (in seconds). See: Handling Epoch Dates and Times. The timestamp should be set at the start of day of birth. | 
**report_id** | **str** | The report ID of the original payroll report for refresh use cases. If used, only the employment records from the original report will be included in the refreshed report response. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


