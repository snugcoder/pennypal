# ErrorMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An error code (can be returned as a number or a string). Useful links: [Common API Status Codes](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/#common-api-status-codes), [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes). | 
**status** | **str** | A status code | [optional] 
**title** | **str** | A title for the error | [optional] 
**level** | **str** | An error level | [optional] 
**message** | **str** | An error message | [optional] 
**user_message** | **str** | Some more details about the error | [optional] 
**asset_id** | **str** | An asset ID. Generated by Connect or by using the Store Customer Pay Statement API. | [optional] 
**account_id** | **str** | An account ID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

