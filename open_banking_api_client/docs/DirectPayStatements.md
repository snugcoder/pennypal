# DirectPayStatements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_pay_history_id** | **str** | An ID for the income and employment details for the given pay period | 
**last_pay_period_indicator** | **bool** | Most recent available pay check | 
**main_pay_statement_fields** | [**MainPayStatementFields**](MainPayStatementFields.md) |  | 
**earnings** | [**[Earnings]**](Earnings.md) | Categorization of pay, for the pay period | 
**deductions** | [**[Deductions]**](Deductions.md) | Deductions from the pay check | [optional] 
**direct_deposits** | [**[DirectDeposits]**](DirectDeposits.md) | Direct deposit information for the paycheck | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


