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

class IdentityMetric(object):
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
        'identity': 'str',
        'dimension_view': 'str',
        'allocation_model': 'str'
    }

    attribute_map = {
        'identity': 'identity',
        'dimension_view': 'dimensionView',
        'allocation_model': 'allocationModel'
    }

    def __init__(self, identity=None, dimension_view=None, allocation_model=None):  # noqa: E501
        """IdentityMetric - a model defined in Swagger"""  # noqa: E501
        self._identity = None
        self._dimension_view = None
        self._allocation_model = None
        self.discriminator = None
        if identity is not None:
            self.identity = identity
        if dimension_view is not None:
            self.dimension_view = dimension_view
        if allocation_model is not None:
            self.allocation_model = allocation_model

    @property
    def identity(self):
        """Gets the identity of this IdentityMetric.  # noqa: E501


        :return: The identity of this IdentityMetric.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this IdentityMetric.


        :param identity: The identity of this IdentityMetric.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def dimension_view(self):
        """Gets the dimension_view of this IdentityMetric.  # noqa: E501


        :return: The dimension_view of this IdentityMetric.  # noqa: E501
        :rtype: str
        """
        return self._dimension_view

    @dimension_view.setter
    def dimension_view(self, dimension_view):
        """Sets the dimension_view of this IdentityMetric.


        :param dimension_view: The dimension_view of this IdentityMetric.  # noqa: E501
        :type: str
        """
        allowed_values = ["LINEAR_ALLOCATION", "PARTICIPATION_ALLOCATION", "LAST_TOUCH_ALLOCATION", "MC_FIRST_TOUCH_ALLOCATION", "MC_LAST_TOUCH_ALLOCATION"]  # noqa: E501
        if dimension_view not in allowed_values:
            raise ValueError(
                "Invalid value for `dimension_view` ({0}), must be one of {1}"  # noqa: E501
                .format(dimension_view, allowed_values)
            )

        self._dimension_view = dimension_view

    @property
    def allocation_model(self):
        """Gets the allocation_model of this IdentityMetric.  # noqa: E501


        :return: The allocation_model of this IdentityMetric.  # noqa: E501
        :rtype: str
        """
        return self._allocation_model

    @allocation_model.setter
    def allocation_model(self, allocation_model):
        """Sets the allocation_model of this IdentityMetric.


        :param allocation_model: The allocation_model of this IdentityMetric.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOCATION_FIRST_TOUCH", "ALLOCATION_LAST_TOUCH", "ALLOCATION_INSTANCE", "ALLOCATION_DEDUPED_INSTANCE", "ALLOCATION_LAST_KNOWN", "ALLOCATION_LEGACY", "ALLOCATION_LINEAR", "ALLOCATION_PARTICIPATION", "ALLOCATION_POSITION_BASED", "ALLOCATION_TIME_DECAY", "ALLOCATION_U_SHAPED", "ALLOCATION_J_SHAPED", "ALLOCATION_REVERSE_J_SHAPED"]  # noqa: E501
        if allocation_model not in allowed_values:
            raise ValueError(
                "Invalid value for `allocation_model` ({0}), must be one of {1}"  # noqa: E501
                .format(allocation_model, allowed_values)
            )

        self._allocation_model = allocation_model

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
        if issubclass(IdentityMetric, dict):
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
        if not isinstance(other, IdentityMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
