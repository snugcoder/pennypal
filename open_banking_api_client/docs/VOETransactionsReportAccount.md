# VOETransactionsReportAccount


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
**income_streams** | [**[VOETransactionsReportIncomeStream]**](VOETransactionsReportIncomeStream.md) | A list of income stream records | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


