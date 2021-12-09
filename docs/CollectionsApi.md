# swagger_client.CollectionsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all**](CollectionsApi.md#find_all) | **GET** /collections/suites | Retrieves report suites that match the given filters.
[**find_one**](CollectionsApi.md#find_one) | **GET** /collections/suites/{rsid} | Retrieves report suite by id

# **find_all**
> SuiteCollectionItem find_all(rsids=rsids, rsid_contains=rsid_contains, limit=limit, page=page, expansion=expansion)

Retrieves report suites that match the given filters.

Returns all report suite types in a single collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
rsids = 'rsids_example' # str | Filter list to only include suites in this RSID list (comma-delimited) (optional)
rsid_contains = 'rsid_contains_example' # str | Filter list to only include suites whose rsid contains rsidContains. (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional metadata fields to include on response. (optional)

try:
    # Retrieves report suites that match the given filters.
    api_response = api_instance.find_all(rsids=rsids, rsid_contains=rsid_contains, limit=limit, page=page, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsids** | **str**| Filter list to only include suites in this RSID list (comma-delimited) | [optional] 
 **rsid_contains** | **str**| Filter list to only include suites whose rsid contains rsidContains. | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional metadata fields to include on response. | [optional] 

### Return type

[**SuiteCollectionItem**](SuiteCollectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_one**
> SuiteCollectionItem find_one(rsid, expansion=expansion)

Retrieves report suite by id

Returns all report suite types in a single collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
rsid = 'rsid_example' # str | The rsid of the suite to return
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional metadata fields to include on response. (optional)

try:
    # Retrieves report suite by id
    api_response = api_instance.find_one(rsid, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsid** | **str**| The rsid of the suite to return | 
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional metadata fields to include on response. | [optional] 

### Return type

[**SuiteCollectionItem**](SuiteCollectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

