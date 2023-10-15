# PayStatement

A pay statement document and pay statement label

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label to be associated with the pay statement. This label will allow the paystub to go through data extraction. * &#x60;lastPayPeriod&#x60;: default label that should be used for the VOIE - Paystub products * &#x60;lastPayPeriodMinusOne&#x60;: the second most recent pay statement * &#x60;lastPayPeriodMinusTwo&#x60;: the third most recent pay statement * &#x60;previousYearLastPayPeriod&#x60; Last pay statement of the previous calendar year * &#x60;previousYear2LastPayPeriod&#x60;: last pay statement of the calendar year 2 years prior * &#x60;earliestPayPeriod&#x60;: the earliest pay statement | 
**statement** | **str** | A Base64 encoded pay statement file. Finicity supports PDF, JPG, or PNG files. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


