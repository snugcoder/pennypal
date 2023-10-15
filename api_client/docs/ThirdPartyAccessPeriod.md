# ThirdPartyAccessPeriod

Object which describes access validity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Multiple types will be supported. Presently below types are supported. * \&quot;timeframe\&quot;: Specifies a timeframe bounded by a startTime and endTime.     The startTime is the time at which the access was granted and the access key generated,    and the endTime is the time at which the access was revoked. Times are represented in ISO 8601 format(\&quot;2022-03-10T06:06:20Z\&quot;) | 
**start_time** | **datetime** | A date-time with time zone | 
**end_time** | **datetime** | A date-time with time zone | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


