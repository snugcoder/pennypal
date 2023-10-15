# AccountOwnerIdentityInsights

List of account owner Identity Insights

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_email_valid** | **bool** | True if the email address is valid. | [optional] 
**email_first_seen_days** | **float** | Count of days since the email was first observed in Ekata&#39;s Identity Network. If the email has not been observed before, first_seen_days will be 0. | [optional] 
**email_domain_creation_date** | **str** | Returns a date that the email domain was created. | [optional] 
**email_to_name** | **str** | The match status between the input name and the queried entity. * not found * match * no-match | [optional] 
**ip_risk** | **float** | True if the IP address is considered risky, based on multiple IP data points and velocity calculations. | [optional] 
**ip_risk_score** | **float** | Comprehensive risk score associated with an IP address, with a higher score indicating a riskier IP address. A number between 0 and 1 rounded to three decimal places. | [optional] 
**ip_last_seen_days** | **float** | Count of days since the IP address was last observed in Ekata&#39;s Identity Network. If the IP address has not been observed before, IpLastSeenDays will be 0. | [optional] 
**ip_geolocation_country_code** | **str** | The ISO-3166 alpha-2 country code associated with the geolocation of the IP address. | [optional] 
**ip_geolocation_subdivision** | **str** | More granular detail about the IP address location. | [optional] 
**ip_phone_distance** | **float** | The distance (in miles) between the IP address and the closest physical address associated with the phone number. | [optional] 
**ip_address_distance** | **float** | The distance (in miles) between the IP address and the physical address. | [optional] 
**is_phone_valid** | **bool** | True if the phone number is valid. | [optional] 
**phone_line_type** | **str** | The line type of the phone number. * landline - traditional wired phone line. * fixed-voip - VoIP-based fixed line phones. * mobile - wireless phone line. * voicemail - voicemail-only service. * toll-free - callee pays for call. * premium - caller pays a premium for the call-e.g., 976 area code. * non-fixed-voip - Skype, for example * other - anything that does not match the previous categories. | [optional] 
**phone_carrier** | **str** | The company that provides voice and/or data services for the phone number. Carriers are returned at the MVNO level. | [optional] 
**phone_country_code** | **str** | The ISO-3166 alpha-2 country code associated with the phone number. | [optional] 
**phone_last_seen_days** | **float** | Count of days since the phone was last observed in Ekata&#39;s Identity Network. If the phone has not been observed before, &#x60;phoneLastSeenDays&#x60; will be 0. | [optional] 
**phone_email_first_seen_days** | **float** | Count of days since the combination of phone and email was first observed in Ekata&#39;s Identity Network. If that combination has not been observed before, &#x60;phoneEmailFirstSeenDays&#x60; will be 0. | [optional] 
**phone_to_name** | **str** | The match status between the input name and the queried entity.  * not-found  * match  * no-match | [optional] 
**phone_to_address** | **str** | The match status between the input phone and the queried entity. * match - Phone location matches input address line 1, address line 2, city, state, and postal code.   * postal-match - Phone location postal code matches input address postal code.   * zip4-match - Phone location postal code zip+4 matches input address postal code zip+4.   * city-state-match - Phone location city and state matches input address city and state.  * metro-match - Phone location is in the same metro area as input address.   * country-match - Phone location country matches input address country.   * no-match - Phone location does not match input address. | [optional] 
**address_validity_level** | **float** | The most granular level to which the address could be validated. Ex. If the address was only valid to the city level (but not to the house level), it would return “valid_to_city”.   * missing_address - An input address was not provided.    * invalid - The input address is not valid.    * valid - The input address is valid.    * valid_to_country - The input address could only be validated to the country level. This means the country of the input address is valid, but the other elements of the input address were unable to be confirmed as valid or invalid.    * valid_to_city - The input address was validated to the city level. This means the country, state, city, and postal code of the input address are valid, but the street, house number, and subpremise of the input address were unable to be confirmed as valid or invalid.    * valid_to_street - The input address was validated to the street level. This means the country, state, city, postal code, and street of the input address are valid, but the house number and subpremise of the input address were unable to be confirmed as valid or invalid.      * valid_to_house_number - The input address was validated to the street and house number level. This means the country, state, city,postal code, street, and house number of the input address are valid, but the subpremise of the input address was unable to be confirmed as valid or invalid.       * valid_to_house_number_missing_apt - The input address was validated to the street and house number level. This means the country, state, city, postal code, street, and house number of the input address are valid, but the subpremise of the input address was missing and thus unable to be confirmed as valid or invalid. | [optional] 
**address_to_name** | **str** | The match status between the input name and the queried entity. * not-found * match * no-match | [optional] 
**identity_network_score** | **float** | Comprehensive network score built on behavioral insights such as velocity, popularity, volatility, and age of an attribute, with a higher score indicating a riskier account sign-up. A number between 0 and 1 rounded to three decimal places. | [optional] 
**identity_risk_score** | **float** | Comprehensive identity risk score with a higher score indicating a riskier account sign-up. | [optional] 
**warnings** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


