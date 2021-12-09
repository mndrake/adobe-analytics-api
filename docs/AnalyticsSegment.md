# AnalyticsSegment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the segment. | [optional] 
**description** | **str** | A description of the segment. | [optional] 
**rsid** | **str** | The report suite id. | [optional] 
**report_suite_name** | **str** | The friendly name for the report suite id. | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**definition** | [**AnalyticsSegmentDefinition**](AnalyticsSegmentDefinition.md) |  | [optional] 
**compatibility** | [**SegmentCompatibility**](SegmentCompatibility.md) |  | [optional] 
**definition_last_modified** | **datetime** |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**site_title** | **str** | A name for the report suite.  This is deprecated and should use the report suite name instead. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | All existing tags associated with the segment. | [optional] 
**modified** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

