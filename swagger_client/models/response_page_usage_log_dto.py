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

class ResponsePageUsageLogDto(object):
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
        'content': 'list[UsageLogDto]',
        'total_elements': 'int',
        'last_page': 'bool',
        'number_of_elements': 'int',
        'total_pages': 'int',
        'first_page': 'bool',
        'sort': 'str',
        'size': 'int',
        'number': 'int'
    }

    attribute_map = {
        'content': 'content',
        'total_elements': 'totalElements',
        'last_page': 'lastPage',
        'number_of_elements': 'numberOfElements',
        'total_pages': 'totalPages',
        'first_page': 'firstPage',
        'sort': 'sort',
        'size': 'size',
        'number': 'number'
    }

    def __init__(self, content=None, total_elements=None, last_page=None, number_of_elements=None, total_pages=None, first_page=None, sort=None, size=None, number=None):  # noqa: E501
        """ResponsePageUsageLogDto - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._total_elements = None
        self._last_page = None
        self._number_of_elements = None
        self._total_pages = None
        self._first_page = None
        self._sort = None
        self._size = None
        self._number = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if total_elements is not None:
            self.total_elements = total_elements
        if last_page is not None:
            self.last_page = last_page
        if number_of_elements is not None:
            self.number_of_elements = number_of_elements
        if total_pages is not None:
            self.total_pages = total_pages
        if first_page is not None:
            self.first_page = first_page
        if sort is not None:
            self.sort = sort
        if size is not None:
            self.size = size
        if number is not None:
            self.number = number

    @property
    def content(self):
        """Gets the content of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The content of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: list[UsageLogDto]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ResponsePageUsageLogDto.


        :param content: The content of this ResponsePageUsageLogDto.  # noqa: E501
        :type: list[UsageLogDto]
        """

        self._content = content

    @property
    def total_elements(self):
        """Gets the total_elements of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The total_elements of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this ResponsePageUsageLogDto.


        :param total_elements: The total_elements of this ResponsePageUsageLogDto.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    @property
    def last_page(self):
        """Gets the last_page of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The last_page of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: bool
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this ResponsePageUsageLogDto.


        :param last_page: The last_page of this ResponsePageUsageLogDto.  # noqa: E501
        :type: bool
        """

        self._last_page = last_page

    @property
    def number_of_elements(self):
        """Gets the number_of_elements of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The number_of_elements of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """Sets the number_of_elements of this ResponsePageUsageLogDto.


        :param number_of_elements: The number_of_elements of this ResponsePageUsageLogDto.  # noqa: E501
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def total_pages(self):
        """Gets the total_pages of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The total_pages of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this ResponsePageUsageLogDto.


        :param total_pages: The total_pages of this ResponsePageUsageLogDto.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def first_page(self):
        """Gets the first_page of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The first_page of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: bool
        """
        return self._first_page

    @first_page.setter
    def first_page(self, first_page):
        """Sets the first_page of this ResponsePageUsageLogDto.


        :param first_page: The first_page of this ResponsePageUsageLogDto.  # noqa: E501
        :type: bool
        """

        self._first_page = first_page

    @property
    def sort(self):
        """Gets the sort of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The sort of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ResponsePageUsageLogDto.


        :param sort: The sort of this ResponsePageUsageLogDto.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def size(self):
        """Gets the size of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The size of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResponsePageUsageLogDto.


        :param size: The size of this ResponsePageUsageLogDto.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def number(self):
        """Gets the number of this ResponsePageUsageLogDto.  # noqa: E501


        :return: The number of this ResponsePageUsageLogDto.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ResponsePageUsageLogDto.


        :param number: The number of this ResponsePageUsageLogDto.  # noqa: E501
        :type: int
        """

        self._number = number

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
        if issubclass(ResponsePageUsageLogDto, dict):
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
        if not isinstance(other, ResponsePageUsageLogDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other