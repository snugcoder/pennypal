# MainPayStatementFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_date** | **int** | Pay date for the pay period | 
**gross_pay_amount** | **float** | Gross pay amount for the pay period | 
**start_date** | **int** | Start date for the pay period | [optional] 
**end_date** | **int** | End date for the pay period | [optional] 
**pay_period_hours** | **float** | Sum of all hours worked each week for the pay period | [optional] 
**pay_frequency** | **str** | The current pay frequency, or how often a regular pay check is   distributed:  * &#x60;Daily&#x60;  * &#x60;Weekly&#x60;  * &#x60;Bi-Weekly&#x60;  * &#x60;Semi-Monthly&#x60;  * &#x60;Monthly&#x60;  * &#x60;Quarterly&#x60;  * &#x60;Semi-Annual&#x60;  * &#x60;Annual&#x60;  * &#x60;Every 2.6 wks&#x60;  * &#x60;Every 4 wks&#x60;  * &#x60;Every 5.2 wks&#x60;  * &#x60;Other&#x60;  | [optional] 
**pay_type** | **str** | Current pay type:  * &#x60;Salary&#x60;  * &#x60;Hourly&#x60;  * &#x60;Daily&#x60;  | [optional] 
**gross_pay_amount_ytd** | **float** | Year to date (YTD) gross pay amount at the time of payment | [optional] 
**net_pay_amount** | **float** | Net pay amount for a pay period | [optional] 
**net_pay_amount_ytd** | **float** | Year to date (YTD) net pay amount at the time of payment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


