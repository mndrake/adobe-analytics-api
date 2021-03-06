# swagger-client
The endpoints described here are routed through Adobe.io.          In order to use these endpoints you must create an oAuth client that is          subscribed to access the Adobe Analytics Reporting API.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1 - Build: 2019-10-03_20:32:29.323
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AnalyticsCalculatedMetric() # AnalyticsCalculatedMetric | JSON-formatted Object containing key/value pairs for calculated metric creation. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
expansion = ['expansion_example'] # list[str] | Comma-delimited list of additional calculated metric metadata fields to include on response. (optional)

try:
    # Create a new Calculated Metric
    api_response = api_instance.calculatedmetrics_create_calculated_metric(body=body, locale=locale, expansion=expansion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_create_calculated_metric: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The calculated metric ID to be deleted
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Deletion of Calculated Metrics by Id
    api_response = api_instance.calculatedmetrics_delete_calculated_metric(id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_delete_calculated_metric: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The function ID to retrieve
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Retrieve a calculated metric function by id
    api_response = api_instance.calculatedmetrics_get_calculated_metric_function(id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_get_calculated_metric_function: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
locale = 'en_US' # str | Locale (optional) (default to en_US)

try:
    # Retrieve calculated metric functions
    api_response = api_instance.calculatedmetrics_get_calculated_metric_functions(locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_get_calculated_metric_functions: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
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

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AnalyticsCalculatedMetric() # AnalyticsCalculatedMetric | JSON-formatted Object containing key/value pairs for calculated metric validation. (optional)
locale = 'en_US' # str | Locale (optional) (default to en_US)
migrating = false # bool | Include migration functions in validation (optional) (default to false)

try:
    # Validate a calculated metric definition
    api_response = api_instance.calculatedmetrics_validate_calculated_metric(body=body, locale=locale, migrating=migrating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculatedmetricsApi->calculatedmetrics_validate_calculated_metric: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
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

# create an instance of the API class
api_instance = swagger_client.CalculatedmetricsApi(swagger_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://analytics.adobe.io/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CalculatedmetricsApi* | [**calculatedmetrics_create_calculated_metric**](docs/CalculatedmetricsApi.md#calculatedmetrics_create_calculated_metric) | **POST** /calculatedmetrics | Create a new Calculated Metric
*CalculatedmetricsApi* | [**calculatedmetrics_delete_calculated_metric**](docs/CalculatedmetricsApi.md#calculatedmetrics_delete_calculated_metric) | **DELETE** /calculatedmetrics/{id} | Deletion of Calculated Metrics by Id
*CalculatedmetricsApi* | [**calculatedmetrics_get_calculated_metric_function**](docs/CalculatedmetricsApi.md#calculatedmetrics_get_calculated_metric_function) | **GET** /calculatedmetrics/functions/{id} | Retrieve a calculated metric function by id
*CalculatedmetricsApi* | [**calculatedmetrics_get_calculated_metric_functions**](docs/CalculatedmetricsApi.md#calculatedmetrics_get_calculated_metric_functions) | **GET** /calculatedmetrics/functions | Retrieve calculated metric functions
*CalculatedmetricsApi* | [**calculatedmetrics_update_calculated_metric**](docs/CalculatedmetricsApi.md#calculatedmetrics_update_calculated_metric) | **PUT** /calculatedmetrics/{id} | Update an existing calculated metric
*CalculatedmetricsApi* | [**calculatedmetrics_validate_calculated_metric**](docs/CalculatedmetricsApi.md#calculatedmetrics_validate_calculated_metric) | **POST** /calculatedmetrics/validate | Validate a calculated metric definition
*CalculatedmetricsApi* | [**find_calculated_metrics**](docs/CalculatedmetricsApi.md#find_calculated_metrics) | **GET** /calculatedmetrics | Retrieve many calculated metrics
*CalculatedmetricsApi* | [**find_one_calculated_metric**](docs/CalculatedmetricsApi.md#find_one_calculated_metric) | **GET** /calculatedmetrics/{id} | Retrieve a single calculated metric by id
*CollectionsApi* | [**find_all**](docs/CollectionsApi.md#find_all) | **GET** /collections/suites | Retrieves report suites that match the given filters.
*CollectionsApi* | [**find_one**](docs/CollectionsApi.md#find_one) | **GET** /collections/suites/{rsid} | Retrieves report suite by id
*ComponentMetadataSharesApi* | [**delete_share**](docs/ComponentMetadataSharesApi.md#delete_share) | **DELETE** /componentmetadata/shares/{id} | Removes the shareId and all associations from that share
*ComponentMetadataSharesApi* | [**find_all_shares_for_company**](docs/ComponentMetadataSharesApi.md#find_all_shares_for_company) | **GET** /componentmetadata/shares | Returns a list of shares for the current user&#x27;s company
*ComponentMetadataSharesApi* | [**get_share_by_id**](docs/ComponentMetadataSharesApi.md#get_share_by_id) | **GET** /componentmetadata/shares/{id} | Retrieves an share by its id
*ComponentMetadataSharesApi* | [**save_share**](docs/ComponentMetadataSharesApi.md#save_share) | **POST** /componentmetadata/shares | Saves the given share for the current user&#x27;s company
*ComponentMetadataSharesApi* | [**search_component_shares**](docs/ComponentMetadataSharesApi.md#search_component_shares) | **POST** /componentmetadata/shares/component/search | search for shares for several components at once
*ComponentMetadataSharesApi* | [**shared_to_me**](docs/ComponentMetadataSharesApi.md#shared_to_me) | **GET** /componentmetadata/shares/sharedto/me | get components shared with the current user by type
*ComponentMetadataSharesApi* | [**update_shares**](docs/ComponentMetadataSharesApi.md#update_shares) | **PUT** /componentmetadata/shares | Share components with users. WARNING: Authoritative; deletes/overwrites all pre-existing shares for the given components
*ComponentMetadataTagsApi* | [**delete_tag**](docs/ComponentMetadataTagsApi.md#delete_tag) | **DELETE** /componentmetadata/tags/{id} | Removes the tagId and all associations from that tag to any components
*ComponentMetadataTagsApi* | [**delete_tag_items**](docs/ComponentMetadataTagsApi.md#delete_tag_items) | **DELETE** /componentmetadata/tags | Disassociates all tags from the given components
*ComponentMetadataTagsApi* | [**find_all_for_company**](docs/ComponentMetadataTagsApi.md#find_all_for_company) | **GET** /componentmetadata/tags | Returns a list of tags for the current user&#x27;s company
*ComponentMetadataTagsApi* | [**get_components_by_tag_name**](docs/ComponentMetadataTagsApi.md#get_components_by_tag_name) | **GET** /componentmetadata/tags/tagnames | Retrieves component ids associated with the given tag names
*ComponentMetadataTagsApi* | [**get_tag_by_id**](docs/ComponentMetadataTagsApi.md#get_tag_by_id) | **GET** /componentmetadata/tags/{id} | Retrieves an tag by its id
*ComponentMetadataTagsApi* | [**get_tag_list_by_component_id_and_component_type**](docs/ComponentMetadataTagsApi.md#get_tag_list_by_component_id_and_component_type) | **GET** /componentmetadata/tags/search | Retrieves a tags for a given component by componentId and componentType
*ComponentMetadataTagsApi* | [**save_tag_component_list**](docs/ComponentMetadataTagsApi.md#save_tag_component_list) | **PUT** /componentmetadata/tags/tagitems | Tag a component with one or many tags at once. WARNING: Authoritative; deletes/overwrites all pre-existing associations
*ComponentMetadataTagsApi* | [**save_tag_list**](docs/ComponentMetadataTagsApi.md#save_tag_list) | **POST** /componentmetadata/tags | Saves the given tag(s) for the current user&#x27;s company
*ComponentMetadataTagsApi* | [**search_component_tags2**](docs/ComponentMetadataTagsApi.md#search_component_tags2) | **POST** /componentmetadata/tags/component/search | search for tags for several components at once
*DaterangesApi* | [**create_date_range**](docs/DaterangesApi.md#create_date_range) | **POST** /dateranges | Creates configuration for a DateRange.
*DaterangesApi* | [**delete_date_range**](docs/DaterangesApi.md#delete_date_range) | **DELETE** /dateranges/{dateRangeId} | Deletes a DateRange.
*DaterangesApi* | [**get_date_range**](docs/DaterangesApi.md#get_date_range) | **GET** /dateranges/{dateRangeId} | Retrieves configuration for a DateRange.
*DaterangesApi* | [**get_date_ranges**](docs/DaterangesApi.md#get_date_ranges) | **GET** /dateranges | Returns a list of dateranges for the user
*DaterangesApi* | [**update_date_range**](docs/DaterangesApi.md#update_date_range) | **PUT** /dateranges/{dateRangeId} | Updates configuration for a DateRange.
*DimensionsApi* | [**dimensions_get_dimension**](docs/DimensionsApi.md#dimensions_get_dimension) | **GET** /dimensions/{dimensionId} | Returns a dimension for the given report suite
*DimensionsApi* | [**dimensions_get_dimensions**](docs/DimensionsApi.md#dimensions_get_dimensions) | **GET** /dimensions | Returns a list of dimensions for a given report suite.
*MetricsApi* | [**get_metric**](docs/MetricsApi.md#get_metric) | **GET** /metrics/{id} | Returns a metric for the given report suite
*MetricsApi* | [**get_metrics**](docs/MetricsApi.md#get_metrics) | **GET** /metrics | Returns a list of metrics for the given report suite
*ProjectsApi* | [**projects_create_project**](docs/ProjectsApi.md#projects_create_project) | **POST** /projects | Creates a single project.
*ProjectsApi* | [**projects_delete_project**](docs/ProjectsApi.md#projects_delete_project) | **DELETE** /projects/{projectId} | deletes a project.
*ProjectsApi* | [**projects_get_project**](docs/ProjectsApi.md#projects_get_project) | **GET** /projects/{projectId} | Retrieves configuration for a Project.
*ProjectsApi* | [**projects_get_projects**](docs/ProjectsApi.md#projects_get_projects) | **GET** /projects | Returns a list of projects for the user
*ProjectsApi* | [**projects_update_project**](docs/ProjectsApi.md#projects_update_project) | **PUT** /projects/{projectId} | Updates configuration for a project.
*ProjectsApi* | [**projects_validate_project**](docs/ProjectsApi.md#projects_validate_project) | **POST** /projects/validate | Validates a Project definition
*ReportsApi* | [**run_report**](docs/ReportsApi.md#run_report) | **POST** /reports | Runs a report for the request in the post body
*ReportsApi* | [**run_top_item_report**](docs/ReportsApi.md#run_top_item_report) | **GET** /reports/topItems | Runs a top items report for the request in the post body
*SegmentsApi* | [**segments_create_segment**](docs/SegmentsApi.md#segments_create_segment) | **POST** /segments | Creates Segment
*SegmentsApi* | [**segments_delete_segment**](docs/SegmentsApi.md#segments_delete_segment) | **DELETE** /segments/{id} | Delete Segment
*SegmentsApi* | [**segments_get_segment**](docs/SegmentsApi.md#segments_get_segment) | **GET** /segments/{id} | Get a Single Segment
*SegmentsApi* | [**segments_get_segments**](docs/SegmentsApi.md#segments_get_segments) | **GET** /segments | Retrieve All Segments
*SegmentsApi* | [**segments_update_segment**](docs/SegmentsApi.md#segments_update_segment) | **PUT** /segments/{id} | Update a Segment
*SegmentsApi* | [**segments_validate_segment**](docs/SegmentsApi.md#segments_validate_segment) | **POST** /segments/validate | Validate a Segment
*UsagelogsApi* | [**get_usage_access_logs**](docs/UsagelogsApi.md#get_usage_access_logs) | **GET** /auditlogs/usage | Retrieves usage and access logs for the search criteria provided.
*UsersApi* | [**find_all**](docs/UsersApi.md#find_all) | **GET** /users | Returns a list of users for the current user&#x27;s login company
*UsersApi* | [**get_current_user**](docs/UsersApi.md#get_current_user) | **GET** /users/me | Get the current user

## Documentation For Models

 - [AnalyticsCalculatedMetric](docs/AnalyticsCalculatedMetric.md)
 - [AnalyticsDateRange](docs/AnalyticsDateRange.md)
 - [AnalyticsDateRangeDefinition](docs/AnalyticsDateRangeDefinition.md)
 - [AnalyticsDimension](docs/AnalyticsDimension.md)
 - [AnalyticsMetric](docs/AnalyticsMetric.md)
 - [AnalyticsProject](docs/AnalyticsProject.md)
 - [AnalyticsSegment](docs/AnalyticsSegment.md)
 - [AnalyticsSegmentDefinition](docs/AnalyticsSegmentDefinition.md)
 - [AnalyticsSegmentDefinitionContainer](docs/AnalyticsSegmentDefinitionContainer.md)
 - [AnalyticsSegmentDefinitionContainerPred](docs/AnalyticsSegmentDefinitionContainerPred.md)
 - [AnalyticsSegmentDefinitionContainerPredVal](docs/AnalyticsSegmentDefinitionContainerPredVal.md)
 - [AnalyticsSegmentResponseItem](docs/AnalyticsSegmentResponseItem.md)
 - [AnalyticsUser](docs/AnalyticsUser.md)
 - [AnalyticsVirtualReportSuite](docs/AnalyticsVirtualReportSuite.md)
 - [CalcMetricCompatibility](docs/CalcMetricCompatibility.md)
 - [CalcMetricFunction](docs/CalcMetricFunction.md)
 - [CalcMetricFunctionDef](docs/CalcMetricFunctionDef.md)
 - [CalcMetricFunctionParameter](docs/CalcMetricFunctionParameter.md)
 - [CalculatedMetricDef](docs/CalculatedMetricDef.md)
 - [CalculatedMetricErrorStatus](docs/CalculatedMetricErrorStatus.md)
 - [CalendarType](docs/CalendarType.md)
 - [Column](docs/Column.md)
 - [ComponentSearch](docs/ComponentSearch.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [IdentityMetric](docs/IdentityMetric.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse200Success](docs/InlineResponse200Success.md)
 - [JsonNode](docs/JsonNode.md)
 - [Locale](docs/Locale.md)
 - [NoneSettings](docs/NoneSettings.md)
 - [Owner](docs/Owner.md)
 - [Pageable](docs/Pageable.md)
 - [PredictiveSettings](docs/PredictiveSettings.md)
 - [ProjectCompatibility](docs/ProjectCompatibility.md)
 - [ProjectsValidateBody](docs/ProjectsValidateBody.md)
 - [PublishingStatus](docs/PublishingStatus.md)
 - [RankedColumnError](docs/RankedColumnError.md)
 - [RankedColumnMetaData](docs/RankedColumnMetaData.md)
 - [RankedReportData](docs/RankedReportData.md)
 - [RankedRequest](docs/RankedRequest.md)
 - [RankedSettings](docs/RankedSettings.md)
 - [RankedStatistics](docs/RankedStatistics.md)
 - [RankedSummaryData](docs/RankedSummaryData.md)
 - [ReportDimension](docs/ReportDimension.md)
 - [ReportErrorStatus](docs/ReportErrorStatus.md)
 - [ReportFilter](docs/ReportFilter.md)
 - [ReportMetric](docs/ReportMetric.md)
 - [ReportMetricPredictiveSettings](docs/ReportMetricPredictiveSettings.md)
 - [ReportMetrics](docs/ReportMetrics.md)
 - [ReportRow](docs/ReportRow.md)
 - [ReportRows](docs/ReportRows.md)
 - [ReportSearch](docs/ReportSearch.md)
 - [ResponsePageUsageLogDto](docs/ResponsePageUsageLogDto.md)
 - [RollingDateFunction](docs/RollingDateFunction.md)
 - [Row](docs/Row.md)
 - [RowItem](docs/RowItem.md)
 - [SegmentCompatibility](docs/SegmentCompatibility.md)
 - [Share](docs/Share.md)
 - [SharedComponent](docs/SharedComponent.md)
 - [Sort](docs/Sort.md)
 - [SuiteCollectionItem](docs/SuiteCollectionItem.md)
 - [Tag](docs/Tag.md)
 - [TaggedComponent](docs/TaggedComponent.md)
 - [UnhashReportData](docs/UnhashReportData.md)
 - [UsageLogDto](docs/UsageLogDto.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


