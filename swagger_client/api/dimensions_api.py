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


class DimensionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dimensions_get_dimension(self, dimension_id, rsid, **kwargs):  # noqa: E501
        """Returns a dimension for the given report suite  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dimensions_get_dimension(dimension_id, rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dimension_id: The dimension ID. For example a valid id is a value like 'evar1' (required)
        :param str rsid: The report suite ID. (required)
        :param str locale: The locale to use for returning system named dimensions.
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: AnalyticsDimension
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dimensions_get_dimension_with_http_info(dimension_id, rsid, **kwargs)  # noqa: E501
        else:
            (data) = self.dimensions_get_dimension_with_http_info(dimension_id, rsid, **kwargs)  # noqa: E501
            return data

    def dimensions_get_dimension_with_http_info(self, dimension_id, rsid, **kwargs):  # noqa: E501
        """Returns a dimension for the given report suite  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dimensions_get_dimension_with_http_info(dimension_id, rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dimension_id: The dimension ID. For example a valid id is a value like 'evar1' (required)
        :param str rsid: The report suite ID. (required)
        :param str locale: The locale to use for returning system named dimensions.
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: AnalyticsDimension
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dimension_id', 'rsid', 'locale', 'expansion']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dimensions_get_dimension" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dimension_id' is set
        if ('dimension_id' not in params or
                params['dimension_id'] is None):
            raise ValueError("Missing the required parameter `dimension_id` when calling `dimensions_get_dimension`")  # noqa: E501
        # verify the required parameter 'rsid' is set
        if ('rsid' not in params or
                params['rsid'] is None):
            raise ValueError("Missing the required parameter `rsid` when calling `dimensions_get_dimension`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dimension_id' in params:
            path_params['dimensionId'] = params['dimension_id']  # noqa: E501

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
            '/dimensions/{dimensionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsDimension',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dimensions_get_dimensions(self, rsid, **kwargs):  # noqa: E501
        """Returns a list of dimensions for a given report suite.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dimensions_get_dimensions(rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rsid: A Report Suite ID (required)
        :param str locale: Locale
        :param bool segmentable: Only include dimensions that are valid within a segment.
        :param bool reportable: Only include dimensions that are valid within a report.
        :param bool classifiable: Only include classifiable dimensions.
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: list[AnalyticsDimension]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dimensions_get_dimensions_with_http_info(rsid, **kwargs)  # noqa: E501
        else:
            (data) = self.dimensions_get_dimensions_with_http_info(rsid, **kwargs)  # noqa: E501
            return data

    def dimensions_get_dimensions_with_http_info(self, rsid, **kwargs):  # noqa: E501
        """Returns a list of dimensions for a given report suite.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dimensions_get_dimensions_with_http_info(rsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rsid: A Report Suite ID (required)
        :param str locale: Locale
        :param bool segmentable: Only include dimensions that are valid within a segment.
        :param bool reportable: Only include dimensions that are valid within a report.
        :param bool classifiable: Only include classifiable dimensions.
        :param list[str] expansion: Add extra metadata to items (comma-delimited list)
        :return: list[AnalyticsDimension]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rsid', 'locale', 'segmentable', 'reportable', 'classifiable', 'expansion']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dimensions_get_dimensions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rsid' is set
        if ('rsid' not in params or
                params['rsid'] is None):
            raise ValueError("Missing the required parameter `rsid` when calling `dimensions_get_dimensions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rsid' in params:
            query_params.append(('rsid', params['rsid']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'segmentable' in params:
            query_params.append(('segmentable', params['segmentable']))  # noqa: E501
        if 'reportable' in params:
            query_params.append(('reportable', params['reportable']))  # noqa: E501
        if 'classifiable' in params:
            query_params.append(('classifiable', params['classifiable']))  # noqa: E501
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
            '/dimensions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AnalyticsDimension]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)