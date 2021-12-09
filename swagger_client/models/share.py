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

class Share(object):
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
        'id': 'int',
        'share_to_id': 'int',
        'share_to_type': 'str',
        'share_to_display_name': 'str',
        'component_type': 'str',
        'component_id': 'str',
        'access_level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'share_to_id': 'shareToId',
        'share_to_type': 'shareToType',
        'share_to_display_name': 'shareToDisplayName',
        'component_type': 'componentType',
        'component_id': 'componentId',
        'access_level': 'accessLevel'
    }

    def __init__(self, id=None, share_to_id=None, share_to_type=None, share_to_display_name=None, component_type=None, component_id=None, access_level=None):  # noqa: E501
        """Share - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._share_to_id = None
        self._share_to_type = None
        self._share_to_display_name = None
        self._component_type = None
        self._component_id = None
        self._access_level = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if share_to_id is not None:
            self.share_to_id = share_to_id
        if share_to_type is not None:
            self.share_to_type = share_to_type
        if share_to_display_name is not None:
            self.share_to_display_name = share_to_display_name
        if component_type is not None:
            self.component_type = component_type
        if component_id is not None:
            self.component_id = component_id
        if access_level is not None:
            self.access_level = access_level

    @property
    def id(self):
        """Gets the id of this Share.  # noqa: E501

        the share id  # noqa: E501

        :return: The id of this Share.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Share.

        the share id  # noqa: E501

        :param id: The id of this Share.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def share_to_id(self):
        """Gets the share_to_id of this Share.  # noqa: E501

        the id of the user/group the component is shared with  # noqa: E501

        :return: The share_to_id of this Share.  # noqa: E501
        :rtype: int
        """
        return self._share_to_id

    @share_to_id.setter
    def share_to_id(self, share_to_id):
        """Sets the share_to_id of this Share.

        the id of the user/group the component is shared with  # noqa: E501

        :param share_to_id: The share_to_id of this Share.  # noqa: E501
        :type: int
        """

        self._share_to_id = share_to_id

    @property
    def share_to_type(self):
        """Gets the share_to_type of this Share.  # noqa: E501

        the type of entity shared with (user/group/all)  # noqa: E501

        :return: The share_to_type of this Share.  # noqa: E501
        :rtype: str
        """
        return self._share_to_type

    @share_to_type.setter
    def share_to_type(self, share_to_type):
        """Sets the share_to_type of this Share.

        the type of entity shared with (user/group/all)  # noqa: E501

        :param share_to_type: The share_to_type of this Share.  # noqa: E501
        :type: str
        """

        self._share_to_type = share_to_type

    @property
    def share_to_display_name(self):
        """Gets the share_to_display_name of this Share.  # noqa: E501

        full name of the entity shared with  # noqa: E501

        :return: The share_to_display_name of this Share.  # noqa: E501
        :rtype: str
        """
        return self._share_to_display_name

    @share_to_display_name.setter
    def share_to_display_name(self, share_to_display_name):
        """Sets the share_to_display_name of this Share.

        full name of the entity shared with  # noqa: E501

        :param share_to_display_name: The share_to_display_name of this Share.  # noqa: E501
        :type: str
        """

        self._share_to_display_name = share_to_display_name

    @property
    def component_type(self):
        """Gets the component_type of this Share.  # noqa: E501

        the type of component being shared  # noqa: E501

        :return: The component_type of this Share.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this Share.

        the type of component being shared  # noqa: E501

        :param component_type: The component_type of this Share.  # noqa: E501
        :type: str
        """

        self._component_type = component_type

    @property
    def component_id(self):
        """Gets the component_id of this Share.  # noqa: E501

        the id of the component being shared  # noqa: E501

        :return: The component_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this Share.

        the id of the component being shared  # noqa: E501

        :param component_id: The component_id of this Share.  # noqa: E501
        :type: str
        """

        self._component_id = component_id

    @property
    def access_level(self):
        """Gets the access_level of this Share.  # noqa: E501

        Level of rights shared with entity. (for projects only)  # noqa: E501

        :return: The access_level of this Share.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this Share.

        Level of rights shared with entity. (for projects only)  # noqa: E501

        :param access_level: The access_level of this Share.  # noqa: E501
        :type: str
        """

        self._access_level = access_level

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
        if issubclass(Share, dict):
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
        if not isinstance(other, Share):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
