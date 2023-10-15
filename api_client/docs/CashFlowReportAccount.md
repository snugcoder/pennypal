# CashFlowReportAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Finicity account ID | [optional] 
**owner_name** | **str** | The name(s) of the account owner(s), retrieved from the institution. | [optional] 
**owner_address** | **str** | The mailing address of the account owner, retrieved from the institution. | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**number** | **str** | The account number from the institution (obfuscated) | [optional] 
**type** | **str** | CFR: &#x60;ALL&#x60; (&#x60;checking&#x60; / &#x60;savings&#x60; / &#x60;loan&#x60; / &#x60;mortgage&#x60; / &#x60;credit card&#x60; / &#x60;CD&#x60; / &#x60;MM&#x60; / &#x60;investment&#x60;...) | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable) | [optional] 
**current_balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**available_balance** | **float** | Available balance | [optional] 
**balance_date** | **int** | A timestamp showing when the &#x60;balance&#x60; was captured | [optional] 
**transactions** | [**[ReportTransaction]**](ReportTransaction.md) | a list of transaction records | [optional] 
**cash_flow_balance** | [**CashFlowCashFlowBalance**](CashFlowCashFlowBalance.md) |  | [optional] 
**cash_flow_credit** | [**CashFlowCashFlowCredit**](CashFlowCashFlowCredit.md) |  | [optional] 
**cash_flow_debit** | [**CashFlowCashFlowDebit**](CashFlowCashFlowDebit.md) |  | [optional] 
**cash_flow_characteristic** | [**CashFlowCashFlowCharacteristic**](CashFlowCashFlowCharacteristic.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


