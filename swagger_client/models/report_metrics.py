# coding: utf-8

"""
    Adobe Analytics APIs

    The endpoints described here are routed through Adobe.io.          In order to use these endpoints you must create an oAuth client that is          subscribed to access the Adobe Analytics Reporting API.  # noqa: E501

    OpenAPI spec version: v1 - Build: 2019-10-03_20:32:29.323
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReportMetrics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metric_filters': 'list[ReportFilter]',
        'metrics': 'list[ReportMetric]'
    }

    attribute_map = {
        'metric_filters': 'metricFilters',
        'metrics': 'metrics'
    }

    def __init__(self, metric_filters=None, metrics=None):  # noqa: E501
        """ReportMetrics - a model defined in Swagger"""  # noqa: E501
        self._metric_filters = None
        self._metrics = None
        self.discriminator = None
        if metric_filters is not None:
            self.metric_filters = metric_filters
        if metrics is not None:
            self.metrics = metrics

    @property
    def metric_filters(self):
        """Gets the metric_filters of this ReportMetrics.  # noqa: E501


        :return: The metric_filters of this ReportMetrics.  # noqa: E501
        :rtype: list[ReportFilter]
        """
        return self._metric_filters

    @metric_filters.setter
    def metric_filters(self, metric_filters):
        """Sets the metric_filters of this ReportMetrics.


        :param metric_filters: The metric_filters of this ReportMetrics.  # noqa: E501
        :type: list[ReportFilter]
        """

        self._metric_filters = metric_filters

    @property
    def metrics(self):
        """Gets the metrics of this ReportMetrics.  # noqa: E501


        :return: The metrics of this ReportMetrics.  # noqa: E501
        :rtype: list[ReportMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ReportMetrics.


        :param metrics: The metrics of this ReportMetrics.  # noqa: E501
        :type: list[ReportMetric]
        """

        self._metrics = metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ReportMetrics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
