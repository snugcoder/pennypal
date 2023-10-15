# ObbAccountDetails

Details of the account and financial institution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_owner** | [**ObbAccountOwner**](ObbAccountOwner.md) |  | 
**id** | **int** | An account ID represented as a number | 
**institution** | [**ObbInstitution**](ObbInstitution.md) |  | 
**account_number_display** | **str** | The account number from a financial institution in truncated format | [optional] 
**aggregation_attempt_date** | **str** | A timestamp showing the last aggregation attempt. This will not be present until you have run your first aggregation for the account. | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt. This will not be present until you have run your first aggregation for the account | [optional] 
**aggregation_success_date** | **str** | A timestamp showing the last successful aggregation of the account. This will not be present until you have run your first aggregation for the account. | [optional] 
**currency** | **str** | The currency of the account | [optional] 
**current_balance** | **float** | Current reported balance of the account | [optional] 
**institution_login_id** | **int** | An institution login ID (from the account record), represented as a number | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**real_account_number_last4** | **int** | The last 4 digits of the ACH account number | [optional] 
**status** | **str** | pending during account discovery, always active following successful account activation | [optional] 
**type** | **str** | Account type, e.g. checking/saving | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


