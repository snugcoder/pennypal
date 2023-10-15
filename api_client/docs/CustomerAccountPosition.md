# CustomerAccountPosition

Details for investment account holdings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the investment position | [optional] 
**description** | **str** | The description of the holding | [optional] 
**symbol** | **str** | The investment position&#39;s market ticker symbol | [optional] 
**units** | **float** | The number of units of the holding | [optional] 
**current_price** | **float** | The current price of the investment holding | [optional] 
**security_name** | **str** | The security name for the investment holding | [optional] 
**transaction_type** | **str** | The transaction type of the holding, such as cash, margin, and more | [optional] 
**market_value** | **float** | Market value of an investment position at the time of retrieval | [optional] 
**change_percent** | **float** | The percent change in value since the previous day | [optional] 
**daily_change** | **float** | The value amount change since the previous day | [optional] 
**cost_basis** | **float** | The total cost of acquiring the security | [optional] 
**hold_type** | **str** | The type of the holding | [optional] 
**inv_security_type** | **str** | The security type for the investment holding | [optional] 
**status** | **str** | The status of the holding | [optional] 
**current_price_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**security_type** | **str** | Type of security for the investment position | [optional] 
**mf_type** | **str** | Type of mutual fund, such as open ended | [optional] 
**pos_type** | **str** | Fund type assigned by the FI (long or short) | [optional] 
**total_gl_dollar** | **float** | Total gain and loss of the position at the time of aggregation in dollars | [optional] 
**total_gl_percent** | **float** | Total gain and loss of the position at the time of aggregation in percentage | [optional] 
**option_strike_price** | **float** | The strike price of the option contract | [optional] 
**option_type** | **str** | The type of option contract (PUT or CALL) | [optional] 
**option_shares_per_contract** | **float** | The number of shares per option contract | [optional] 
**option_expire_date** | **date** | Expiration date of option | [optional] 
**fi_asset_class** | **str** | Financial Institution (FI) defined asset class (COMMON STOCK, COMNEQTY, EQUITY/STOCK, CMA-ISA, CONVERTIBLE PREFERREDS, CORPORATE BONDS, OTHER MONEY FUNDS, ALLOCATION FUNDS, CMA-TAXABLE, FOREIGNEQUITYADRS, COMMONSTOCK, PREFERRED STOCKS, STABLE VALUE, FOREIGN EQUITY ADRS) | [optional] 
**asset_class** | **str** | An asset class is a grouping of comparable financial securities. These include equities (stocks), fixed income (bonds), and cash equivalent or money market instruments. (DOMESTICBOND, LARGESTOCK, INTLSTOCK, MONEYMRKT, OTHER) | [optional] 
**currency_rate** | **float** | Currency rate, ratio of currency to original currency | [optional] 
**security_id** | **str** | The security ID of the transaction | [optional] 
**security_id_type** | **str** | The security type. This field is related to the &#x60;securityId&#x60; field. Possible values: * \&quot;CUSIP\&quot;  * \&quot;ISIN\&quot;  * \&quot;SEDOL\&quot;  * \&quot;SICC\&quot;  * \&quot;VALOR\&quot;  * \&quot;WKN\&quot; | [optional] 
**cost_basis_per_share** | **float** | The per share cost of acquiring the security | [optional] 
**sub_account_type** | **str** | The subaccount&#39;s type, such as cash | [optional] 
**security_currency** | **str** | Symbol for the currency that the account is being converted into | [optional] 
**today_gl_dollar** | **float** | The current day&#39;s gain and loss of the position at the time of aggregation in dollars | [optional] 
**today_gl_percent** | **float** | The current day&#39;s gain and loss of the position at the time of aggregation in percentage | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


