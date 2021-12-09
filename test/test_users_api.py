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
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_all(self):
        """Test case for find_all

        Returns a list of users for the current user's login company  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Get the current user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
