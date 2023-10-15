# ReportInstitutionAccount

An account record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the account | 
**name** | **str** | The account name from the institution | 
**number** | **str** | The account number from the institution (all digits except the last four are obfuscated) | 
**type** | **str** | One of the values from account types | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt | 
**transactions** | [**[ReportTransactionNewTxBased]**](ReportTransactionNewTxBased.md) | a list of transaction records | 
**owner_name** | **str** | The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report. | [optional] 
**current_balance** | **float** | Current balance of the account | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**balance_date** | **int** | A timestamp showing when the balance was captured | [optional] 
**cash_flow_balance** | [**CashFlowCashFlowBalance**](CashFlowCashFlowBalance.md) |  | [optional] 
**cash_flow_credit** | [**CashFlowCashFlowCredit**](CashFlowCashFlowCredit.md) |  | [optional] 
**cash_flow_debit** | [**CashFlowCashFlowDebit**](CashFlowCashFlowDebit.md) |  | [optional] 
**cash_flow_characteristic** | [**CashFlowCashFlowCharacteristic**](CashFlowCashFlowCharacteristic.md) |  | [optional] 
**balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**average_monthly_balance** | **float** | The average monthly balance of this account | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_account** | **int** | The count for the total number of insufficient funds transactions, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_over6_months_account** | **int** | The total number of  insufficient funds fees for the account over six months | [optional] 
**tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account** | **int** | The number of days since the most recent insufficient funds transaction, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**asset** | [**PrequalificationReportAssetSummary**](PrequalificationReportAssetSummary.md) |  | [optional] 
**details** | [**AccountDetailsTxBased**](AccountDetailsTxBased.md) |  | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_over2_months_account** | **int** | The count for the total number of insufficient funds transactions for the last two months, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**position** | [**ReportAccountPosition**](ReportAccountPosition.md) |  | [optional] 
**income_streams** | [**[VOIETXVerifyReportIncomeStream]**](VOIETXVerifyReportIncomeStream.md) | A list of income stream records | [optional] 
**beginning_balance** | **float** | Beginning balance of account per the time period in the report | [optional] 
**misc_deposits** | [**[ReportTransaction]**](ReportTransaction.md) | A list of miscellaneous deposits | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


