# coding: utf-8

"""
    Adobe Analytics APIs

    The endpoints described here are routed through Adobe.io.          In order to use these endpoints you must create an oAuth client that is          subscribed to access the Adobe Analytics Reporting API.  # noqa: E501

    OpenAPI spec version: v1 - Build: 2019-10-03_20:32:29.323
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.projects_api import ProjectsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_create_project(self):
        """Test case for projects_create_project

        Creates a single project.  # noqa: E501
        """
        pass

    def test_projects_delete_project(self):
        """Test case for projects_delete_project

        deletes a project.  # noqa: E501
        """
        pass

    def test_projects_get_project(self):
        """Test case for projects_get_project

        Retrieves configuration for a Project.  # noqa: E501
        """
        pass

    def test_projects_get_projects(self):
        """Test case for projects_get_projects

        Returns a list of projects for the user  # noqa: E501
        """
        pass

    def test_projects_update_project(self):
        """Test case for projects_update_project

        Updates configuration for a project.  # noqa: E501
        """
        pass

    def test_projects_validate_project(self):
        """Test case for projects_validate_project

        Validates a Project definition  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
