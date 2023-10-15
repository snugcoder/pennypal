# Transactions

A list of transactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **int** | The total number of results matching search criteria | 
**displaying** | **int** | The number of results returned | 
**more_available** | **bool** | If the value of &#x60;moreAvailable&#x60; is \&quot;true\&quot;, you can retrieve the next page of results by increasing the value of the start parameter in your next request:\&quot;...&amp;start&#x3D;6&amp;limit&#x3D;5\&quot; | 
**from_date** | **int** | Value of the &#x60;fromDate&#x60; request parameter that generated this response | 
**to_date** | **int** | Value of the &#x60;toDate&#x60; request parameter that generated this response | 
**sort** | **str** | Value of the sort request parameter that generated this response | 
**transactions** | [**[Transaction]**](Transaction.md) | The array of transactions | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


