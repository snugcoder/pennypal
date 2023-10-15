# LoanPaymentDetailsAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID | 
**account_number** | **str** | Institution&#39;s ID of the Student Loan Account | 
**account_payment_number** | **str** | The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number. | 
**account_payment_address** | **str** | The payment address to which send manual payments should be sent | 
**account_future_payoff_amount** | **float** | The payoff amount for the account | [optional] 
**account_future_payoff_date** | **datetime** | The date to which the \&quot;Future Payoff Amount\&quot; applies | [optional] 
**group_detail** | [**[LoanPaymentDetailsGroup]**](LoanPaymentDetailsGroup.md) | Group details | [optional] 
**loan_detail** | [**[LoanPaymentDetailsLoan]**](LoanPaymentDetailsLoan.md) | Loan details | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


