# swagger_client.UsersApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all**](UsersApi.md#find_all) | **GET** /users | Returns a list of users for the current user&#x27;s login company
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/me | Get the current user

# **find_all**
> list[AnalyticsUser] find_all(limit=limit, page=page)

Returns a list of users for the current user's login company

Retrieves a list of all users for the company designated by the auth token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # Returns a list of users for the current user's login company
    api_response = api_instance.find_all(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**list[AnalyticsUser]**](AnalyticsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> AnalyticsUser get_current_user()

Get the current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get the current user
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalyticsUser**](AnalyticsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

