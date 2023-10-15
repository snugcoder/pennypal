# ReportTransactionBase2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normalized_payee** | **str** | A normalized payee, derived from the transaction&#39;s &#x60;description&#x60; and &#x60;memo&#x60; fields | [optional] 
**institution_transaction_id** | **str** | The unique identifier given by the FI for each transaction | [optional] 
**category** | **str** | One of the values from Categories (assigned based on the payee name) | [optional] 
**type** | **str** | One of the values from transaction types | [optional] 
**security_type** | **str** | The type of investment security (VOA only) | [optional] 
**symbol** | **str** | Investment symbol (VOA only) | [optional] 
**commission** | **float** | A commission amount | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


