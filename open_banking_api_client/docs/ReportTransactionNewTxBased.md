# ReportTransactionNewTxBased


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A transaction ID | 
**posted_date** | **int** | A timestamp showing when the transaction was posted or cleared by the institution | 
**description** | **str** | The description of the transaction, as provided by the institution (often known as &#x60;payee&#x60;). In the event that this field is left blank by the institution, Finicity will pass a value of \&quot;No description provided by institution\&quot;. All other values are provided by the institution. | 
**amount** | **float** | The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values. | [optional] 
**memo** | **str** | The memo field of the transaction, as provided by the institution. The institution must provide either a description, a memo, or both. It is recommended to concatenate the two fields into a single value. | [optional] 
**investment_transaction_type** | **str** | Keywords in the description and memo fields were used to translate investment transactions into these types  * &#x60;cancel&#x60;  * &#x60;purchaseToClose&#x60;  * &#x60;purchasetoCover&#x60;  * &#x60;contribution&#x60;  * &#x60;optionExercise&#x60;  * &#x60;optionExpiration&#x60;  * &#x60;fee&#x60;  * &#x60;soldToClose&#x60;  * &#x60;soldToOpen&#x60;  * &#x60;split&#x60;  * &#x60;transfer&#x60;  * &#x60;returnOfCapital&#x60;  * &#x60;income&#x60;  * &#x60;purchased&#x60;  * &#x60;sold&#x60;  * &#x60;dividendreInvest&#x60;  * &#x60;dividend&#x60;  * &#x60;reinvestOfIncome&#x60;  * &#x60;interest&#x60;  * &#x60;deposit&#x60;  * &#x60;otherInfo&#x60;  | [optional] 
**normalized_payee** | **str** | A normalized payee, derived from the transaction&#39;s &#x60;description&#x60; and &#x60;memo&#x60; fields | [optional] 
**institution_transaction_id** | **str** | The unique identifier given by the FI for each transaction | [optional] 
**category** | **str** | One of the values from Categories (assigned based on the payee name) | [optional] 
**type** | **str** | One of the values from transaction types | [optional] 
**security_type** | **str** | The type of investment security (VOA only) | [optional] 
**symbol** | **str** | Investment symbol (VOA only) | [optional] 
**commission** | **float** | A commission amount | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


