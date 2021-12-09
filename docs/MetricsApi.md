# swagger_client.MetricsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric**](MetricsApi.md#get_metric) | **GET** /metrics/{id} | Returns a metric for the given report suite
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /metrics | Returns a list of metrics for the given report suite

# **get_metric**
> AnalyticsMetric get_metric(id, rsid, locale=locale, expansion=expansion)

Returns a metric for the given report suite

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetricsApi()
id = 'id_example' # str | The id of the metric for which to retrieve info. Note ids are values like pageviews, not metrics/pageviews
rsid = 'rsid_example' # str | ID of desired report suite ie. myrsid
locale = 'en_US' # str | Locale that system named metrics should be returned in (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Add extra metadata to items (comma-delimited list) (optional)

try:
    # Returns a metric for the given report suite
    api_response = api_instance.get_metric(id, rsid, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the metric for which to retrieve info. Note ids are values like pageviews, not metrics/pageviews | 
 **rsid** | **str**| ID of desired report suite ie. myrsid | 
 **locale** | **str**| Locale that system named metrics should be returned in | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Add extra metadata to items (comma-delimited list) | [optional] 

### Return type

[**AnalyticsMetric**](AnalyticsMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**
> AnalyticsMetric get_metrics(rsid, locale=locale, segmentable=segmentable, expansion=expansion)

Returns a list of metrics for the given report suite

This returns the metrics list primarily for the Analytics product. The platform identity API Returns a list of all possible metrics for the supported systems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetricsApi()
rsid = 'rsid_example' # str | ID of desired report suite ie. myrsid
locale = 'en_US' # str | Locale that system named metrics should be returned in (optional) (default to en_US)
segmentable = false # bool | Filter the metrics by if they are valid in a segment. (optional) (default to false)
expansion = ['expansion_example'] # list[str] | Add extra metadata to items (comma-delimited list) (optional)

try:
    # Returns a list of metrics for the given report suite
    api_response = api_instance.get_metrics(rsid, locale=locale, segmentable=segmentable, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsid** | **str**| ID of desired report suite ie. myrsid | 
 **locale** | **str**| Locale that system named metrics should be returned in | [optional] [default to en_US]
 **segmentable** | **bool**| Filter the metrics by if they are valid in a segment. | [optional] [default to false]
 **expansion** | [**list[str]**](str.md)| Add extra metadata to items (comma-delimited list) | [optional] 

### Return type

[**AnalyticsMetric**](AnalyticsMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

