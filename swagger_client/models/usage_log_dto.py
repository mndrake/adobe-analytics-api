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

class UsageLogDto(object):
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
        'date_created': 'datetime',
        'event_description': 'str',
        'ip_address': 'str',
        'rsid': 'str',
        'event_type': 'str',
        'login': 'str'
    }

    attribute_map = {
        'date_created': 'dateCreated',
        'event_description': 'eventDescription',
        'ip_address': 'ipAddress',
        'rsid': 'rsid',
        'event_type': 'eventType',
        'login': 'login'
    }

    def __init__(self, date_created=None, event_description=None, ip_address=None, rsid=None, event_type=None, login=None):  # noqa: E501
        """UsageLogDto - a model defined in Swagger"""  # noqa: E501
        self._date_created = None
        self._event_description = None
        self._ip_address = None
        self._rsid = None
        self._event_type = None
        self._login = None
        self.discriminator = None
        if date_created is not None:
            self.date_created = date_created
        if event_description is not None:
            self.event_description = event_description
        if ip_address is not None:
            self.ip_address = ip_address
        if rsid is not None:
            self.rsid = rsid
        if event_type is not None:
            self.event_type = event_type
        if login is not None:
            self.login = login

    @property
    def date_created(self):
        """Gets the date_created of this UsageLogDto.  # noqa: E501


        :return: The date_created of this UsageLogDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this UsageLogDto.


        :param date_created: The date_created of this UsageLogDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def event_description(self):
        """Gets the event_description of this UsageLogDto.  # noqa: E501


        :return: The event_description of this UsageLogDto.  # noqa: E501
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """Sets the event_description of this UsageLogDto.


        :param event_description: The event_description of this UsageLogDto.  # noqa: E501
        :type: str
        """

        self._event_description = event_description

    @property
    def ip_address(self):
        """Gets the ip_address of this UsageLogDto.  # noqa: E501


        :return: The ip_address of this UsageLogDto.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this UsageLogDto.


        :param ip_address: The ip_address of this UsageLogDto.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def rsid(self):
        """Gets the rsid of this UsageLogDto.  # noqa: E501


        :return: The rsid of this UsageLogDto.  # noqa: E501
        :rtype: str
        """
        return self._rsid

    @rsid.setter
    def rsid(self, rsid):
        """Sets the rsid of this UsageLogDto.


        :param rsid: The rsid of this UsageLogDto.  # noqa: E501
        :type: str
        """

        self._rsid = rsid

    @property
    def event_type(self):
        """Gets the event_type of this UsageLogDto.  # noqa: E501


        :return: The event_type of this UsageLogDto.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this UsageLogDto.


        :param event_type: The event_type of this UsageLogDto.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def login(self):
        """Gets the login of this UsageLogDto.  # noqa: E501


        :return: The login of this UsageLogDto.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UsageLogDto.


        :param login: The login of this UsageLogDto.  # noqa: E501
        :type: str
        """

        self._login = login

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
        if issubclass(UsageLogDto, dict):
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
        if not isinstance(other, UsageLogDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
