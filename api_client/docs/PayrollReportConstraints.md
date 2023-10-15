# PayrollReportConstraints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_data** | [**PayrollData**](PayrollData.md) |  | 
**report_custom_fields** | [**ReportCustomFields**](ReportCustomFields.md) |  | [optional] 
**pay_statements_from_date** | **int** | Limits the pay statement history in the VOIE - Payroll report income record. Pay statements are only included if the payDate of the statement is equal to or greater than the start date requested. Date should be in Unix epoch time (in seconds). See: Handling Epoch Dates and Times. | [optional] 
**market_segment** | **str** | Use case for requesting the consumer&#39;s data. Current supported enumerations are \&quot;Mortgage\&quot; and \&quot;KYC\&quot;. If your use case doesn&#39;t match one of these please reach out to your technical point of contact. | [optional] 
**exclude_emp_info** | **bool** | Only used on an exception basis for clients that need to exclude EmpInfo data from the VOE-Payroll or VOIE-Payroll report. If true is passed EmpInfo payroll provider&#39;s data will not be searched or returned. | [optional] 
**purpose** | **str** | FCRA required 2-digit Permissible Purpose Code, specifying the reason for retrieving this report. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


