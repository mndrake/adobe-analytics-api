# swagger_client.DaterangesApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_date_range**](DaterangesApi.md#create_date_range) | **POST** /dateranges | Creates configuration for a DateRange.
[**delete_date_range**](DaterangesApi.md#delete_date_range) | **DELETE** /dateranges/{dateRangeId} | Deletes a DateRange.
[**get_date_range**](DaterangesApi.md#get_date_range) | **GET** /dateranges/{dateRangeId} | Retrieves configuration for a DateRange.
[**get_date_ranges**](DaterangesApi.md#get_date_ranges) | **GET** /dateranges | Returns a list of dateranges for the user
[**update_date_range**](DaterangesApi.md#update_date_range) | **PUT** /dateranges/{dateRangeId} | Updates configuration for a DateRange.

# **create_date_range**
> AnalyticsDateRange create_date_range(body=body, locale=locale, expansion=expansion)

Creates configuration for a DateRange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DaterangesApi()
body = swagger_client.AnalyticsDateRange() # AnalyticsDateRange | JSON-formatted array of Date Range objects containing key-value pairs (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional date range metadata fields to include on response. (optional)

try:
    # Creates configuration for a DateRange.
    api_response = api_instance.create_date_range(body=body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaterangesApi->create_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsDateRange**](AnalyticsDateRange.md)| JSON-formatted array of Date Range objects containing key-value pairs | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional date range metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsDateRange**](AnalyticsDateRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_date_range**
> InlineResponse2001 delete_date_range(date_range_id)

Deletes a DateRange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DaterangesApi()
date_range_id = 'date_range_id_example' # str | The id of the date range to delete

try:
    # Deletes a DateRange.
    api_response = api_instance.delete_date_range(date_range_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaterangesApi->delete_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_range_id** | **str**| The id of the date range to delete | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_date_range**
> AnalyticsDateRange get_date_range(date_range_id, locale=locale, expansion=expansion)

Retrieves configuration for a DateRange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DaterangesApi()
date_range_id = 'date_range_id_example' # str | The DateRange id for which to retrieve information
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional date range metadata fields to include on response. (optional)

try:
    # Retrieves configuration for a DateRange.
    api_response = api_instance.get_date_range(date_range_id, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaterangesApi->get_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_range_id** | **str**| The DateRange id for which to retrieve information | 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional date range metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsDateRange**](AnalyticsDateRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_date_ranges**
> AnalyticsDateRange get_date_ranges(locale=locale, filter_by_ids=filter_by_ids, limit=limit, page=page, expansion=expansion, include_type=include_type)

Returns a list of dateranges for the user

This API allows users to store commonly used date ranges so that they can be reused throughout the product.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DaterangesApi()
locale = 'en_US' # str | Locale (optional) (default to en_US)
filter_by_ids = 'filter_by_ids_example' # str | Filter list to only include date ranges in the specified list (comma-delimited list of IDs) (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional date range metadata fields to include on response. (optional)
include_type = ['include_type_example'] # list[str] | Include additional date ranges not owned by user. The \"all\" option takes precedence over \"shared\" (optional)

try:
    # Returns a list of dateranges for the user
    api_response = api_instance.get_date_ranges(locale=locale, filter_by_ids=filter_by_ids, limit=limit, page=page, expansion=expansion, include_type=include_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaterangesApi->get_date_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| Locale | [optional] [default to en_US]
 **filter_by_ids** | **str**| Filter list to only include date ranges in the specified list (comma-delimited list of IDs) | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional date range metadata fields to include on response. | [optional] 
 **include_type** | [**list[str]**](str.md)| Include additional date ranges not owned by user. The \&quot;all\&quot; option takes precedence over \&quot;shared\&quot; | [optional] 

### Return type

[**AnalyticsDateRange**](AnalyticsDateRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_date_range**
> AnalyticsDateRange update_date_range(date_range_id, body=body, locale=locale, expansion=expansion)

Updates configuration for a DateRange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DaterangesApi()
date_range_id = 'date_range_id_example' # str | The DateRange id for which to retrieve information
body = swagger_client.AnalyticsDateRange() # AnalyticsDateRange | JSON-formatted array of Date Range objects containing key-value pairs (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional date range metadata fields to include on response. (optional)

try:
    # Updates configuration for a DateRange.
    api_response = api_instance.update_date_range(date_range_id, body=body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaterangesApi->update_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_range_id** | **str**| The DateRange id for which to retrieve information | 
 **body** | [**AnalyticsDateRange**](AnalyticsDateRange.md)| JSON-formatted array of Date Range objects containing key-value pairs | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional date range metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsDateRange**](AnalyticsDateRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

