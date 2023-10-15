# CashFlowTransactionAnalyticsAttributes

Transaction Analytics Attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_deposits_credits_for_the_report_time_period** | [**[CashFlowActivityDepositsCredits]**](CashFlowActivityDepositsCredits.md) | List of all deposit transactions posted to the account during the report period | 
**activity_withdrawals_debits_for_the_report_time_period** | [**[CashFlowActivityWithdrawalsDebits]**](CashFlowActivityWithdrawalsDebits.md) | List of all withdrawal transactions posted to the account during the report period | 
**average_transaction_value_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average value of transactions during periods in the report. Values may be positive or negative | 
**historic_weeks_with_zero_transactions** | [**CashFlowNumWeeksZeros**](CashFlowNumWeeksZeros.md) |  | [optional] 
**last_transaction_date** | [**[CashFlowTransactionAnalyticsAttributesLastTransactionDate]**](CashFlowTransactionAnalyticsAttributesLastTransactionDate.md) | Latest posted transaction(s) to the account. May be more than one if they share the same timestamp | [optional] 
**net_cash_flow_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Net cash flow for each month during the report period | [optional] 
**net_cash_flow_for_the_report_time_period** | **float** | Net cash flow during the report period (may be positive or negative) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


