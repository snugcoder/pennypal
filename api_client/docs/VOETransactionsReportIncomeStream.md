# VOETransactionsReportIncomeStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Income stream ID | 
**name** | **str** | A human-readable name based on the &#x60;normalizedPayee&#x60; name of the transactions for this income stream | 
**status** | **str** | Possible values: \&quot;ACTIVE\&quot;, \&quot;INACTIVE\&quot; | 
**estimate_inclusion** | **str** | Possible values: \&quot;HIGH\&quot;, \&quot;MODERATE\&quot;, \&quot;LOW\&quot;, \&quot;NO\&quot; | 
**confidence** | **int** | Level of confidence that the deposit stream represents income (example: 85%) | 
**cadence** | [**CadenceDetails**](CadenceDetails.md) |  | 
**days_since_last_transaction** | **int** | The number of days since the last credit transaction for the particular income stream | 
**next_expected_transaction_date** | **int** | The next expected credit transaction date for the particular income stream, based on the cadence | 
**transactions** | [**[ReportTransaction]**](ReportTransaction.md) | A list of transaction records | 
**income_stream_months** | **int** | The number of months the income transactions are observed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


