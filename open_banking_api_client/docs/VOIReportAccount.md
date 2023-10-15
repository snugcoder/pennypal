# VOIReportAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the account | [optional] 
**number** | **str** | The account number from the institution (all digits except the last four are obfuscated) | [optional] 
**owner_name** | **str** | The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report. | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**type** | **str** | One of the values from account types | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt | [optional] 
**income_streams** | [**[VOIReportIncomeStream]**](VOIReportIncomeStream.md) | A list of income stream records | [optional] 
**balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**average_monthly_balance** | **float** | The average monthly balance of this account | [optional] 
**transactions** | [**[ReportTransaction]**](ReportTransaction.md) | a list of transaction records | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**current_balance** | **float** | Current balance of the account | [optional] 
**beginning_balance** | **float** | Beginning balance of account per the time period in the report | [optional] 
**misc_deposits** | [**[ReportTransaction]**](ReportTransaction.md) | A list of miscellaneous deposits | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


