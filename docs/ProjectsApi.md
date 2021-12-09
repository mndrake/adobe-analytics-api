# swagger_client.ProjectsApi

All URIs are relative to *https://analytics.adobe.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_create_project**](ProjectsApi.md#projects_create_project) | **POST** /projects | Creates a single project.
[**projects_delete_project**](ProjectsApi.md#projects_delete_project) | **DELETE** /projects/{projectId} | deletes a project.
[**projects_get_project**](ProjectsApi.md#projects_get_project) | **GET** /projects/{projectId} | Retrieves configuration for a Project.
[**projects_get_projects**](ProjectsApi.md#projects_get_projects) | **GET** /projects | Returns a list of projects for the user
[**projects_update_project**](ProjectsApi.md#projects_update_project) | **PUT** /projects/{projectId} | Updates configuration for a project.
[**projects_validate_project**](ProjectsApi.md#projects_validate_project) | **POST** /projects/validate | Validates a Project definition

# **projects_create_project**
> AnalyticsProject projects_create_project(body=body, expansion=expansion, locale=locale)

Creates a single project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.AnalyticsProject() # AnalyticsProject | JSON-formatted Object containing project keys/value pairs to be updated. (optional)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional project metadata fields to include on response. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Creates a single project.
    api_response = api_instance.projects_create_project(body=body, expansion=expansion, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsProject**](AnalyticsProject.md)| JSON-formatted Object containing project keys/value pairs to be updated. | [optional] 
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional project metadata fields to include on response. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**AnalyticsProject**](AnalyticsProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete_project**
> DeleteResponse projects_delete_project(project_id, locale=locale)

deletes a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 'project_id_example' # str | The Project id for which to retrieve information
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # deletes a project.
    api_response = api_instance.projects_delete_project(project_id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The Project id for which to retrieve information | 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project**
> AnalyticsProject projects_get_project(project_id, expansion=expansion, locale=locale)

Retrieves configuration for a Project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 'project_id_example' # str | The Project id for which to retrieve information
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional project metadata fields to include on response. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Retrieves configuration for a Project.
    api_response = api_instance.projects_get_project(project_id, expansion=expansion, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The Project id for which to retrieve information | 
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional project metadata fields to include on response. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**AnalyticsProject**](AnalyticsProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects**
> list[AnalyticsProject] projects_get_projects(include_type=include_type, expansion=expansion, filter_by_ids=filter_by_ids, locale=locale, pagination=pagination, owner_id=owner_id, limit=limit, page=page)

Returns a list of projects for the user

This Returns the projects list primarily for the Analytics product. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
include_type = ['include_type_example'] # list[str] | Include additional projects not owned by user. The \"all\" option takes precedence over \"shared\". If neither guided, or project is included, both types are returned (optional)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional project metadata fields to include on response. (optional)
filter_by_ids = 'filter_by_ids_example' # str | Filter list to only include projects in the specified list (comma-delimited list of IDs) (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
pagination = 'false' # str | return paginated results (optional) (default to false)
owner_id = 56 # int | Filter list to only include projects owned by the specified loginId (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
page = 0 # int | Page number (base 0 - first page is \"0\") (optional) (default to 0)

try:
    # Returns a list of projects for the user
    api_response = api_instance.projects_get_projects(include_type=include_type, expansion=expansion, filter_by_ids=filter_by_ids, locale=locale, pagination=pagination, owner_id=owner_id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_type** | [**list[str]**](str.md)| Include additional projects not owned by user. The \&quot;all\&quot; option takes precedence over \&quot;shared\&quot;. If neither guided, or project is included, both types are returned | [optional] 
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional project metadata fields to include on response. | [optional] 
 **filter_by_ids** | **str**| Filter list to only include projects in the specified list (comma-delimited list of IDs) | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]
 **pagination** | **str**| return paginated results | [optional] [default to false]
 **owner_id** | **int**| Filter list to only include projects owned by the specified loginId | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **page** | **int**| Page number (base 0 - first page is \&quot;0\&quot;) | [optional] [default to 0]

### Return type

[**list[AnalyticsProject]**](AnalyticsProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update_project**
> AnalyticsProject projects_update_project(project_id, body=body, expansion=expansion, locale=locale)

Updates configuration for a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 'project_id_example' # str | The Project id for which to retrieve information
body = swagger_client.AnalyticsProject() # AnalyticsProject | JSON-formatted Object containing project keys/value pairs to be updated. (optional)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional project metadata fields to include on response. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Updates configuration for a project.
    api_response = api_instance.projects_update_project(project_id, body=body, expansion=expansion, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The Project id for which to retrieve information | 
 **body** | [**AnalyticsProject**](AnalyticsProject.md)| JSON-formatted Object containing project keys/value pairs to be updated. | [optional] 
 **expansion** | [**list[str]**](str.md)| Comma-delimited list of additional project metadata fields to include on response. | [optional] 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**AnalyticsProject**](AnalyticsProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_validate_project**
> ProjectCompatibility projects_validate_project(body, locale=locale)

Validates a Project definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.ProjectsValidateBody() # ProjectsValidateBody | JSON-formatted Object containing key/value pairs for Project validation.
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Validates a Project definition
    api_response = api_instance.projects_validate_project(body, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_validate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectsValidateBody**](ProjectsValidateBody.md)| JSON-formatted Object containing key/value pairs for Project validation. | 
 **locale** | **str**| Locale | [optional] [default to en_US]

### Return type

[**ProjectCompatibility**](ProjectCompatibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

