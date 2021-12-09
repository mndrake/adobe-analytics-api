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


class ProjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def projects_create_project(self, **kwargs):  # noqa: E501
        """Creates a single project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_create_project(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnalyticsProject body: JSON-formatted Object containing project keys/value pairs to be updated.
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str locale: Locale
        :return: AnalyticsProject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_create_project_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_create_project_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_create_project_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a single project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_create_project_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnalyticsProject body: JSON-formatted Object containing project keys/value pairs to be updated.
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str locale: Locale
        :return: AnalyticsProject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'expansion', 'locale']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_create_project" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expansion' in params:
            query_params.append(('expansion', params['expansion']))  # noqa: E501
            collection_formats['expansion'] = 'csv'  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsProject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_delete_project(self, project_id, **kwargs):  # noqa: E501
        """deletes a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_delete_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The Project id for which to retrieve information (required)
        :param str locale: Locale
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_delete_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_delete_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_delete_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """deletes a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_delete_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The Project id for which to retrieve information (required)
        :param str locale: Locale
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'locale']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_delete_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_delete_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501

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
            '/projects/{projectId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project(self, project_id, **kwargs):  # noqa: E501
        """Retrieves configuration for a Project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The Project id for which to retrieve information (required)
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str locale: Locale
        :return: AnalyticsProject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_get_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Retrieves configuration for a Project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The Project id for which to retrieve information (required)
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str locale: Locale
        :return: AnalyticsProject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'expansion', 'locale']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'expansion' in params:
            query_params.append(('expansion', params['expansion']))  # noqa: E501
            collection_formats['expansion'] = 'csv'  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501

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
            '/projects/{projectId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsProject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_projects(self, **kwargs):  # noqa: E501
        """Returns a list of projects for the user  # noqa: E501

        This Returns the projects list primarily for the Analytics product.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] include_type: Include additional projects not owned by user. The \"all\" option takes precedence over \"shared\". If neither guided, or project is included, both types are returned
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str filter_by_ids: Filter list to only include projects in the specified list (comma-delimited list of IDs)
        :param str locale: Locale
        :param str pagination: return paginated results
        :param int owner_id: Filter list to only include projects owned by the specified loginId
        :param int limit: Number of results per page
        :param int page: Page number (base 0 - first page is \"0\")
        :return: list[AnalyticsProject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_projects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_projects_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_get_projects_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of projects for the user  # noqa: E501

        This Returns the projects list primarily for the Analytics product.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] include_type: Include additional projects not owned by user. The \"all\" option takes precedence over \"shared\". If neither guided, or project is included, both types are returned
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str filter_by_ids: Filter list to only include projects in the specified list (comma-delimited list of IDs)
        :param str locale: Locale
        :param str pagination: return paginated results
        :param int owner_id: Filter list to only include projects owned by the specified loginId
        :param int limit: Number of results per page
        :param int page: Page number (base 0 - first page is \"0\")
        :return: list[AnalyticsProject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_type', 'expansion', 'filter_by_ids', 'locale', 'pagination', 'owner_id', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_projects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_type' in params:
            query_params.append(('includeType', params['include_type']))  # noqa: E501
            collection_formats['includeType'] = 'csv'  # noqa: E501
        if 'expansion' in params:
            query_params.append(('expansion', params['expansion']))  # noqa: E501
            collection_formats['expansion'] = 'csv'  # noqa: E501
        if 'filter_by_ids' in params:
            query_params.append(('filterByIds', params['filter_by_ids']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'pagination' in params:
            query_params.append(('pagination', params['pagination']))  # noqa: E501
        if 'owner_id' in params:
            query_params.append(('ownerId', params['owner_id']))  # noqa: E501
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
            '/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AnalyticsProject]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_update_project(self, project_id, **kwargs):  # noqa: E501
        """Updates configuration for a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_update_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The Project id for which to retrieve information (required)
        :param AnalyticsProject body: JSON-formatted Object containing project keys/value pairs to be updated.
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str locale: Locale
        :return: AnalyticsProject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_update_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_update_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_update_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Updates configuration for a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_update_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The Project id for which to retrieve information (required)
        :param AnalyticsProject body: JSON-formatted Object containing project keys/value pairs to be updated.
        :param list[str] expansion: Comma-delimited list of additional project metadata fields to include on response.
        :param str locale: Locale
        :return: AnalyticsProject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'body', 'expansion', 'locale']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_update_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_update_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'expansion' in params:
            query_params.append(('expansion', params['expansion']))  # noqa: E501
            collection_formats['expansion'] = 'csv'  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsProject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_validate_project(self, body, **kwargs):  # noqa: E501
        """Validates a Project definition  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_validate_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectsValidateBody body: JSON-formatted Object containing key/value pairs for Project validation. (required)
        :param str locale: Locale
        :return: ProjectCompatibility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_validate_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_validate_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def projects_validate_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Validates a Project definition  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_validate_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectsValidateBody body: JSON-formatted Object containing key/value pairs for Project validation. (required)
        :param str locale: Locale
        :return: ProjectCompatibility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'locale']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_validate_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `projects_validate_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501

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
            '/projects/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectCompatibility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)