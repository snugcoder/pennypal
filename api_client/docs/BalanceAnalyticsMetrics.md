# BalanceAnalyticsMetrics

Balance analytics metrics and calculations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | **float** | Available Balance | [optional] 
**available_balance_date** | **str** | Available Balance date | [optional] 
**average_daily_balance_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average daily ending balance each month over the report time period | [optional] 
**average_daily_balance_for_the_report_time_period** | **float** | Average Daily Balance | [optional] 
**average_weekday_balance_for_the_report_time_period** | **float** | Average Weekday Balance | [optional] 
**count_daily_negative_balances_by_month_for_the_report_time_period** | [**[ObbDateRangeAndCount]**](ObbDateRangeAndCount.md) | Number of negative daily ending balances each month over the report time period | [optional] 
**current_running_balance** | **float** | Current Running Balance Date | [optional] 
**current_running_balance_date** | **str** | Current Running Balance date | [optional] 
**daily_balances_by_weekday_for_the_report_time_period** | [**[ObbDailyBalance]**](ObbDailyBalance.md) | Daily balance of the account during weekdays over the length of the report | [optional]  if omitted the server will use the default value of []
**daily_balances_for_the_report_time_period** | [**[ObbDailyBalance]**](ObbDailyBalance.md) | Daily balance of the account over the length of the report | [optional]  if omitted the server will use the default value of []
**historic_number_of_weeks_average_balance_increasing** | [**ObbNumWeeksAverageBalanceIncreasing**](ObbNumWeeksAverageBalanceIncreasing.md) |  | [optional] 
**maximum_daily_balance_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Maximum daily ending balance each month over the report time period | [optional] 
**maximum_running_balance_for_the_report_time_period** | **float** | Maximum Running Balance | [optional] 
**minimum_daily_balance_by_month_for_the_report_time_period** | [**[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Minimum daily ending balance each month over the report time period | [optional] 
**minimum_running_balance_for_the_report_time_period** | **float** | Minimum Running Balance | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


