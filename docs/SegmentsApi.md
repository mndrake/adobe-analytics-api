# swagger_client.SegmentsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segments_create_segment**](SegmentsApi.md#segments_create_segment) | **POST** /segments | Creates Segment
[**segments_delete_segment**](SegmentsApi.md#segments_delete_segment) | **DELETE** /segments/{id} | Delete Segment
[**segments_get_segment**](SegmentsApi.md#segments_get_segment) | **GET** /segments/{id} | Get a Single Segment
[**segments_get_segments**](SegmentsApi.md#segments_get_segments) | **GET** /segments | Retrieve All Segments
[**segments_update_segment**](SegmentsApi.md#segments_update_segment) | **PUT** /segments/{id} | Update a Segment
[**segments_validate_segment**](SegmentsApi.md#segments_validate_segment) | **POST** /segments/validate | Validate a Segment

# **segments_create_segment**
> AnalyticsSegmentResponseItem segments_create_segment(body, locale=locale, expansion=expansion)

Creates Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
body = swagger_client.AnalyticsSegment() # AnalyticsSegment | JSON-formatted Object containing key/value pairs for segment creation.
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional segment metadata fields to include on response. (optional)

try:
    # Creates Segment
    api_response = api_instance.segments_create_segment(body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsSegment**](AnalyticsSegment.md)| JSON-formatted Object containing key/value pairs for segment creation. | 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional segment metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsSegmentResponseItem**](AnalyticsSegmentResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segments_delete_segment**
> str segments_delete_segment(id, locale=locale)

Delete Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
id = 'id_example' # str | The segment ID to be deleted
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Delete Segment
    api_response = api_instance.segments_delete_segment(id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_delete_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The segment ID to be deleted | 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segments_get_segment**
> AnalyticsSegmentResponseItem segments_get_segment(id, locale=locale, expansion=expansion)

Get a Single Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
id = 'id_example' # str | The segment ID to retrieve
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional segment metadata fields to include on response. (optional)

try:
    # Get a Single Segment
    api_response = api_instance.segments_get_segment(id, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_get_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The segment ID to retrieve | 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional segment metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsSegmentResponseItem**](AnalyticsSegmentResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segments_get_segments**
> AnalyticsSegmentResponseItem segments_get_segments(rsids=rsids, segment_filter=segment_filter, locale=locale, name=name, tag_names=tag_names, filter_by_published_segments=filter_by_published_segments, limit=limit, page=page, sort_direction=sort_direction, sort_property=sort_property, expansion=expansion, include_type=include_type)

Retrieve All Segments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
rsids = 'rsids_example' # str | Filter list to only include segments tied to specified RSID list (comma-delimited) (optional)
segment_filter = 'segment_filter_example' # str | Filter list to only include segments in the specified list (comma-delimited list of IDs) (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
name = 'name_example' # str | Filter list to only include segments that contains the Name (optional)
tag_names = 'tag_names_example' # str | Filter list to only include segments that contains one of the tags (optional)
filter_by_published_segments = 'all' # str | Filter list to only include segments where the published field is set to one of the allowable values (all, true, false). (optional) (default to all)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)
sort_direction = 'ASC' # str | Sort direction (ASC or DESC (optional) (default to ASC)
sort_property = 'id' # str | Property to sort by (name, modified_date, id is currently allowed) (optional) (default to id)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional segment metadata fields to include on response. (optional)
include_type = ['include_type_example'] # list[str] | Include additional segments not owned by user. The \"all\" option takes precedence over \"shared\" (optional)

try:
    # Retrieve All Segments
    api_response = api_instance.segments_get_segments(rsids=rsids, segment_filter=segment_filter, locale=locale, name=name, tag_names=tag_names, filter_by_published_segments=filter_by_published_segments, limit=limit, page=page, sort_direction=sort_direction, sort_property=sort_property, expansion=expansion, include_type=include_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_get_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsids** | **str**| Filter list to only include segments tied to specified RSID list (comma-delimited) | [optional] 
 **segment_filter** | **str**| Filter list to only include segments in the specified list (comma-delimited list of IDs) | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **name** | **str**| Filter list to only include segments that contains the Name | [optional] 
 **tag_names** | **str**| Filter list to only include segments that contains one of the tags | [optional] 
 **filter_by_published_segments** | **str**| Filter list to only include segments where the published field is set to one of the allowable values (all, true, false). | [optional] [default to all]
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]
 **sort_direction** | **str**| Sort direction (ASC or DESC | [optional] [default to ASC]
 **sort_property** | **str**| Property to sort by (name, modified_date, id is currently allowed) | [optional] [default to id]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional segment metadata fields to include on response. | [optional] 
 **include_type** | [**list[str]**](str.md)| Include additional segments not owned by user. The \&quot;all\&quot; option takes precedence over \&quot;shared\&quot; | [optional] 

### Return type

[**AnalyticsSegmentResponseItem**](AnalyticsSegmentResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segments_update_segment**
> AnalyticsSegmentResponseItem segments_update_segment(id, body=body, locale=locale, expansion=expansion)

Update a Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
id = 'id_example' # str | Segment ID to be updated
body = NULL # dict(str, object) | JSON-formatted Object containing key/value pairs to be updated. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional segment metadata fields to include on response. (optional)

try:
    # Update a Segment
    api_response = api_instance.segments_update_segment(id, body=body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_update_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Segment ID to be updated | 
 **body** | [**dict(str, object)**](dict.md)| JSON-formatted Object containing key/value pairs to be updated. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional segment metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsSegmentResponseItem**](AnalyticsSegmentResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segments_validate_segment**
> SegmentCompatibility segments_validate_segment(body, rsid)

Validate a Segment

Returns a segment validation for the segment contained in the post body of the report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
body = 'body_example' # str | Segment definition
rsid = 'rsid_example' # str | RSID to run the report against

try:
    # Validate a Segment
    api_response = api_instance.segments_validate_segment(body, rsid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_validate_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Segment definition | 
 **rsid** | **str**| RSID to run the report against | 

### Return type

[**SegmentCompatibility**](SegmentCompatibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

