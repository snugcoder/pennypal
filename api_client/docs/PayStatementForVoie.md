# PayStatementForVoie


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **bool** | This will display true if the pay statement is billable. If a pay statement has been digitized previously, this will display as false as it will not be billable. | 
**asset_id** | **str** | The asset ID of the stored pay statement | 
**employer** | [**Employer**](Employer.md) |  | 
**employee** | [**Employee**](Employee.md) |  | 
**pay_stat** | [**[PayStat]**](PayStat.md) | Information pertaining to the earnings on the pay statement | 
**institutions** | **[str]** | Not populated for the voieWithStatement style of paystub report. For the VOIE - Paystub (with TXVerify) reports this would include details of the financial institution accounts and income streams with matching transactions to the pay statement. | 
**pay_period** | **str** | The pay period of the pay statement | [optional] 
**pay_date** | **int** | The listed pay date for the pay statement | [optional] 
**start_date** | **int** | The beginning of the pay period | [optional] 
**end_date** | **int** | The end of the pay period | [optional] 
**net_pay_current** | **float** | The total pay after deductions for the employee for the current pay period | [optional] 
**net_pay_ytd** | **float** | The total accumulation of pay after deductions for the employee for the current pay year | [optional] 
**gross_pay_current** | **float** | The total pay before deductions for the employee for the current pay period | [optional] 
**gross_pay_ytd** | **float** | The total accumulation of pay before deductions for the employee for the current pay year | [optional] 
**payroll_provider** | **str** | The payroll provider extracted from the pay statement | [optional] 
**direct_deposits** | [**[DirectDeposit]**](DirectDeposit.md) | Information pertaining to the direct deposits on the pay statement | [optional] 
**error_code** | **int** | Error code for the asset | [optional] 
**error_message** | **str** | Error message for the asset | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


