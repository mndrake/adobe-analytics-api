# swagger_client.ReportsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_report**](ReportsApi.md#run_report) | **POST** /reports | Runs a report for the request in the post body
[**run_top_item_report**](ReportsApi.md#run_top_item_report) | **GET** /reports/topItems | Runs a top items report for the request in the post body

# **run_report**
> RankedReportData run_report(body=body)

Runs a report for the request in the post body

See the [Reporting User Guide](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/reporting-guide.md) for details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.RankedRequest() # RankedRequest |  (optional)

try:
    # Runs a report for the request in the post body
    api_response = api_instance.run_report(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->run_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RankedRequest**](RankedRequest.md)|  | [optional] 

### Return type

[**RankedReportData**](RankedReportData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_top_item_report**
> UnhashReportData run_top_item_report(rsid, dimension, locale=locale, date_range=date_range, search_clause=search_clause, start_date=start_date, end_date=end_date, search_and=search_and, search_or=search_or, search_not=search_not, search_phrase=search_phrase, search_phrase=search_phrase, lookup_none_values=lookup_none_values, limit=limit, page=page)

Runs a top items report for the request in the post body

Get the top X items (based on paging restriction) for the specified dimension and rsid. Defaults to last 90 days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
rsid = 'rsid_example' # str | ID of desired report suite ie. myrsid
dimension = 'dimension_example' # str | Dimension to run the report against. Example: 'variables/page'
locale = 'en_US' # str | Locale that system named metrics should be returned in (optional) (default to en_US)
date_range = 'date_range_example' # str | Format: YYYY-MM-DD/YYYY-MM-DD (optional)
search_clause = 'search_clause_example' # str | General search string; wrap with single quotes. Example: 'PageABC' (optional)
start_date = 'start_date_example' # str | Format: YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | Format: YYYY-MM-DD (optional)
search_and = 'search_and_example' # str | Search terms that will be AND-ed together. Space delimited. (optional)
search_or = 'search_or_example' # str | Search terms that will be OR-ed together. Space delimited. (optional)
search_not = 'search_not_example' # str | Search terms that will be treated as NOT including. Space delimited. (optional)
search_phrase = 'search_phrase_example' # str | A full search phrase that will be searched for. (optional)
search_phrase = 'search_phrase_example' # str | A full search phrase that will be searched for. (optional)
lookup_none_values = true # bool | Controls None values to be included (optional) (default to true)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # Runs a top items report for the request in the post body
    api_response = api_instance.run_top_item_report(rsid, dimension, locale=locale, date_range=date_range, search_clause=search_clause, start_date=start_date, end_date=end_date, search_and=search_and, search_or=search_or, search_not=search_not, search_phrase=search_phrase, search_phrase=search_phrase, lookup_none_values=lookup_none_values, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->run_top_item_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsid** | **str**| ID of desired report suite ie. myrsid | 
 **dimension** | **str**| Dimension to run the report against. Example: &#x27;variables/page&#x27; | 
 **locale** | **str**| Locale that system named metrics should be returned in | [optional] [default to en_US]
 **date_range** | **str**| Format: YYYY-MM-DD/YYYY-MM-DD | [optional] 
 **search_clause** | **str**| General search string; wrap with single quotes. Example: &#x27;PageABC&#x27; | [optional] 
 **start_date** | **str**| Format: YYYY-MM-DD | [optional] 
 **end_date** | **str**| Format: YYYY-MM-DD | [optional] 
 **search_and** | **str**| Search terms that will be AND-ed together. Space delimited. | [optional] 
 **search_or** | **str**| Search terms that will be OR-ed together. Space delimited. | [optional] 
 **search_not** | **str**| Search terms that will be treated as NOT including. Space delimited. | [optional] 
 **search_phrase** | **str**| A full search phrase that will be searched for. | [optional] 
 **search_phrase** | **str**| A full search phrase that will be searched for. | [optional] 
 **lookup_none_values** | **bool**| Controls None values to be included | [optional] [default to true]
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**UnhashReportData**](UnhashReportData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

