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

class RankedRequest(object):
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
        'rsid': 'str',
        'dimension': 'str',
        'locale': 'Locale',
        'global_filters': 'list[ReportFilter]',
        'search': 'ReportSearch',
        'settings': 'RankedSettings',
        'statistics': 'RankedStatistics',
        'metric_container': 'ReportMetrics',
        'row_container': 'ReportRows',
        'anchor_date': 'str'
    }

    attribute_map = {
        'rsid': 'rsid',
        'dimension': 'dimension',
        'locale': 'locale',
        'global_filters': 'globalFilters',
        'search': 'search',
        'settings': 'settings',
        'statistics': 'statistics',
        'metric_container': 'metricContainer',
        'row_container': 'rowContainer',
        'anchor_date': 'anchorDate'
    }

    def __init__(self, rsid=None, dimension=None, locale=None, global_filters=None, search=None, settings=None, statistics=None, metric_container=None, row_container=None, anchor_date=None):  # noqa: E501
        """RankedRequest - a model defined in Swagger"""  # noqa: E501
        self._rsid = None
        self._dimension = None
        self._locale = None
        self._global_filters = None
        self._search = None
        self._settings = None
        self._statistics = None
        self._metric_container = None
        self._row_container = None
        self._anchor_date = None
        self.discriminator = None
        if rsid is not None:
            self.rsid = rsid
        if dimension is not None:
            self.dimension = dimension
        if locale is not None:
            self.locale = locale
        if global_filters is not None:
            self.global_filters = global_filters
        if search is not None:
            self.search = search
        if settings is not None:
            self.settings = settings
        if statistics is not None:
            self.statistics = statistics
        if metric_container is not None:
            self.metric_container = metric_container
        if row_container is not None:
            self.row_container = row_container
        if anchor_date is not None:
            self.anchor_date = anchor_date

    @property
    def rsid(self):
        """Gets the rsid of this RankedRequest.  # noqa: E501


        :return: The rsid of this RankedRequest.  # noqa: E501
        :rtype: str
        """
        return self._rsid

    @rsid.setter
    def rsid(self, rsid):
        """Sets the rsid of this RankedRequest.


        :param rsid: The rsid of this RankedRequest.  # noqa: E501
        :type: str
        """

        self._rsid = rsid

    @property
    def dimension(self):
        """Gets the dimension of this RankedRequest.  # noqa: E501


        :return: The dimension of this RankedRequest.  # noqa: E501
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this RankedRequest.


        :param dimension: The dimension of this RankedRequest.  # noqa: E501
        :type: str
        """

        self._dimension = dimension

    @property
    def locale(self):
        """Gets the locale of this RankedRequest.  # noqa: E501


        :return: The locale of this RankedRequest.  # noqa: E501
        :rtype: Locale
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this RankedRequest.


        :param locale: The locale of this RankedRequest.  # noqa: E501
        :type: Locale
        """

        self._locale = locale

    @property
    def global_filters(self):
        """Gets the global_filters of this RankedRequest.  # noqa: E501


        :return: The global_filters of this RankedRequest.  # noqa: E501
        :rtype: list[ReportFilter]
        """
        return self._global_filters

    @global_filters.setter
    def global_filters(self, global_filters):
        """Sets the global_filters of this RankedRequest.


        :param global_filters: The global_filters of this RankedRequest.  # noqa: E501
        :type: list[ReportFilter]
        """

        self._global_filters = global_filters

    @property
    def search(self):
        """Gets the search of this RankedRequest.  # noqa: E501


        :return: The search of this RankedRequest.  # noqa: E501
        :rtype: ReportSearch
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this RankedRequest.


        :param search: The search of this RankedRequest.  # noqa: E501
        :type: ReportSearch
        """

        self._search = search

    @property
    def settings(self):
        """Gets the settings of this RankedRequest.  # noqa: E501


        :return: The settings of this RankedRequest.  # noqa: E501
        :rtype: RankedSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this RankedRequest.


        :param settings: The settings of this RankedRequest.  # noqa: E501
        :type: RankedSettings
        """

        self._settings = settings

    @property
    def statistics(self):
        """Gets the statistics of this RankedRequest.  # noqa: E501


        :return: The statistics of this RankedRequest.  # noqa: E501
        :rtype: RankedStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this RankedRequest.


        :param statistics: The statistics of this RankedRequest.  # noqa: E501
        :type: RankedStatistics
        """

        self._statistics = statistics

    @property
    def metric_container(self):
        """Gets the metric_container of this RankedRequest.  # noqa: E501


        :return: The metric_container of this RankedRequest.  # noqa: E501
        :rtype: ReportMetrics
        """
        return self._metric_container

    @metric_container.setter
    def metric_container(self, metric_container):
        """Sets the metric_container of this RankedRequest.


        :param metric_container: The metric_container of this RankedRequest.  # noqa: E501
        :type: ReportMetrics
        """

        self._metric_container = metric_container

    @property
    def row_container(self):
        """Gets the row_container of this RankedRequest.  # noqa: E501


        :return: The row_container of this RankedRequest.  # noqa: E501
        :rtype: ReportRows
        """
        return self._row_container

    @row_container.setter
    def row_container(self, row_container):
        """Sets the row_container of this RankedRequest.


        :param row_container: The row_container of this RankedRequest.  # noqa: E501
        :type: ReportRows
        """

        self._row_container = row_container

    @property
    def anchor_date(self):
        """Gets the anchor_date of this RankedRequest.  # noqa: E501


        :return: The anchor_date of this RankedRequest.  # noqa: E501
        :rtype: str
        """
        return self._anchor_date

    @anchor_date.setter
    def anchor_date(self, anchor_date):
        """Sets the anchor_date of this RankedRequest.


        :param anchor_date: The anchor_date of this RankedRequest.  # noqa: E501
        :type: str
        """

        self._anchor_date = anchor_date

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
        if issubclass(RankedRequest, dict):
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
        if not isinstance(other, RankedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other