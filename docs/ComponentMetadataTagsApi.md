# swagger_client.ComponentMetadataTagsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tag**](ComponentMetadataTagsApi.md#delete_tag) | **DELETE** /componentmetadata/tags/{id} | Removes the tagId and all associations from that tag to any components
[**delete_tag_items**](ComponentMetadataTagsApi.md#delete_tag_items) | **DELETE** /componentmetadata/tags | Disassociates all tags from the given components
[**find_all_for_company**](ComponentMetadataTagsApi.md#find_all_for_company) | **GET** /componentmetadata/tags | Returns a list of tags for the current user&#x27;s company
[**get_components_by_tag_name**](ComponentMetadataTagsApi.md#get_components_by_tag_name) | **GET** /componentmetadata/tags/tagnames | Retrieves component ids associated with the given tag names
[**get_tag_by_id**](ComponentMetadataTagsApi.md#get_tag_by_id) | **GET** /componentmetadata/tags/{id} | Retrieves an tag by its id
[**get_tag_list_by_component_id_and_component_type**](ComponentMetadataTagsApi.md#get_tag_list_by_component_id_and_component_type) | **GET** /componentmetadata/tags/search | Retrieves a tags for a given component by componentId and componentType
[**save_tag_component_list**](ComponentMetadataTagsApi.md#save_tag_component_list) | **PUT** /componentmetadata/tags/tagitems | Tag a component with one or many tags at once. WARNING: Authoritative; deletes/overwrites all pre-existing associations
[**save_tag_list**](ComponentMetadataTagsApi.md#save_tag_list) | **POST** /componentmetadata/tags | Saves the given tag(s) for the current user&#x27;s company
[**search_component_tags2**](ComponentMetadataTagsApi.md#search_component_tags2) | **POST** /componentmetadata/tags/component/search | search for tags for several components at once

# **delete_tag**
> list[dict(str, object)] delete_tag(id)

Removes the tagId and all associations from that tag to any components

Delete by tagId. Will un-tag any/all components that were associated with the passed tagId.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
id = 56 # int | The tagId to be deleted

try:
    # Removes the tagId and all associations from that tag to any components
    api_response = api_instance.delete_tag(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tagId to be deleted | 

### Return type

**list[dict(str, object)]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_items**
> list[dict(str, object)] delete_tag_items(component_ids, component_type)

Disassociates all tags from the given components

Removes all tags from the passed componentIds. Note that currently this is done in a single DB query, so there is a single combined response for the entire operation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
component_ids = 'component_ids_example' # str | Comma-separated list of componentIds to operate on.
component_type = 'component_type_example' # str | The component type to operate on.

try:
    # Disassociates all tags from the given components
    api_response = api_instance.delete_tag_items(component_ids, component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->delete_tag_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_ids** | **str**| Comma-separated list of componentIds to operate on. | 
 **component_type** | **str**| The component type to operate on. | 

### Return type

**list[dict(str, object)]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_for_company**
> list[Tag] find_all_for_company(limit=limit, page=page)

Returns a list of tags for the current user's company

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # Returns a list of tags for the current user's company
    api_response = api_instance.find_all_for_company(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->find_all_for_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components_by_tag_name**
> list[str] get_components_by_tag_name(tag_names, component_type)

Retrieves component ids associated with the given tag names

Given a comma separated list of tag names, return component ids associated with them.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
tag_names = 'tag_names_example' # str | Comma separated list of tag names.
component_type = 'component_type_example' # str | The component type to operate on.

try:
    # Retrieves component ids associated with the given tag names
    api_response = api_instance.get_components_by_tag_name(tag_names, component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->get_components_by_tag_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_names** | **str**| Comma separated list of tag names. | 
 **component_type** | **str**| The component type to operate on. | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_by_id**
> Tag get_tag_by_id(id)

Retrieves an tag by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
id = 56 # int | Tag ID to be retrieved

try:
    # Retrieves an tag by its id
    api_response = api_instance.get_tag_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->get_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tag ID to be retrieved | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_list_by_component_id_and_component_type**
> list[Tag] get_tag_list_by_component_id_and_component_type(component_id, component_type)

Retrieves a tags for a given component by componentId and componentType

Given a componentId, return all tags associated with that component

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
component_id = 'component_id_example' # str | The componentId to operate on. Currently this is just the segmentId.
component_type = 'component_type_example' # str | The component type to operate on.

try:
    # Retrieves a tags for a given component by componentId and componentType
    api_response = api_instance.get_tag_list_by_component_id_and_component_type(component_id, component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->get_tag_list_by_component_id_and_component_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| The componentId to operate on. Currently this is just the segmentId. | 
 **component_type** | **str**| The component type to operate on. | 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_tag_component_list**
> list[TaggedComponent] save_tag_component_list(body=body)

Tag a component with one or many tags at once. WARNING: Authoritative; deletes/overwrites all pre-existing associations

This endpoint allows many tags at once to be created/deleted. Any tags passed to this endpoint will become the *only* tags for that componentId (all other tags will be removed).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
body = [swagger_client.TaggedComponent()] # list[TaggedComponent] | JSON-formatted object containing key-value pairs that conform to the schema (optional)

try:
    # Tag a component with one or many tags at once. WARNING: Authoritative; deletes/overwrites all pre-existing associations
    api_response = api_instance.save_tag_component_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->save_tag_component_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[TaggedComponent]**](TaggedComponent.md)| JSON-formatted object containing key-value pairs that conform to the schema | [optional] 

### Return type

[**list[TaggedComponent]**](TaggedComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_tag_list**
> list[Tag] save_tag_list(body=body)

Saves the given tag(s) for the current user's company

Allows creation of a new tag and applies that new tag to the passed component

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
body = [swagger_client.Tag()] # list[Tag] | JSON-formatted array of Tag objects containing key-value pairs (optional)

try:
    # Saves the given tag(s) for the current user's company
    api_response = api_instance.save_tag_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->save_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Tag]**](Tag.md)| JSON-formatted array of Tag objects containing key-value pairs | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_component_tags2**
> TaggedComponent search_component_tags2(body=body, limit=limit, page=page)

search for tags for several components at once

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataTagsApi()
body = swagger_client.ComponentSearch() # ComponentSearch | items to search for (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # search for tags for several components at once
    api_response = api_instance.search_component_tags2(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataTagsApi->search_component_tags2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComponentSearch**](ComponentSearch.md)| items to search for | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**TaggedComponent**](TaggedComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

