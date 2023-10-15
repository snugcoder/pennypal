# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A transaction ID | 
**amount** | **float** | The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values. | 
**account_id** | **int** | An account ID represented as a number | 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**status** | **str** | One of \&quot;active\&quot;, \&quot;pending\&quot;, or \&quot;shadow\&quot; (see [Transaction Status](https://developer.mastercard.com/open-banking-us/documentation/products/manage/transaction-data/#transaction-status)) | 
**description** | **str** | The description value is from the financial institution (FI), often known as the payee. The value \&quot;No description provided by institution\&quot; is returned when the FI doesn&#39;t provide one | 
**created_date** | **int** | A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it was added to our platform. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**memo** | **str** | The institution must provide either a description, a memo, or both. We recommended concatenating the two fields into a single value. | [optional] 
**type** | **str** | If provided by the institution, the following values may be returned in the field of a record: * \&quot;atm\&quot;  * \&quot;cash\&quot;  * \&quot;check\&quot;  * \&quot;credit\&quot;  * \&quot;debit\&quot;  * \&quot;deposit\&quot;  * \&quot;directDebit\&quot;  * \&quot;directDeposit\&quot;  * \&quot;dividend\&quot;  * \&quot;fee\&quot;  * \&quot;interest\&quot;  * \&quot;other\&quot;  * \&quot;payment\&quot;  * \&quot;pointOfSale\&quot;  * \&quot;repeatPayment\&quot;  * \&quot;serviceCharge\&quot;  * \&quot;transfer\&quot; | [optional] 
**transaction_date** | **int** | A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it occurred. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**posted_date** | **int** | A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it was posted or cleared by the institution. This value isn&#39;t required for student loan transaction data. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**first_effective_date** | **int** | A date in Unix epoch time (in seconds). Represents the first timestamp of the transaction recorded in the &#x60;effectiveDate&#x60; field. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**effective_date** | **int** | A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it became effective on an account by an institution. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**option_expire_date** | **int** | A date in Unix epoch time (in seconds). Represents the timestamp of the transaction expiration date when it became expires on an account by an institution. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**check_num** | **int** | The check number of the transaction | [optional] 
**escrow_amount** | **float** | The portion of the transaction allocated to escrow | [optional] 
**fee_amount** | **float** | The portion of the overall transaction amount applied to fees | [optional] 
**suspense_amount** | **float** | Temporarily hold funds if you overpay or underpay your monthly payment | [optional] 
**interest_amount** | **float** | The portion of the transaction allocated to interest | [optional] 
**principal_amount** | **float** | The portion of the transaction allocated to principal | [optional] 
**option_strike_price** | **float** | The strike price of the option contract | [optional] 
**unit_quantity** | **int** | The number of units (individual shares) in the transaction | [optional] 
**unit_price** | **float** | Share price for the investment unit: stocks, mutual funds, ETFs | [optional] 
**categorization** | [**Categorization**](Categorization.md) |  | [optional] 
**running_balance_amount** | **float** | The ending balance after the transaction was posted | [optional] 
**subaccount_security_type** | **str** | The type of sub account the funds came from | [optional] 
**commission_amount** | **int** | Transaction commission | [optional] 
**ticker** | **str** | Ticker symbol for the investment related to the transaction | [optional] 
**investment_transaction_type** | **str** | Keywords in the &#x60;description&#x60; and &#x60;memo&#x60; fields were used to translate investment transactions into these types.  Possible values:  * \&quot;cancel\&quot;  * \&quot;purchaseToClose\&quot;  * \&quot;purchaseToCover\&quot;  * \&quot;contribution\&quot;  * \&quot;optionExercise\&quot;  * \&quot;optionExpiration\&quot;  * \&quot;fee\&quot;  * \&quot;soldToClose\&quot;  * \&quot;soldToOpen\&quot;  * \&quot;split\&quot;  * \&quot;transfer\&quot;  * \&quot;returnOfCapital\&quot;  * \&quot;income\&quot;  * \&quot;purchased\&quot;  * \&quot;sold\&quot;  * \&quot;dividendreInvest\&quot;  * \&quot;tax\&quot;  * \&quot;dividend\&quot;  * \&quot;reinvestOfIncome\&quot;  * \&quot;interest\&quot;  * \&quot;deposit\&quot;  * \&quot;otherInfo\&quot; | [optional] 
**taxes_amount** | **int** | Taxes applicable to the investment trade | [optional] 
**currency_symbol** | **str** | If the foreign amount value is present then this is the currency code of that foreign amount | [optional] 
**income_type** | **str** | Capital gains applied in short, long, or miscellaneous terms for tax purposes | [optional] 
**split_denominator** | **float** | Denominator of the stock split for the transaction | [optional] 
**split_numerator** | **float** | Numerator of the stock split for the transaction | [optional] 
**shares_per_contract** | **float** | Shares per contract of the underlying stock option | [optional] 
**sub_account_fund** | **str** | The sub account where the funds came from | [optional] 
**security_id** | **str** | The security ID of the transaction | [optional] 
**security_id_type** | **str** | The security type. This field is related to the &#x60;securityId&#x60; field. Possible values: * \&quot;CUSIP\&quot;  * \&quot;ISIN\&quot;  * \&quot;SEDOL\&quot;  * \&quot;SICC\&quot;  * \&quot;VALOR\&quot;  * \&quot;WKN\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


