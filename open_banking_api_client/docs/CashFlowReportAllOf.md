# CashFlowReportAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** | The &#x60;postedDate&#x60; of the earliest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**end_date** | **int** | The &#x60;postedDate&#x60; of the latest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**days** | **int** | Number of days covered by the report | [optional] 
**seasoned** | **bool** | \&quot;true\&quot; if the report covers more than 365 days | [optional] 
**institutions** | [**[ReportInstitution]**](ReportInstitution.md) | A list of institution records, including information about the individual accounts used in this report | [optional] 
**cash_flow_balance_summary** | [**CashFlowCashFlowBalanceSummary**](CashFlowCashFlowBalanceSummary.md) |  | [optional] 
**cash_flow_credit_summary** | [**CashFlowCashFlowCreditSummary**](CashFlowCashFlowCreditSummary.md) |  | [optional] 
**cash_flow_debit_summary** | [**CashFlowCashFlowDebitSummary**](CashFlowCashFlowDebitSummary.md) |  | [optional] 
**cash_flow_characteristics_summary** | [**CashFlowCashFlowCharacteristicsSummary**](CashFlowCashFlowCharacteristicsSummary.md) |  | [optional] 
**possible_loan_deposits** | [**[CashFlowPossibleLoanDeposits]**](CashFlowPossibleLoanDeposits.md) | A possible loan deposits record | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


