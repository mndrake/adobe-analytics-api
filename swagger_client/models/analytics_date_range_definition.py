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

class AnalyticsDateRangeDefinition(object):
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
        'start': 'list[RollingDateFunction]',
        'end': 'list[RollingDateFunction]',
        'calendar_type': 'CalendarType',
        'version': 'str'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'calendar_type': 'calendarType',
        'version': 'version'
    }

    def __init__(self, start=None, end=None, calendar_type=None, version=None):  # noqa: E501
        """AnalyticsDateRangeDefinition - a model defined in Swagger"""  # noqa: E501
        self._start = None
        self._end = None
        self._calendar_type = None
        self._version = None
        self.discriminator = None
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if version is not None:
            self.version = version

    @property
    def start(self):
        """Gets the start of this AnalyticsDateRangeDefinition.  # noqa: E501


        :return: The start of this AnalyticsDateRangeDefinition.  # noqa: E501
        :rtype: list[RollingDateFunction]
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AnalyticsDateRangeDefinition.


        :param start: The start of this AnalyticsDateRangeDefinition.  # noqa: E501
        :type: list[RollingDateFunction]
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this AnalyticsDateRangeDefinition.  # noqa: E501


        :return: The end of this AnalyticsDateRangeDefinition.  # noqa: E501
        :rtype: list[RollingDateFunction]
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this AnalyticsDateRangeDefinition.


        :param end: The end of this AnalyticsDateRangeDefinition.  # noqa: E501
        :type: list[RollingDateFunction]
        """

        self._end = end

    @property
    def calendar_type(self):
        """Gets the calendar_type of this AnalyticsDateRangeDefinition.  # noqa: E501


        :return: The calendar_type of this AnalyticsDateRangeDefinition.  # noqa: E501
        :rtype: CalendarType
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this AnalyticsDateRangeDefinition.


        :param calendar_type: The calendar_type of this AnalyticsDateRangeDefinition.  # noqa: E501
        :type: CalendarType
        """

        self._calendar_type = calendar_type

    @property
    def version(self):
        """Gets the version of this AnalyticsDateRangeDefinition.  # noqa: E501


        :return: The version of this AnalyticsDateRangeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnalyticsDateRangeDefinition.


        :param version: The version of this AnalyticsDateRangeDefinition.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(AnalyticsDateRangeDefinition, dict):
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
        if not isinstance(other, AnalyticsDateRangeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other