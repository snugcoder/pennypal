# ObbAnalyticsReport

Cash Flow or Balance Analytics report data as JSON

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**report_header** | [**ObbReportHeader**](ObbReportHeader.md) |  | 
**title** | **str** | Title of the report | 
**account_results** | [**[BalanceAnalyticsAccountResult]**](BalanceAnalyticsAccountResult.md) | Balance results per account | [optional] 
**business_id** | **int** | Business ID | [optional] 
**business_summary** | [**BalanceAnalyticsBusinessSummary**](BalanceAnalyticsBusinessSummary.md) |  | [optional] 
**requester_name** | **str** | Name of requester | [optional] 
**total_revenue** | **float** | The total revenue | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


