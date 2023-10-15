# LoanPaymentDetailsGroup

Group details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID | 
**group_number** | **str** | Institution&#39;s ID of the Student Loan Group | 
**group_payment_number** | **str** | The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number. | 
**group_payment_address** | **str** | The payment address to which send manual payments should be sent | 
**group_loan_detail** | [**[LoanPaymentDetailsLoan]**](LoanPaymentDetailsLoan.md) |  | 
**group_future_payoff_amount** | **float** | The payoff amount for the group | [optional] 
**group_future_payoff_date** | **datetime** | The date to which the \&quot;Future Payoff Amount\&quot; applies | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


