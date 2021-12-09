# swagger_client.DimensionsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dimensions_get_dimension**](DimensionsApi.md#dimensions_get_dimension) | **GET** /dimensions/{dimensionId} | Returns a dimension for the given report suite
[**dimensions_get_dimensions**](DimensionsApi.md#dimensions_get_dimensions) | **GET** /dimensions | Returns a list of dimensions for a given report suite.

# **dimensions_get_dimension**
> AnalyticsDimension dimensions_get_dimension(dimension_id, rsid, locale=locale, expansion=expansion)

Returns a dimension for the given report suite

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DimensionsApi()
dimension_id = 'dimension_id_example' # str | The dimension ID. For example a valid id is a value like 'evar1'
rsid = 'rsid_example' # str | The report suite ID.
locale = 'en_US' # str | The locale to use for returning system named dimensions. (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Add extra metadata to items (comma-delimited list) (optional)

try:
    # Returns a dimension for the given report suite
    api_response = api_instance.dimensions_get_dimension(dimension_id, rsid, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DimensionsApi->dimensions_get_dimension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dimension_id** | **str**| The dimension ID. For example a valid id is a value like &#x27;evar1&#x27; | 
 **rsid** | **str**| The report suite ID. | 
 **locale** | **str**| The locale to use for returning system named dimensions. | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Add extra metadata to items (comma-delimited list) | [optional] 

### Return type

[**AnalyticsDimension**](AnalyticsDimension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dimensions_get_dimensions**
> list[AnalyticsDimension] dimensions_get_dimensions(rsid, locale=locale, segmentable=segmentable, reportable=reportable, classifiable=classifiable, expansion=expansion)

Returns a list of dimensions for a given report suite.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DimensionsApi()
rsid = 'rsid_example' # str | A Report Suite ID
locale = 'en_US' # str | Locale (optional) (default to en_US)
segmentable = true # bool | Only include dimensions that are valid within a segment. (optional)
reportable = true # bool | Only include dimensions that are valid within a report. (optional)
classifiable = false # bool | Only include classifiable dimensions. (optional) (default to false)
expansion = ['expansion_example'] # list[str] | Add extra metadata to items (comma-delimited list) (optional)

try:
    # Returns a list of dimensions for a given report suite.
    api_response = api_instance.dimensions_get_dimensions(rsid, locale=locale, segmentable=segmentable, reportable=reportable, classifiable=classifiable, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DimensionsApi->dimensions_get_dimensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsid** | **str**| A Report Suite ID | 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **segmentable** | **bool**| Only include dimensions that are valid within a segment. | [optional] 
 **reportable** | **bool**| Only include dimensions that are valid within a report. | [optional] 
 **classifiable** | **bool**| Only include classifiable dimensions. | [optional] [default to false]
 **expansion** | [**list[str]**](str.md)| Add extra metadata to items (comma-delimited list) | [optional] 

### Return type

[**list[AnalyticsDimension]**](AnalyticsDimension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

