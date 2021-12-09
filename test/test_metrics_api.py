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
from swagger_client.api.metrics_api import MetricsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metric(self):
        """Test case for get_metric

        Returns a metric for the given report suite  # noqa: E501
        """
        pass

    def test_get_metrics(self):
        """Test case for get_metrics

        Returns a list of metrics for the given report suite  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
