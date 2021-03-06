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

class UnhashReportData(object):
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
        'total_pages': 'int',
        'first_page': 'bool',
        'last_page': 'bool',
        'number_of_elements': 'int',
        'number': 'int',
        'total_elements': 'int',
        'message': 'str',
        'report_id': 'str',
        'search_and': 'str',
        'search_or': 'str',
        'search_not': 'str',
        'search_phrase': 'str',
        'oberon_request_xml': 'str',
        'oberon_response_xml': 'str',
        'rows': 'list[RowItem]'
    }

    attribute_map = {
        'total_pages': 'totalPages',
        'first_page': 'firstPage',
        'last_page': 'lastPage',
        'number_of_elements': 'numberOfElements',
        'number': 'number',
        'total_elements': 'totalElements',
        'message': 'message',
        'report_id': 'reportId',
        'search_and': 'searchAnd',
        'search_or': 'searchOr',
        'search_not': 'searchNot',
        'search_phrase': 'searchPhrase',
        'oberon_request_xml': 'oberonRequestXML',
        'oberon_response_xml': 'oberonResponseXML',
        'rows': 'rows'
    }

    def __init__(self, total_pages=None, first_page=None, last_page=None, number_of_elements=None, number=None, total_elements=None, message=None, report_id=None, search_and=None, search_or=None, search_not=None, search_phrase=None, oberon_request_xml=None, oberon_response_xml=None, rows=None):  # noqa: E501
        """UnhashReportData - a model defined in Swagger"""  # noqa: E501
        self._total_pages = None
        self._first_page = None
        self._last_page = None
        self._number_of_elements = None
        self._number = None
        self._total_elements = None
        self._message = None
        self._report_id = None
        self._search_and = None
        self._search_or = None
        self._search_not = None
        self._search_phrase = None
        self._oberon_request_xml = None
        self._oberon_response_xml = None
        self._rows = None
        self.discriminator = None
        if total_pages is not None:
            self.total_pages = total_pages
        if first_page is not None:
            self.first_page = first_page
        if last_page is not None:
            self.last_page = last_page
        if number_of_elements is not None:
            self.number_of_elements = number_of_elements
        if number is not None:
            self.number = number
        if total_elements is not None:
            self.total_elements = total_elements
        if message is not None:
            self.message = message
        if report_id is not None:
            self.report_id = report_id
        if search_and is not None:
            self.search_and = search_and
        if search_or is not None:
            self.search_or = search_or
        if search_not is not None:
            self.search_not = search_not
        if search_phrase is not None:
            self.search_phrase = search_phrase
        if oberon_request_xml is not None:
            self.oberon_request_xml = oberon_request_xml
        if oberon_response_xml is not None:
            self.oberon_response_xml = oberon_response_xml
        if rows is not None:
            self.rows = rows

    @property
    def total_pages(self):
        """Gets the total_pages of this UnhashReportData.  # noqa: E501


        :return: The total_pages of this UnhashReportData.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this UnhashReportData.


        :param total_pages: The total_pages of this UnhashReportData.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def first_page(self):
        """Gets the first_page of this UnhashReportData.  # noqa: E501


        :return: The first_page of this UnhashReportData.  # noqa: E501
        :rtype: bool
        """
        return self._first_page

    @first_page.setter
    def first_page(self, first_page):
        """Sets the first_page of this UnhashReportData.


        :param first_page: The first_page of this UnhashReportData.  # noqa: E501
        :type: bool
        """

        self._first_page = first_page

    @property
    def last_page(self):
        """Gets the last_page of this UnhashReportData.  # noqa: E501


        :return: The last_page of this UnhashReportData.  # noqa: E501
        :rtype: bool
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this UnhashReportData.


        :param last_page: The last_page of this UnhashReportData.  # noqa: E501
        :type: bool
        """

        self._last_page = last_page

    @property
    def number_of_elements(self):
        """Gets the number_of_elements of this UnhashReportData.  # noqa: E501


        :return: The number_of_elements of this UnhashReportData.  # noqa: E501
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """Sets the number_of_elements of this UnhashReportData.


        :param number_of_elements: The number_of_elements of this UnhashReportData.  # noqa: E501
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def number(self):
        """Gets the number of this UnhashReportData.  # noqa: E501


        :return: The number of this UnhashReportData.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this UnhashReportData.


        :param number: The number of this UnhashReportData.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def total_elements(self):
        """Gets the total_elements of this UnhashReportData.  # noqa: E501


        :return: The total_elements of this UnhashReportData.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this UnhashReportData.


        :param total_elements: The total_elements of this UnhashReportData.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    @property
    def message(self):
        """Gets the message of this UnhashReportData.  # noqa: E501


        :return: The message of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UnhashReportData.


        :param message: The message of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def report_id(self):
        """Gets the report_id of this UnhashReportData.  # noqa: E501


        :return: The report_id of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this UnhashReportData.


        :param report_id: The report_id of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def search_and(self):
        """Gets the search_and of this UnhashReportData.  # noqa: E501


        :return: The search_and of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._search_and

    @search_and.setter
    def search_and(self, search_and):
        """Sets the search_and of this UnhashReportData.


        :param search_and: The search_and of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._search_and = search_and

    @property
    def search_or(self):
        """Gets the search_or of this UnhashReportData.  # noqa: E501


        :return: The search_or of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._search_or

    @search_or.setter
    def search_or(self, search_or):
        """Sets the search_or of this UnhashReportData.


        :param search_or: The search_or of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._search_or = search_or

    @property
    def search_not(self):
        """Gets the search_not of this UnhashReportData.  # noqa: E501


        :return: The search_not of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._search_not

    @search_not.setter
    def search_not(self, search_not):
        """Sets the search_not of this UnhashReportData.


        :param search_not: The search_not of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._search_not = search_not

    @property
    def search_phrase(self):
        """Gets the search_phrase of this UnhashReportData.  # noqa: E501


        :return: The search_phrase of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._search_phrase

    @search_phrase.setter
    def search_phrase(self, search_phrase):
        """Sets the search_phrase of this UnhashReportData.


        :param search_phrase: The search_phrase of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._search_phrase = search_phrase

    @property
    def oberon_request_xml(self):
        """Gets the oberon_request_xml of this UnhashReportData.  # noqa: E501


        :return: The oberon_request_xml of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._oberon_request_xml

    @oberon_request_xml.setter
    def oberon_request_xml(self, oberon_request_xml):
        """Sets the oberon_request_xml of this UnhashReportData.


        :param oberon_request_xml: The oberon_request_xml of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._oberon_request_xml = oberon_request_xml

    @property
    def oberon_response_xml(self):
        """Gets the oberon_response_xml of this UnhashReportData.  # noqa: E501


        :return: The oberon_response_xml of this UnhashReportData.  # noqa: E501
        :rtype: str
        """
        return self._oberon_response_xml

    @oberon_response_xml.setter
    def oberon_response_xml(self, oberon_response_xml):
        """Sets the oberon_response_xml of this UnhashReportData.


        :param oberon_response_xml: The oberon_response_xml of this UnhashReportData.  # noqa: E501
        :type: str
        """

        self._oberon_response_xml = oberon_response_xml

    @property
    def rows(self):
        """Gets the rows of this UnhashReportData.  # noqa: E501


        :return: The rows of this UnhashReportData.  # noqa: E501
        :rtype: list[RowItem]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this UnhashReportData.


        :param rows: The rows of this UnhashReportData.  # noqa: E501
        :type: list[RowItem]
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
        if issubclass(UnhashReportData, dict):
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
        if not isinstance(other, UnhashReportData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
