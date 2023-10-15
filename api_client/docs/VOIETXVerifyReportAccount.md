# VOIETXVerifyReportAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the account | 
**number** | **str** | The account number from the institution (all digits except the last four are obfuscated) | 
**name** | **str** | The account name from the institution | 
**type** | **str** | One of the values from account types | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt | 
**transactions** | [**[ReportTransactionNewTxBased]**](ReportTransactionNewTxBased.md) | a list of transaction records | 
**owner_name** | **str** | The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report. | [optional] 
**income_streams** | [**[VOIETXVerifyReportIncomeStream]**](VOIETXVerifyReportIncomeStream.md) | A list of income stream records | [optional] 
**balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**average_monthly_balance** | **float** | The average monthly balance of this account | [optional] 
**details** | [**AccountDetailsTxBased**](AccountDetailsTxBased.md) |  | [optional] 
**position** | [**ReportAccountPosition**](ReportAccountPosition.md) |  | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


