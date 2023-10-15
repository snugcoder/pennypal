# CashFlowOutflowAttributes

Outflow attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_withdrawals_by_month_for_the_report_time_period** | [**[ObbDateRangeAndCount]**](ObbDateRangeAndCount.md) | Count of all withdrawals during periods in the report | 
**historic_count_of_withdrawal_transactions** | **int** | Count of ALL withdrawals over entire known history of the account (may exceed requested length of report) | 
**maximum_withdrawal_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Maximum withdrawal value for different periods in the report | 
**minimum_withdrawal_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Minimum withdrawal value for different periods in the report | 
**sum_withdrawals_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Sum of all withdrawals during periods in the report | 
**average_withdrawal_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average value of withdrawals during periods in the report | [optional] 
**historic_sum_of_withdrawals** | **float** | Sum of ALL withdrawals over entire known history of the account (may exceed requested length of report) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


