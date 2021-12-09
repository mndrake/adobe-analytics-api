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

class ReportRows(object):
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
        'row_filters': 'list[ReportFilter]',
        'rows': 'list[ReportRow]'
    }

    attribute_map = {
        'row_filters': 'rowFilters',
        'rows': 'rows'
    }

    def __init__(self, row_filters=None, rows=None):  # noqa: E501
        """ReportRows - a model defined in Swagger"""  # noqa: E501
        self._row_filters = None
        self._rows = None
        self.discriminator = None
        if row_filters is not None:
            self.row_filters = row_filters
        if rows is not None:
            self.rows = rows

    @property
    def row_filters(self):
        """Gets the row_filters of this ReportRows.  # noqa: E501


        :return: The row_filters of this ReportRows.  # noqa: E501
        :rtype: list[ReportFilter]
        """
        return self._row_filters

    @row_filters.setter
    def row_filters(self, row_filters):
        """Sets the row_filters of this ReportRows.


        :param row_filters: The row_filters of this ReportRows.  # noqa: E501
        :type: list[ReportFilter]
        """

        self._row_filters = row_filters

    @property
    def rows(self):
        """Gets the rows of this ReportRows.  # noqa: E501


        :return: The rows of this ReportRows.  # noqa: E501
        :rtype: list[ReportRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ReportRows.


        :param rows: The rows of this ReportRows.  # noqa: E501
        :type: list[ReportRow]
        """

        self._rows = rows

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
        if issubclass(ReportRows, dict):
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
        if not isinstance(other, ReportRows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other