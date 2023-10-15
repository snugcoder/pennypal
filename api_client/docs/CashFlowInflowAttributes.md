# CashFlowInflowAttributes

Inflow Attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_deposits_by_month_for_the_report_time_period** | [**[ObbDateRangeAndCount]**](ObbDateRangeAndCount.md) | Count of all deposits during periods in the report | 
**historic_count_of_deposit_transactions** | **int** | Count of ALL deposits over entire known history of the account (may exceed requested length of report) | 
**maximum_deposit_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Maximum deposit value for different periods in the report | 
**minimum_deposit_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Minimum deposit value for different periods in the report | 
**sum_deposits_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Sum of all deposits during periods in the report | 
**average_deposit_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average value of deposits during periods in the report | [optional] 
**historic_sum_of_deposits** | **float** | Sum of ALL deposits over entire known history of the account (may exceed requested length of report) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


