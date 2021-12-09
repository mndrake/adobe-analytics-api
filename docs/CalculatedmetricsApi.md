# swagger_client.CalculatedmetricsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculatedmetrics_create_calculated_metric**](CalculatedmetricsApi.md#calculatedmetrics_create_calculated_metric) | **POST** /calculatedmetrics | Create a new Calculated Metric
[**calculatedmetrics_delete_calculated_metric**](CalculatedmetricsApi.md#calculatedmetrics_delete_calculated_metric) | **DELETE** /calculatedmetrics/{id} | Deletion of Calculated Metrics by Id
[**calculatedmetrics_get_calculated_metric_function**](CalculatedmetricsApi.md#calculatedmetrics_get_calculated_metric_function) | **GET** /calculatedmetrics/functions/{id} | Retrieve a calculated metric function by id
[**calculatedmetrics_get_calculated_metric_functions**](CalculatedmetricsApi.md#calculatedmetrics_get_calculated_metric_functions) | **GET** /calculatedmetrics/functions | Retrieve calculated metric functions
[**calculatedmetrics_update_calculated_metric**](CalculatedmetricsApi.md#calculatedmetrics_update_calculated_metric) | **PUT** /calculatedmetrics/{id} | Update an existing calculated metric
[**calculatedmetrics_validate_calculated_metric**](CalculatedmetricsApi.md#calculatedmetrics_validate_calculated_metric) | **POST** /calculatedmetrics/validate | Validate a calculated metric definition
[**find_calculated_metrics**](CalculatedmetricsApi.md#find_calculated_metrics) | **GET** /calculatedmetrics | Retrieve many calculated metrics
[**find_one_calculated_metric**](CalculatedmetricsApi.md#find_one_calculated_metric) | **GET** /calculatedmetrics/{id} | Retrieve a single calculated metric by id

# **calculatedmetrics_create_calculated_metric**
> AnalyticsCalculatedMetric calculatedmetrics_create_calculated_metric(body=body, locale=locale, expansion=expansion)

Create a new Calculated Metric

Creates a new calculated metric. The following attributes are available when creating a calculated metric:  IMPORTANT: Required Fields: name, definition, rsid  Optional fields: description  Example definition for use in testing API below (\"Visits per visitor\"):  ```json  \"definition\": {        \"formula\": {          \"func\": \"divide\",          \"col1\": {            \"func\": \"metric\",            \"name\": \"metrics/visits\",            \"description\": \"Visits\"          },          \"col2\": {            \"func\": \"metric\",            \"name\": \"metrics/visitors\",            \"description\": \"Unique Visitors\"          }        },        \"func\": \"calc-metric\",        \"version\": [          1,          0,          0        ]      } ```  A calculated metric response will always include these default items:* id, name, description, rsid, owner*   Other attributes can be optionally requested through the 'expansion' field as defined/documented in the GET endpoints (see GET \"/calculatedmetrics\" or GET \"/calculatedmetrics/{id}\" for more documentation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
body = swagger_client.AnalyticsCalculatedMetric() # AnalyticsCalculatedMetric | JSON-formatted Object containing key/value pairs for calculated metric creation. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional calculated metric metadata fields to include on response. (optional)

try:
    # Create a new Calculated Metric
    api_response = api_instance.calculatedmetrics_create_calculated_metric(body=body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_create_calculated_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)| JSON-formatted Object containing key/value pairs for calculated metric creation. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional calculated metric metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculatedmetrics_delete_calculated_metric**
> DeleteResponse calculatedmetrics_delete_calculated_metric(id, locale=locale)

Deletion of Calculated Metrics by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
id = 'id_example' # str | The calculated metric ID to be deleted
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Deletion of Calculated Metrics by Id
    api_response = api_instance.calculatedmetrics_delete_calculated_metric(id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_delete_calculated_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The calculated metric ID to be deleted | 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculatedmetrics_get_calculated_metric_function**
> CalcMetricFunction calculatedmetrics_get_calculated_metric_function(id, locale=locale)

Retrieve a calculated metric function by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
id = 'id_example' # str | The function ID to retrieve
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Retrieve a calculated metric function by id
    api_response = api_instance.calculatedmetrics_get_calculated_metric_function(id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_get_calculated_metric_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function ID to retrieve | 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**CalcMetricFunction**](CalcMetricFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculatedmetrics_get_calculated_metric_functions**
> list[CalcMetricFunction] calculatedmetrics_get_calculated_metric_functions(locale=locale)

Retrieve calculated metric functions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Retrieve calculated metric functions
    api_response = api_instance.calculatedmetrics_get_calculated_metric_functions(locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_get_calculated_metric_functions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**list[CalcMetricFunction]**](CalcMetricFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculatedmetrics_update_calculated_metric**
> AnalyticsCalculatedMetric calculatedmetrics_update_calculated_metric(id, body=body, locale=locale, expansion=expansion)

Update an existing calculated metric

The following fields can be modified through this endpoint: <br><b>name, description, definition, owner, rsid</b> Example \"defintion\" for use in testing API below (\"Visits per visitor\"):<br> \"definition\": {        \"formula\": {          \"func\": \"divide\",          \"col1\": {            \"func\": \"metric\",            \"name\": \"metrics/visits\",            \"description\": \"Visits\"          },          \"col2\": {            \"func\": \"metric\",            \"name\": \"metrics/visitors\",            \"description\": \"Unique Visitors\"          }        },        \"func\": \"calc-metric\",        \"version\": [          1,          0,          0        ]      }<br><br>Response will be the newly modified calculated metric object after the update request completes.<br><br><b><span style=\"text-decoration: underline;\">CalculatedMetricResponse</span></b><br>A calculated metric response will always include these default items:* id, name, description, rsid, owner*   Other attributes can be optionally requested through the 'expansion' field as defined/documented in the GET endpoints (see GET \"/calculatedmetrics\" or GET \"/calculatedmetrics/{id}\" for more documentation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
id = 'id_example' # str | Calculated Metric ID to be updated
body = swagger_client.AnalyticsCalculatedMetric() # AnalyticsCalculatedMetric | JSON-formatted Object containing key/value pairs to be updated. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional calculated metric metadata fields to include on response. (optional)

try:
    # Update an existing calculated metric
    api_response = api_instance.calculatedmetrics_update_calculated_metric(id, body=body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_update_calculated_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Calculated Metric ID to be updated | 
 **body** | [**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)| JSON-formatted Object containing key/value pairs to be updated. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional calculated metric metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculatedmetrics_validate_calculated_metric**
> AnalyticsCalculatedMetric calculatedmetrics_validate_calculated_metric(body=body, locale=locale, migrating=migrating)

Validate a calculated metric definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
body = swagger_client.AnalyticsCalculatedMetric() # AnalyticsCalculatedMetric | JSON-formatted Object containing key/value pairs for calculated metric validation. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
migrating = false # bool | Include migration functions in validation (optional) (default to false)

try:
    # Validate a calculated metric definition
    api_response = api_instance.calculatedmetrics_validate_calculated_metric(body=body, locale=locale, migrating=migrating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_validate_calculated_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)| JSON-formatted Object containing key/value pairs for calculated metric validation. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **migrating** | **bool**| Include migration functions in validation | [optional] [default to false]

### Return type

[**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_calculated_metrics**
> list[AnalyticsCalculatedMetric] find_calculated_metrics(rsids=rsids, owner_id=owner_id, filter_by_ids=filter_by_ids, to_be_used_in_rsid=to_be_used_in_rsid, locale=locale, name=name, tag_names=tag_names, favorite=favorite, approved=approved, limit=limit, page=page, sort_direction=sort_direction, sort_property=sort_property, expansion=expansion, include_type=include_type)

Retrieve many calculated metrics

A calculated metric response will always include these default items: *id, name, description, rsid, owner, polarity, precision, type*   Other attributes can be optionally requested through the 'expansion' field:  * *modified*: Date that the metric was last modified (ISO 8601) * *definition*: Calculated metric definition as JSON object * *compatibility*: Products that the metric is compatible with * *reportSuiteName*: Also return the friendly Report Suite name for the RSID * *tags*: Gives all existing tags associated with the calculated metric  For more information about calculated metrics go [here](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/calculatedmetrics.md)  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
rsids = 'rsids_example' # str | Filter list to only include calculated metrics tied to specified RSID list (comma-delimited) (optional)
owner_id = 56 # int | Filter list to only include calculated metrics owned by the specified loginId (optional)
filter_by_ids = 'filter_by_ids_example' # str | Filter list to only include calculated metrics in the specified list (comma-delimited list of IDs) (this is the same as calculatedMetricFilter, and is overwritten by calculatedMetricFilter (optional)
to_be_used_in_rsid = 'to_be_used_in_rsid_example' # str | The report suite where the calculated metric intended to be used.  This report suite will be used to determine things like compatibility and permissions.  If it is not specified then the permissions will be calculated based on the union of all metrics authorized in all groups the user belongs to.  If the compatibility expansion is specified and toBeUsedInRsid is not then the compatibility returned is based off the compatibility from the last time the calculated metric was saved. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
name = 'name_example' # str | Filter list to only include calculated metrics that contains the Name (optional)
tag_names = 'tag_names_example' # str | Filter list to only include calculated metrics that contains one of the tags (optional)
favorite = true # bool | Filter list to only include calculated metrics that are favorites (optional)
approved = true # bool | Filter list to only include calculated metrics that are approved (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)
sort_direction = 'ASC' # str | Sort direction (ASC or DESC) (optional) (default to ASC)
sort_property = 'id' # str | Property to sort by (name, modified_date, id is currently allowed) (optional) (default to id)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional calculated metric metadata fields to include on response. (optional)
include_type = ['include_type_example'] # list[str] | Include additional calculated metrics not owned by user. The \"all\" option takes precedence over \"shared\" (optional)

try:
    # Retrieve many calculated metrics
    api_response = api_instance.find_calculated_metrics(rsids=rsids, owner_id=owner_id, filter_by_ids=filter_by_ids, to_be_used_in_rsid=to_be_used_in_rsid, locale=locale, name=name, tag_names=tag_names, favorite=favorite, approved=approved, limit=limit, page=page, sort_direction=sort_direction, sort_property=sort_property, expansion=expansion, include_type=include_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->find_calculated_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsids** | **str**| Filter list to only include calculated metrics tied to specified RSID list (comma-delimited) | [optional] 
 **owner_id** | **int**| Filter list to only include calculated metrics owned by the specified loginId | [optional] 
 **filter_by_ids** | **str**| Filter list to only include calculated metrics in the specified list (comma-delimited list of IDs) (this is the same as calculatedMetricFilter, and is overwritten by calculatedMetricFilter | [optional] 
 **to_be_used_in_rsid** | **str**| The report suite where the calculated metric intended to be used.  This report suite will be used to determine things like compatibility and permissions.  If it is not specified then the permissions will be calculated based on the union of all metrics authorized in all groups the user belongs to.  If the compatibility expansion is specified and toBeUsedInRsid is not then the compatibility returned is based off the compatibility from the last time the calculated metric was saved. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **name** | **str**| Filter list to only include calculated metrics that contains the Name | [optional] 
 **tag_names** | **str**| Filter list to only include calculated metrics that contains one of the tags | [optional] 
 **favorite** | **bool**| Filter list to only include calculated metrics that are favorites | [optional] 
 **approved** | **bool**| Filter list to only include calculated metrics that are approved | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]
 **sort_direction** | **str**| Sort direction (ASC or DESC) | [optional] [default to ASC]
 **sort_property** | **str**| Property to sort by (name, modified_date, id is currently allowed) | [optional] [default to id]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional calculated metric metadata fields to include on response. | [optional] 
 **include_type** | [**list[str]**](str.md)| Include additional calculated metrics not owned by user. The \&quot;all\&quot; option takes precedence over \&quot;shared\&quot; | [optional] 

### Return type

[**list[AnalyticsCalculatedMetric]**](AnalyticsCalculatedMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_one_calculated_metric**
> AnalyticsCalculatedMetric find_one_calculated_metric(id, locale=locale, expansion=expansion)

Retrieve a single calculated metric by id

A calculated metric response will always include these default items: *id, name, description, rsid, owner, polarity, precision, type*   Other attributes can be optionally requested through the 'expansion' field:  * *modified*: Date that the metric was last modified (ISO 8601) * *definition*: Calculated metric definition as JSON object * *compatibility*: Products that the metric is compatible with * *reportSuiteName*: Also return the friendly Report Suite name for the RSID * *tags*: Gives all existing tags associated with the calculated metric  For more information about calculated metrics go [here](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/calculatedmetrics.md)  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi()
id = 'id_example' # str | The calculated metric ID to retrieve
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional calculated metric metadata fields to include on response. (optional)

try:
    # Retrieve a single calculated metric by id
    api_response = api_instance.find_one_calculated_metric(id, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->find_one_calculated_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The calculated metric ID to retrieve | 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional calculated metric metadata fields to include on response. | [optional] 

### Return type

[**AnalyticsCalculatedMetric**](AnalyticsCalculatedMetric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

