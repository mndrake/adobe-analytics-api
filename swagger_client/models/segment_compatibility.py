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

class SegmentCompatibility(object):
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
        'valid': 'bool',
        'message': 'str',
        'validator_version': 'str',
        'supported_products': 'list[str]',
        'supported_schema': 'list[str]',
        'supported_features': 'list[str]'
    }

    attribute_map = {
        'valid': 'valid',
        'message': 'message',
        'validator_version': 'validator_version',
        'supported_products': 'supported_products',
        'supported_schema': 'supported_schema',
        'supported_features': 'supported_features'
    }

    def __init__(self, valid=None, message=None, validator_version=None, supported_products=None, supported_schema=None, supported_features=None):  # noqa: E501
        """SegmentCompatibility - a model defined in Swagger"""  # noqa: E501
        self._valid = None
        self._message = None
        self._validator_version = None
        self._supported_products = None
        self._supported_schema = None
        self._supported_features = None
        self.discriminator = None
        if valid is not None:
            self.valid = valid
        if message is not None:
            self.message = message
        if validator_version is not None:
            self.validator_version = validator_version
        if supported_products is not None:
            self.supported_products = supported_products
        if supported_schema is not None:
            self.supported_schema = supported_schema
        if supported_features is not None:
            self.supported_features = supported_features

    @property
    def valid(self):
        """Gets the valid of this SegmentCompatibility.  # noqa: E501


        :return: The valid of this SegmentCompatibility.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this SegmentCompatibility.


        :param valid: The valid of this SegmentCompatibility.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def message(self):
        """Gets the message of this SegmentCompatibility.  # noqa: E501


        :return: The message of this SegmentCompatibility.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SegmentCompatibility.


        :param message: The message of this SegmentCompatibility.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def validator_version(self):
        """Gets the validator_version of this SegmentCompatibility.  # noqa: E501


        :return: The validator_version of this SegmentCompatibility.  # noqa: E501
        :rtype: str
        """
        return self._validator_version

    @validator_version.setter
    def validator_version(self, validator_version):
        """Sets the validator_version of this SegmentCompatibility.


        :param validator_version: The validator_version of this SegmentCompatibility.  # noqa: E501
        :type: str
        """

        self._validator_version = validator_version

    @property
    def supported_products(self):
        """Gets the supported_products of this SegmentCompatibility.  # noqa: E501


        :return: The supported_products of this SegmentCompatibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_products

    @supported_products.setter
    def supported_products(self, supported_products):
        """Sets the supported_products of this SegmentCompatibility.


        :param supported_products: The supported_products of this SegmentCompatibility.  # noqa: E501
        :type: list[str]
        """

        self._supported_products = supported_products

    @property
    def supported_schema(self):
        """Gets the supported_schema of this SegmentCompatibility.  # noqa: E501


        :return: The supported_schema of this SegmentCompatibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_schema

    @supported_schema.setter
    def supported_schema(self, supported_schema):
        """Sets the supported_schema of this SegmentCompatibility.


        :param supported_schema: The supported_schema of this SegmentCompatibility.  # noqa: E501
        :type: list[str]
        """

        self._supported_schema = supported_schema

    @property
    def supported_features(self):
        """Gets the supported_features of this SegmentCompatibility.  # noqa: E501


        :return: The supported_features of this SegmentCompatibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this SegmentCompatibility.


        :param supported_features: The supported_features of this SegmentCompatibility.  # noqa: E501
        :type: list[str]
        """

        self._supported_features = supported_features

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
        if issubclass(SegmentCompatibility, dict):
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
        if not isinstance(other, SegmentCompatibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
