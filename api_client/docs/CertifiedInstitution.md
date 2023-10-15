# CertifiedInstitution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of a financial institution, represented as a number | 
**name** | **str** | The name of the institution | 
**trans_agg** | **bool** | \&quot;true\&quot;: The institution is certified for the Transaction Aggregation product \&quot;false\&quot;: The institution is decertified for the Transaction Aggregation product | 
**ach** | **bool** | \&quot;true\&quot;: The institution is certified for the ACH product \&quot;false\&quot;: The institution is decertified for the ACH product | 
**state_agg** | **bool** | \&quot;true\&quot;: The institution is certified for the Statement Aggregation product \&quot;false\&quot;: The institution is decertified for the Statement Aggregation product | 
**voi** | **bool** | \&quot;true\&quot;: The institution is certified for the VOI product \&quot;false\&quot;: The institution is decertified for the VOI product | 
**voa** | **bool** | \&quot;true\&quot;: The institution is certified for the VOA product \&quot;false\&quot;: The institution is decertified for the VOA product | 
**aha** | **bool** | \&quot;true\&quot;: The institution is certified for the Account History Aggregation product \&quot;false\&quot;: The institution is decertified for the Account History Aggregation product | 
**avail_balance** | **bool** | \&quot;true\&quot;: The institution is certified for the Account Balance Check (ABC) product \&quot;false\&quot;: The institution is decertified for the Account Balance Check (ABC) product | 
**account_owner** | **bool** | \&quot;true\&quot;: The institution is certified for the Account Owner product \&quot;false\&quot;: The institution is decertified for the Account Owner product | 
**student_loan_data** | **bool** | \&quot;true\&quot;: The institution is certified for the Student Loan Data product  \&quot;false\&quot;: The institution is decertified for the Student Loan Data product | 
**loan_payment_details** | **bool** | \&quot;true\&quot;: The institution is certified for the Loan Payment Detail product  \&quot;false\&quot;: The institution is decertified for the Loan Payment Detail product | 
**rssd** | **int** | The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits. | [optional] 
**child_institutions** | [**[ChildInstitution]**](ChildInstitution.md) | An array of child financial institutions | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


