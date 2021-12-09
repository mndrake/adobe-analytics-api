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

class RollingDateFunction(object):
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
        'function': 'str',
        'granularity': 'str',
        'offset': 'int',
        'dow': 'str',
        '_date': 'str'
    }

    attribute_map = {
        'function': 'function',
        'granularity': 'granularity',
        'offset': 'offset',
        'dow': 'dow',
        '_date': 'date'
    }

    def __init__(self, function=None, granularity=None, offset=None, dow=None, _date=None):  # noqa: E501
        """RollingDateFunction - a model defined in Swagger"""  # noqa: E501
        self._function = None
        self._granularity = None
        self._offset = None
        self._dow = None
        self.__date = None
        self.discriminator = None
        if function is not None:
            self.function = function
        if granularity is not None:
            self.granularity = granularity
        if offset is not None:
            self.offset = offset
        if dow is not None:
            self.dow = dow
        if _date is not None:
            self._date = _date

    @property
    def function(self):
        """Gets the function of this RollingDateFunction.  # noqa: E501


        :return: The function of this RollingDateFunction.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this RollingDateFunction.


        :param function: The function of this RollingDateFunction.  # noqa: E501
        :type: str
        """

        self._function = function

    @property
    def granularity(self):
        """Gets the granularity of this RollingDateFunction.  # noqa: E501


        :return: The granularity of this RollingDateFunction.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this RollingDateFunction.


        :param granularity: The granularity of this RollingDateFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["year", "quarter", "month", "week", "day", "hour", "minute"]  # noqa: E501
        if granularity not in allowed_values:
            raise ValueError(
                "Invalid value for `granularity` ({0}), must be one of {1}"  # noqa: E501
                .format(granularity, allowed_values)
            )

        self._granularity = granularity

    @property
    def offset(self):
        """Gets the offset of this RollingDateFunction.  # noqa: E501


        :return: The offset of this RollingDateFunction.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this RollingDateFunction.


        :param offset: The offset of this RollingDateFunction.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def dow(self):
        """Gets the dow of this RollingDateFunction.  # noqa: E501


        :return: The dow of this RollingDateFunction.  # noqa: E501
        :rtype: str
        """
        return self._dow

    @dow.setter
    def dow(self, dow):
        """Sets the dow of this RollingDateFunction.


        :param dow: The dow of this RollingDateFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]  # noqa: E501
        if dow not in allowed_values:
            raise ValueError(
                "Invalid value for `dow` ({0}), must be one of {1}"  # noqa: E501
                .format(dow, allowed_values)
            )

        self._dow = dow

    @property
    def _date(self):
        """Gets the _date of this RollingDateFunction.  # noqa: E501


        :return: The _date of this RollingDateFunction.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this RollingDateFunction.


        :param _date: The _date of this RollingDateFunction.  # noqa: E501
        :type: str
        """

        self.__date = _date

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
        if issubclass(RollingDateFunction, dict):
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
        if not isinstance(other, RollingDateFunction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other