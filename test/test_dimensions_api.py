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
from swagger_client.api.dimensions_api import DimensionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDimensionsApi(unittest.TestCase):
    """DimensionsApi unit test stubs"""

    def setUp(self):
        self.api = DimensionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dimensions_get_dimension(self):
        """Test case for dimensions_get_dimension

        Returns a dimension for the given report suite  # noqa: E501
        """
        pass

    def test_dimensions_get_dimensions(self):
        """Test case for dimensions_get_dimensions

        Returns a list of dimensions for a given report suite.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
