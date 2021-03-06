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
from swagger_client.api.usagelogs_api import UsagelogsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsagelogsApi(unittest.TestCase):
    """UsagelogsApi unit test stubs"""

    def setUp(self):
        self.api = UsagelogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_usage_access_logs(self):
        """Test case for get_usage_access_logs

        Retrieves usage and access logs for the search criteria provided.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
