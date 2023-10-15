# PayrollEmploymentHistoryVOIE


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_date** | **int** | The last time the payroll data was updated in the payroll provider&#39;s system | 
**employer_name** | **str** | Name of the employer as stated by the employer in the payroll system | 
**payroll_source** | **str** | The name of the payroll source where the data was retrieved | 
**employee** | [**PayrollEmployeeRecord**](PayrollEmployeeRecord.md) |  | 
**employment** | [**PayrollEmploymentRecord**](PayrollEmploymentRecord.md) |  | 
**income** | [**PayrollVOIEIncomeRecord**](PayrollVOIEIncomeRecord.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


