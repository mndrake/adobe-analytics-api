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

class Row(object):
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
        'item_id': 'str',
        'value': 'str',
        'row_id': 'str',
        'data': 'list[float]',
        'data_expected': 'list[float]',
        'data_upper_bound': 'list[float]',
        'data_lower_bound': 'list[float]',
        'data_anomaly_detected': 'list[bool]',
        'percent_change': 'list[float]',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'item_id': 'itemId',
        'value': 'value',
        'row_id': 'rowId',
        'data': 'data',
        'data_expected': 'dataExpected',
        'data_upper_bound': 'dataUpperBound',
        'data_lower_bound': 'dataLowerBound',
        'data_anomaly_detected': 'dataAnomalyDetected',
        'percent_change': 'percentChange',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, item_id=None, value=None, row_id=None, data=None, data_expected=None, data_upper_bound=None, data_lower_bound=None, data_anomaly_detected=None, percent_change=None, latitude=None, longitude=None):  # noqa: E501
        """Row - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._value = None
        self._row_id = None
        self._data = None
        self._data_expected = None
        self._data_upper_bound = None
        self._data_lower_bound = None
        self._data_anomaly_detected = None
        self._percent_change = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if value is not None:
            self.value = value
        if row_id is not None:
            self.row_id = row_id
        if data is not None:
            self.data = data
        if data_expected is not None:
            self.data_expected = data_expected
        if data_upper_bound is not None:
            self.data_upper_bound = data_upper_bound
        if data_lower_bound is not None:
            self.data_lower_bound = data_lower_bound
        if data_anomaly_detected is not None:
            self.data_anomaly_detected = data_anomaly_detected
        if percent_change is not None:
            self.percent_change = percent_change
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def item_id(self):
        """Gets the item_id of this Row.  # noqa: E501


        :return: The item_id of this Row.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Row.


        :param item_id: The item_id of this Row.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def value(self):
        """Gets the value of this Row.  # noqa: E501


        :return: The value of this Row.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Row.


        :param value: The value of this Row.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def row_id(self):
        """Gets the row_id of this Row.  # noqa: E501


        :return: The row_id of this Row.  # noqa: E501
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        """Sets the row_id of this Row.


        :param row_id: The row_id of this Row.  # noqa: E501
        :type: str
        """

        self._row_id = row_id

    @property
    def data(self):
        """Gets the data of this Row.  # noqa: E501


        :return: The data of this Row.  # noqa: E501
        :rtype: list[float]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Row.


        :param data: The data of this Row.  # noqa: E501
        :type: list[float]
        """

        self._data = data

    @property
    def data_expected(self):
        """Gets the data_expected of this Row.  # noqa: E501


        :return: The data_expected of this Row.  # noqa: E501
        :rtype: list[float]
        """
        return self._data_expected

    @data_expected.setter
    def data_expected(self, data_expected):
        """Sets the data_expected of this Row.


        :param data_expected: The data_expected of this Row.  # noqa: E501
        :type: list[float]
        """

        self._data_expected = data_expected

    @property
    def data_upper_bound(self):
        """Gets the data_upper_bound of this Row.  # noqa: E501


        :return: The data_upper_bound of this Row.  # noqa: E501
        :rtype: list[float]
        """
        return self._data_upper_bound

    @data_upper_bound.setter
    def data_upper_bound(self, data_upper_bound):
        """Sets the data_upper_bound of this Row.


        :param data_upper_bound: The data_upper_bound of this Row.  # noqa: E501
        :type: list[float]
        """

        self._data_upper_bound = data_upper_bound

    @property
    def data_lower_bound(self):
        """Gets the data_lower_bound of this Row.  # noqa: E501


        :return: The data_lower_bound of this Row.  # noqa: E501
        :rtype: list[float]
        """
        return self._data_lower_bound

    @data_lower_bound.setter
    def data_lower_bound(self, data_lower_bound):
        """Sets the data_lower_bound of this Row.


        :param data_lower_bound: The data_lower_bound of this Row.  # noqa: E501
        :type: list[float]
        """

        self._data_lower_bound = data_lower_bound

    @property
    def data_anomaly_detected(self):
        """Gets the data_anomaly_detected of this Row.  # noqa: E501


        :return: The data_anomaly_detected of this Row.  # noqa: E501
        :rtype: list[bool]
        """
        return self._data_anomaly_detected

    @data_anomaly_detected.setter
    def data_anomaly_detected(self, data_anomaly_detected):
        """Sets the data_anomaly_detected of this Row.


        :param data_anomaly_detected: The data_anomaly_detected of this Row.  # noqa: E501
        :type: list[bool]
        """

        self._data_anomaly_detected = data_anomaly_detected

    @property
    def percent_change(self):
        """Gets the percent_change of this Row.  # noqa: E501


        :return: The percent_change of this Row.  # noqa: E501
        :rtype: list[float]
        """
        return self._percent_change

    @percent_change.setter
    def percent_change(self, percent_change):
        """Sets the percent_change of this Row.


        :param percent_change: The percent_change of this Row.  # noqa: E501
        :type: list[float]
        """

        self._percent_change = percent_change

    @property
    def latitude(self):
        """Gets the latitude of this Row.  # noqa: E501


        :return: The latitude of this Row.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Row.


        :param latitude: The latitude of this Row.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Row.  # noqa: E501


        :return: The longitude of this Row.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Row.


        :param longitude: The longitude of this Row.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if issubclass(Row, dict):
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
        if not isinstance(other, Row):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
