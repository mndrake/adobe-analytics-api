# AnalyticsCalculatedMetric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System generated id | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rsid** | **str** | The report suite id for which the component was created/updated | [optional] 
**report_suite_name** | **str** | The report suite name for which the component was created/updated | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**polarity** | **str** | Set metric polarity, which indicates whether it&#x27;s good or bad if a given metric goes up. Default&#x3D;positive | [optional] 
**precision** | **int** | Number of decimal places to include in calculated metric result | [optional] 
**type** | **str** |  | [optional] 
**definition** | [**CalculatedMetricDef**](CalculatedMetricDef.md) |  | 
**categories** | **list[str]** |  | [optional] 
**tags** | [**list[Tag]**](Tag.md) |  | [optional] 
**site_title** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**created** | **datetime** | Calculated metric creation date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

