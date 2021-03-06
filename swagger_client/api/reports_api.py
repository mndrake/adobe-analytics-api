# coding: utf-8

"""
    Adobe Analytics APIs

    The endpoints described here are routed through Adobe.io.          In order to use these endpoints you must create an oAuth client that is          subscribed to access the Adobe Analytics Reporting API.  # noqa: E501

    OpenAPI spec version: v1 - Build: 2019-10-03_20:32:29.323
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ReportsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def run_report(self, **kwargs):  # noqa: E501
        """Runs a report for the request in the post body  # noqa: E501

        See the [Reporting User Guide](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/reporting-guide.md) for details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_report(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RankedRequest body:
        :return: RankedReportData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.run_report_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.run_report_with_http_info(**kwargs)  # noqa: E501
            return data

    def run_report_with_http_info(self, **kwargs):  # noqa: E501
        """Runs a report for the request in the post body  # noqa: E501

        See the [Reporting User Guide](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/reporting-guide.md) for details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_report_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RankedRequest body:
        :return: RankedReportData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_report" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/reports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RankedReportData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def run_top_item_report(self, rsid, dimension, **kwargs):  # noqa: E501
        """Runs a top items report for the request in the post body  # noqa: E501

        Get the top X items (based on paging restriction) for the specified dimension and rsid. Defaults to last 90 days.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_top_item_report(rsid, dimension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rsid: ID of desired report suite ie. myrsid (required)
        :param str dimension: Dimension to run the report against. Example: 'variables/page' (required)
        :param str locale: Locale that system named metrics should be returned in
        :param str date_range: Format: YYYY-MM-DD/YYYY-MM-DD
        :param str search_clause: General search string; wrap with single quotes. Example: 'PageABC'
        :param str start_date: Format: YYYY-MM-DD
        :param str end_date: Format: YYYY-MM-DD
        :param str search_and: Search terms that will be AND-ed together. Space delimited.
        :param str search_or: Search terms that will be OR-ed together. Space delimited.
        :param str search_not: Search terms that will be treated as NOT including. Space delimited.
        :param str search_phrase: A full search phrase that will be searched for.
        :param str search_phrase: A full search phrase that will be searched for.
        :param bool lookup_none_values: Controls None values to be included
        :param int limit: Number of results per page
        :param int page: Page number (base 0 - first page is \"0\")
        :return: UnhashReportData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.run_top_item_report_with_http_info(rsid, dimension, **kwargs)  # noqa: E501
        else:
            (data) = self.run_top_item_report_with_http_info(rsid, dimension, **kwargs)  # noqa: E501
            return data

    def run_top_item_report_with_http_info(self, rsid, dimension, **kwargs):  # noqa: E501
        """Runs a top items report for the request in the post body  # noqa: E501

        Get the top X items (based on paging restriction) for the specified dimension and rsid. Defaults to last 90 days.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_top_item_report_with_http_info(rsid, dimension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rsid: ID of desired report suite ie. myrsid (required)
        :param str dimension: Dimension to run the report against. Example: 'variables/page' (required)
        :param str locale: Locale that system named metrics should be returned in
        :param str date_range: Format: YYYY-MM-DD/YYYY-MM-DD
        :param str search_clause: General search string; wrap with single quotes. Example: 'PageABC'
        :param str start_date: Format: YYYY-MM-DD
        :param str end_date: Format: YYYY-MM-DD
        :param str search_and: Search terms that will be AND-ed together. Space delimited.
        :param str search_or: Search terms that will be OR-ed together. Space delimited.
        :param str search_not: Search terms that will be treated as NOT including. Space delimited.
        :param str search_phrase: A full search phrase that will be searched for.
        :param str search_phrase: A full search phrase that will be searched for.
        :param bool lookup_none_values: Controls None values to be included
        :param int limit: Number of results per page
        :param int page: Page number (base 0 - first page is \"0\")
        :return: UnhashReportData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rsid', 'dimension', 'locale', 'date_range', 'search_clause', 'start_date', 'end_date', 'search_and', 'search_or', 'search_not', 'search_phrase', 'search_phrase', 'lookup_none_values', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_top_item_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rsid' is set
        if ('rsid' not in params or
                params['rsid'] is None):
            raise ValueError("Missing the required parameter `rsid` when calling `run_top_item_report`")  # noqa: E501
        # verify the required parameter 'dimension' is set
        if ('dimension' not in params or
                params['dimension'] is None):
            raise ValueError("Missing the required parameter `dimension` when calling `run_top_item_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rsid' in params:
            query_params.append(('rsid', params['rsid']))  # noqa: E501
        if 'dimension' in params:
            query_params.append(('dimension', params['dimension']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'date_range' in params:
            query_params.append(('dateRange', params['date_range']))  # noqa: E501
        if 'search_clause' in params:
            query_params.append(('search-clause', params['search_clause']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'search_and' in params:
            query_params.append(('searchAnd', params['search_and']))  # noqa: E501
        if 'search_or' in params:
            query_params.append(('searchOr', params['search_or']))  # noqa: E501
        if 'search_not' in params:
            query_params.append(('searchNot', params['search_not']))  # noqa: E501
        if 'search_phrase' in params:
            query_params.append(('searchPhrase', params['search_phrase']))  # noqa: E501
        if 'search_phrase' in params:
            query_params.append(('searchPhrase', params['search_phrase']))  # noqa: E501
        if 'lookup_none_values' in params:
            query_params.append(('lookupNoneValues', params['lookup_none_values']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/reports/topItems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UnhashReportData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
