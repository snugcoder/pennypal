# BalanceAndCashFlowAnalyticsReportConstraints

Request parameters from the partner to control the customer accounts included in the report, and the length of time to report on.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[int]** | The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used. | [optional] 
**length_of_report** | **int** | Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


