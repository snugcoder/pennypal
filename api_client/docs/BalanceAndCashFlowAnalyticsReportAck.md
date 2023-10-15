# BalanceAndCashFlowAnalyticsReportAck

Response given when analtyics were generated successfully, providing the caller with a report ID which can be used to retrieve the report as JSON or a PDF.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[int]** | List of account IDs included in the report | 
**created_date** | **str** | Created date of balance analytics request | 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**report_id** | **str** | A report ID | 
**report_pin** | **str** | PIN that may be used to access the report | 
**title** | **str** | Title of the report | 
**business_id** | **int** | Business ID associated with the requested customer | [optional] 
**requester_name** | **str** | Name of requester | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


