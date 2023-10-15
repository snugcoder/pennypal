# ThirdPartyAccessProduct

Product for which access token to be generated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Third party access token can be generated for the following product types:   * \&quot;moneyTransferDetails\&quot;: Retrieve account details for money transfer  * \&quot;availableBalance\&quot;: Retrieves the latest cached available and cleared     account balances for an account.  * \&quot;availableBalanceLive\&quot;: Retrieves the available and cleared account balances live from the financial institution  * \&quot;accountOwner\&quot;: Retrieves names and addresses of the account owner from a financial institution.  * \&quot;paymentIndicator\&quot;: Get the Payment Success Indicator response, scoring the likelihood of payment settlement  * \&quot;paymentFeedback\&quot;: Create feedback loop for Payment Success Indicator (PSI) and/or Payment Routing Optimizer (PRO)  * \&quot;paymentRouting\&quot;: Product recommends the best rail to use as well as the best time to initiate the payment | 
**account_id** | **str** | An account ID | 
**access_period** | [**ThirdPartyAccessPeriod**](ThirdPartyAccessPeriod.md) |  | 
**payor_id** | **str** | The Finicity Partner ID who should be billed when the Requester requests data from Finicity. If no value specified, then the Recipient will be billed. | [optional] 
**max_calls** | **int** | Max number of calls to the consented product (consented api) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


