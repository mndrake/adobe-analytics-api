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


class MetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_metric(self, id, rsid, **kwargs):  # noqa: E501
        """Returns a metric for the given report suite  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metric(id, rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the metric for which to retrieve info. Note ids are values like pageviews, not metrics/pageviews (required)
        :param str rsid: ID of desired report suite ie. myrsid (required)
        :param str locale: Locale that system named metrics should be returned in
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: AnalyticsMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metric_with_http_info(id, rsid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metric_with_http_info(id, rsid, **kwargs)  # noqa: E501
            return data

    def get_metric_with_http_info(self, id, rsid, **kwargs):  # noqa: E501
        """Returns a metric for the given report suite  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metric_with_http_info(id, rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the metric for which to retrieve info. Note ids are values like pageviews, not metrics/pageviews (required)
        :param str rsid: ID of desired report suite ie. myrsid (required)
        :param str locale: Locale that system named metrics should be returned in
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: AnalyticsMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'rsid', 'locale', 'expansion']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metric" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_metric`")  # noqa: E501
        # verify the required parameter 'rsid' is set
        if ('rsid' not in params or
                params['rsid'] is None):
            raise ValueError("Missing the required parameter `rsid` when calling `get_metric`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'rsid' in params:
            query_params.append(('rsid', params['rsid']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'expansion' in params:
            query_params.append(('expansion', params['expansion']))  # noqa: E501
            collection_formats['expansion'] = 'csv'  # noqa: E501

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
            '/metrics/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsMetric',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_metrics(self, rsid, **kwargs):  # noqa: E501
        """Returns a list of metrics for the given report suite  # noqa: E501

        This returns the metrics list primarily for the Analytics product. The platform identity API Returns a list of all possible metrics for the supported systems.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics(rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rsid: ID of desired report suite ie. myrsid (required)
        :param str locale: Locale that system named metrics should be returned in
        :param bool segmentable: Filter the metrics by if they are valid in a segment.
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: AnalyticsMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metrics_with_http_info(rsid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metrics_with_http_info(rsid, **kwargs)  # noqa: E501
            return data

    def get_metrics_with_http_info(self, rsid, **kwargs):  # noqa: E501
        """Returns a list of metrics for the given report suite  # noqa: E501

        This returns the metrics list primarily for the Analytics product. The platform identity API Returns a list of all possible metrics for the supported systems.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_with_http_info(rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rsid: ID of desired report suite ie. myrsid (required)
        :param str locale: Locale that system named metrics should be returned in
        :param bool segmentable: Filter the metrics by if they are valid in a segment.
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: AnalyticsMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rsid', 'locale', 'segmentable', 'expansion']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rsid' is set
        if ('rsid' not in params or
                params['rsid'] is None):
            raise ValueError("Missing the required parameter `rsid` when calling `get_metrics`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rsid' in params:
            query_params.append(('rsid', params['rsid']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'segmentable' in params:
            query_params.append(('segmentable', params['segmentable']))  # noqa: E501
        if 'expansion' in params:
            query_params.append(('expansion', params['expansion']))  # noqa: E501
            collection_formats['expansion'] = 'csv'  # noqa: E501

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
            '/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsMetric',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)