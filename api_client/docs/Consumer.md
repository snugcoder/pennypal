# Consumer

A finicity consumer record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | 
**first_name** | **str** | The first name of the account holder | 
**last_name** | **str** | The last name of the account holder | 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**address** | **str** | A street address | 
**city** | **str** | City | 
**state** | **str** | State | 
**zip** | **str** | A ZIP code | 
**phone** | **str** | A phone number (max length 15). | 
**ssn** | **str** | Last 4 digits of a SSN | 
**birthday** | [**Birthday**](Birthday.md) |  | 
**email** | **str** | An email address | 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**suffix** | **str** | A generational or academic suffix | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


