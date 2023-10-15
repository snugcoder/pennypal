# TransactionsReportConstraintsOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | [**ReportAccountIds**](ReportAccountIds.md) |  | [optional] 
**from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**to_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**include_pending** | **bool** | If pending transactions must be included | [optional]  if omitted the server will use the default value of False
**report_custom_fields** | [**ReportCustomFields**](ReportCustomFields.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


