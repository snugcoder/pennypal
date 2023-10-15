# ThirdPartyAccessKeyData

An object representing the third party access key request  * `customerId`: This is recipient's customer identifier * `partnerId`: This is recipient partner identifier * `thirdPartyPartnerId`: This is requester's partner identifier * `products`: Array of values representing the Mastercard Open Banking APIs for which access needs to be generated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.finicity.com/admin) | 
**third_party_partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.finicity.com/admin) | 
**products** | [**[ThirdPartyAccessProduct]**](ThirdPartyAccessProduct.md) |  | 
**provenance** | [**ThirdPartyAccessProvenance**](ThirdPartyAccessProvenance.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


