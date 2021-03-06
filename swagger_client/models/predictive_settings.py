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

class PredictiveSettings(object):
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
        'training_periods': 'int',
        'high_anomalies': 'bool',
        'low_anomalies': 'bool'
    }

    attribute_map = {
        'training_periods': 'trainingPeriods',
        'high_anomalies': 'highAnomalies',
        'low_anomalies': 'lowAnomalies'
    }

    def __init__(self, training_periods=None, high_anomalies=None, low_anomalies=None):  # noqa: E501
        """PredictiveSettings - a model defined in Swagger"""  # noqa: E501
        self._training_periods = None
        self._high_anomalies = None
        self._low_anomalies = None
        self.discriminator = None
        if training_periods is not None:
            self.training_periods = training_periods
        if high_anomalies is not None:
            self.high_anomalies = high_anomalies
        if low_anomalies is not None:
            self.low_anomalies = low_anomalies

    @property
    def training_periods(self):
        """Gets the training_periods of this PredictiveSettings.  # noqa: E501


        :return: The training_periods of this PredictiveSettings.  # noqa: E501
        :rtype: int
        """
        return self._training_periods

    @training_periods.setter
    def training_periods(self, training_periods):
        """Sets the training_periods of this PredictiveSettings.


        :param training_periods: The training_periods of this PredictiveSettings.  # noqa: E501
        :type: int
        """

        self._training_periods = training_periods

    @property
    def high_anomalies(self):
        """Gets the high_anomalies of this PredictiveSettings.  # noqa: E501


        :return: The high_anomalies of this PredictiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._high_anomalies

    @high_anomalies.setter
    def high_anomalies(self, high_anomalies):
        """Sets the high_anomalies of this PredictiveSettings.


        :param high_anomalies: The high_anomalies of this PredictiveSettings.  # noqa: E501
        :type: bool
        """

        self._high_anomalies = high_anomalies

    @property
    def low_anomalies(self):
        """Gets the low_anomalies of this PredictiveSettings.  # noqa: E501


        :return: The low_anomalies of this PredictiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._low_anomalies

    @low_anomalies.setter
    def low_anomalies(self, low_anomalies):
        """Sets the low_anomalies of this PredictiveSettings.


        :param low_anomalies: The low_anomalies of this PredictiveSettings.  # noqa: E501
        :type: bool
        """

        self._low_anomalies = low_anomalies

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
        if issubclass(PredictiveSettings, dict):
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
        if not isinstance(other, PredictiveSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
