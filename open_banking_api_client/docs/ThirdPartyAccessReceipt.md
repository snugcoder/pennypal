# ThirdPartyAccessReceipt

An object representing consent receipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **int** | Representation of the type of consent receipt | [optional] 
**version** | **str** | A schema version of receipt | [optional] 
**receipt_id** | **str** | This is officially the Consent Receipt ID, but is aliased as the Access Key ID. This is a unique identifier managed by Finicity that points to the contents of this JSON document. | [optional] 
**customer_id** | **str** | This is recipient&#39;s customerId represented as a pseudoidentifier | [optional] 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.finicity.com/admin) | [optional] 
**products** | [**[ThirdPartyAccessProduct]**](ThirdPartyAccessProduct.md) |  | [optional] 
**provenance** | [**ThirdPartyAccessProvenance**](ThirdPartyAccessProvenance.md) |  | [optional] 
**timestamp** | **datetime** | A date-time with time zone | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


