# swagger_client.UsagelogsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_access_logs**](UsagelogsApi.md#get_usage_access_logs) | **GET** /auditlogs/usage | Retrieves usage and access logs for the search criteria provided.

# **get_usage_access_logs**
> ResponsePageUsageLogDto get_usage_access_logs(start_date, end_date, login=login, ip=ip, rsid=rsid, event_type=event_type, event=event, limit=limit, page=page)

Retrieves usage and access logs for the search criteria provided.

This API returns the usage and access logs for a given date range within a 3 month period. This API authenticates with an IMS user token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsagelogsApi()
start_date = '2021-01-01T00:00:00-07' # str | Start date for the maximum of a 3 month period. (default to 2021-01-01T00:00:00-07)
end_date = '2021-01-02T14:32:33-07' # str | End date for the maximum of a 3 month period. (default to 2021-01-02T14:32:33-07)
login = 'login_example' # str | The login value of the user you want to filter logs by. (optional)
ip = 'ip_example' # str | The IP address you want to filter logs by. (optional)
rsid = 'rsid_example' # str | The report suite ID you want to filter logs by. (optional)
event_type = 'event_type_example' # str | The numeric id for the event type you want to filter logs by. (optional)
event = 'event_example' # str | The event description you want to filter logs by. No wildcards permitted. (optional)
limit = 10 # int | Number of results per page. (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\"). (optional) (default to 0)

try:
    # Retrieves usage and access logs for the search criteria provided.
    api_response = api_instance.get_usage_access_logs(start_date, end_date, login=login, ip=ip, rsid=rsid, event_type=event_type, event=event, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsagelogsApi->get_usage_access_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date for the maximum of a 3 month period. | [default to 2021-01-01T00:00:00-07]
 **end_date** | **str**| End date for the maximum of a 3 month period. | [default to 2021-01-02T14:32:33-07]
 **login** | **str**| The login value of the user you want to filter logs by. | [optional] 
 **ip** | **str**| The IP address you want to filter logs by. | [optional] 
 **rsid** | **str**| The report suite ID you want to filter logs by. | [optional] 
 **event_type** | **str**| The numeric id for the event type you want to filter logs by. | [optional] 
 **event** | **str**| The event description you want to filter logs by. No wildcards permitted. | [optional] 
 **limit** | **int**| Number of results per page. | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;). | [optional] [default to 0]

### Return type

[**ResponsePageUsageLogDto**](ResponsePageUsageLogDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

