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

class TaggedComponent(object):
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
        'component_type': 'str',
        'component_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'component_type': 'componentType',
        'component_id': 'componentId',
        'tags': 'tags'
    }

    def __init__(self, component_type=None, component_id=None, tags=None):  # noqa: E501
        """TaggedComponent - a model defined in Swagger"""  # noqa: E501
        self._component_type = None
        self._component_id = None
        self._tags = None
        self.discriminator = None
        if component_type is not None:
            self.component_type = component_type
        if component_id is not None:
            self.component_id = component_id
        if tags is not None:
            self.tags = tags

    @property
    def component_type(self):
        """Gets the component_type of this TaggedComponent.  # noqa: E501


        :return: The component_type of this TaggedComponent.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this TaggedComponent.


        :param component_type: The component_type of this TaggedComponent.  # noqa: E501
        :type: str
        """

        self._component_type = component_type

    @property
    def component_id(self):
        """Gets the component_id of this TaggedComponent.  # noqa: E501


        :return: The component_id of this TaggedComponent.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this TaggedComponent.


        :param component_id: The component_id of this TaggedComponent.  # noqa: E501
        :type: str
        """

        self._component_id = component_id

    @property
    def tags(self):
        """Gets the tags of this TaggedComponent.  # noqa: E501


        :return: The tags of this TaggedComponent.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaggedComponent.


        :param tags: The tags of this TaggedComponent.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

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
        if issubclass(TaggedComponent, dict):
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
        if not isinstance(other, TaggedComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
