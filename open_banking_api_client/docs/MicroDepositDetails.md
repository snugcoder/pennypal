# MicroDepositDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The following values may be returned in the field of a status:  * \&quot;Pending\&quot; : Micro entries not yet deposited to customer&#39;s account * \&quot;Completed\&quot;: Micro entries deposited to customer&#39;s account * \&quot;Verified\&quot;: Micro entries got successfully verified * \&quot;Rejected\&quot;: Micro entries got rejected due to some reason * \&quot;Returned\&quot;: Micro entries got returned back * \&quot;Failed\&quot;: Micro entries got failed due to some reason * \&quot;Expired\&quot;: Micro entries got expired as they remains unverified for certain defined days | [optional] 
**status_description** | **str** | Micro entries status description | [optional] 
**creation_date** | **str** | A date-time without time zone | [optional] 
**routing_number** | **str** | Routing number of receiving bank | [optional] 
**account_number_last4** | **str** | The last 4 digits of the ACH account number | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


