# AccountOwnerDetails

Owner of a customer account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_name** | **str** | The full name of the account owner. Multiple account owners are returned in one string per the source data from the institution. | 
**addresses** | [**AccountOwnerAddresses**](AccountOwnerAddresses.md) |  | 
**relationship** | **str** | The type of relationship to the account:   * \&quot;AUTHORIZED_USER\&quot;    * \&quot;BUSINESS\&quot;     * \&quot;FOR_BENEFIT_OF_PRIMARY\&quot;    * \&quot;FOR_BENEFIT_OF_PRIMARY_JOINT_RESTRICTED\&quot;    * \&quot;FOR_BENEFIT_OF_SECONDARY\&quot;  * \&quot;FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED\&quot;  * \&quot;FOR_BENEFIT_OF_SOLE_OWNER_RESTRICTED\&quot;  * \&quot;POWER_OF_ATTORNEY\&quot;  * \&quot;PRIMARY_JOINT_TENANTS\&quot;  * \&quot;PRIMARY\&quot;  * \&quot;PRIMARY_BORROWER\&quot;  * \&quot;PRIMARY_JOINT\&quot;  * \&quot;SECONDARY\&quot;  * \&quot;SECONDARY_JOINT_TENANTS\&quot;  * \&quot;SECONDARY_BORROWER\&quot;  * \&quot;SECONDARY_JOINT\&quot;  * \&quot;SOLE_OWNER\&quot;  * \&quot;TRUSTEE\&quot;  * \&quot;UNIFORM_TRANSFER_TO_MINOR\&quot; | [optional] 
**first_name** | **str** | The first name of the account holder | [optional] 
**middle_name** | **str** | The middle name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | [optional] 
**suffix** | **str** | A generational or academic suffix | [optional] 
**name_classification** | **str** | The classification of the account holder: * \&quot;person / personal / home\&quot; * \&quot;business\&quot; * \&quot;other\&quot; | [optional] 
**name_classificationconfidencescore** | **float** | The confidence score 0-100 of the name classification. | [optional] 
**emails** | [**AccountOwnerEmails**](AccountOwnerEmails.md) |  | [optional] 
**phones** | [**AccountOwnerPhones**](AccountOwnerPhones.md) |  | [optional] 
**documentations** | [**AccountOwnerDocumentations**](AccountOwnerDocumentations.md) |  | [optional] 
**identity_insights** | [**AccountOwnerIdentityInsights**](AccountOwnerIdentityInsights.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


