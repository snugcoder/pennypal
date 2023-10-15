# VOIETXVerifyReportIncomeStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Finicity&#39;s income stream ID | 
**name** | **str** | A human-readable name based on the &#x60;normalizedPayee&#x60; name of the transactions for this income stream | 
**status** | **str** | Possible values: \&quot;ACTIVE\&quot;, \&quot;INACTIVE\&quot; | 
**confidence** | **int** | Level of confidence that the deposit stream represents income (example: 85%) | 
**cadence** | [**CadenceDetails**](CadenceDetails.md) |  | 
**transactions** | [**[ReportTransaction]**](ReportTransaction.md) | A list of transaction records | 
**net_monthly** | [**[NetMonthly]**](NetMonthly.md) | A list of net monthly records. One instance for each complete calendar month in the report. | [optional] 
**net_annual** | **float** | Sum of all values in &#x60;netMonthlyIncome&#x60; over the previous 12 months | [optional] 
**projected_net_annual** | **float** | Projected net income over the next 12 months, across all income streams, based on &#x60;netAnnualIncome&#x60; | [optional] 
**estimated_gross_annual** | **float** | Before-tax gross annual income (estimated from &#x60;netAnnual&#x60;) across all income stream in the past 12 months | [optional] 
**projected_gross_annual** | **float** | Projected gross income over the next 12 months, across all active income streams, based on &#x60;projectedNetAnnual&#x60; | [optional] 
**average_monthly_income_net** | **float** | Monthly average amount over the previous 24 months | [optional] 
**income_stream_months** | **int** | The number of months the income transactions are observed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


