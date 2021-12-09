# swagger_client.ComponentMetadataSharesApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_share**](ComponentMetadataSharesApi.md#delete_share) | **DELETE** /componentmetadata/shares/{id} | Removes the shareId and all associations from that share
[**find_all_shares_for_company**](ComponentMetadataSharesApi.md#find_all_shares_for_company) | **GET** /componentmetadata/shares | Returns a list of shares for the current user&#x27;s company
[**get_share_by_id**](ComponentMetadataSharesApi.md#get_share_by_id) | **GET** /componentmetadata/shares/{id} | Retrieves an share by its id
[**save_share**](ComponentMetadataSharesApi.md#save_share) | **POST** /componentmetadata/shares | Saves the given share for the current user&#x27;s company
[**search_component_shares**](ComponentMetadataSharesApi.md#search_component_shares) | **POST** /componentmetadata/shares/component/search | search for shares for several components at once
[**shared_to_me**](ComponentMetadataSharesApi.md#shared_to_me) | **GET** /componentmetadata/shares/sharedto/me | get components shared with the current user by type
[**update_shares**](ComponentMetadataSharesApi.md#update_shares) | **PUT** /componentmetadata/shares | Share components with users. WARNING: Authoritative; deletes/overwrites all pre-existing shares for the given components

# **delete_share**
> InlineResponse200 delete_share(id)

Removes the shareId and all associations from that share

Delete by shareId. Will un-share the associated component with the entity shared with.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
id = 56 # int | The shareId to be deleted

try:
    # Removes the shareId and all associations from that share
    api_response = api_instance.delete_share(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->delete_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shareId to be deleted | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_shares_for_company**
> list[Share] find_all_shares_for_company(limit=limit, page=page)

Returns a list of shares for the current user's company

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # Returns a list of shares for the current user's company
    api_response = api_instance.find_all_shares_for_company(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->find_all_shares_for_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**list[Share]**](Share.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_by_id**
> Share get_share_by_id(id)

Retrieves an share by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
id = 56 # int | Share ID to be retrieved

try:
    # Retrieves an share by its id
    api_response = api_instance.get_share_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->get_share_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Share ID to be retrieved | 

### Return type

[**Share**](Share.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_share**
> Share save_share(body=body)

Saves the given share for the current user's company

Allows creation of a new share with a group/user/all

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
body = swagger_client.Share() # Share | JSON-formatted array of Share objects containing key-value pairs (optional)

try:
    # Saves the given share for the current user's company
    api_response = api_instance.save_share(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->save_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Share**](Share.md)| JSON-formatted array of Share objects containing key-value pairs | [optional] 

### Return type

[**Share**](Share.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_component_shares**
> SharedComponent search_component_shares(body=body, limit=limit, page=page)

search for shares for several components at once

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
body = swagger_client.ComponentSearch() # ComponentSearch | items to search for (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # search for shares for several components at once
    api_response = api_instance.search_component_shares(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->search_component_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComponentSearch**](ComponentSearch.md)| items to search for | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**SharedComponent**](SharedComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_to_me**
> list[str] shared_to_me(component_type)

get components shared with the current user by type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
component_type = 'component_type_example' # str | Component type to get shared ids for

try:
    # get components shared with the current user by type
    api_response = api_instance.shared_to_me(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->shared_to_me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type to get shared ids for | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shares**
> SharedComponent update_shares(body=body)

Share components with users. WARNING: Authoritative; deletes/overwrites all pre-existing shares for the given components

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentMetadataSharesApi()
body = swagger_client.SharedComponent() # SharedComponent | JSON-formatted array of Share objects containing key-value pairs (optional)

try:
    # Share components with users. WARNING: Authoritative; deletes/overwrites all pre-existing shares for the given components
    api_response = api_instance.update_shares(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentMetadataSharesApi->update_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharedComponent**](SharedComponent.md)| JSON-formatted array of Share objects containing key-value pairs | [optional] 

### Return type

[**SharedComponent**](SharedComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

