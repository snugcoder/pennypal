# CashFlowReportConstraints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **str** | A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set) | [optional] 
**report_custom_fields** | [**ReportCustomFields**](ReportCustomFields.md) |  | [optional] 
**show_nsf** | **bool** | Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee | [optional] 
**from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**income_stream_confidence_minimum** | **int** | Include income streams in the report, based on the income stream&#39;s confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


