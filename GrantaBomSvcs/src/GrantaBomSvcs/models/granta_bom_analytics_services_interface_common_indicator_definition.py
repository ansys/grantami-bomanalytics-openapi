# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import Model


class GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition(Model):
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
        'name': 'str',
        'legislation_names': 'list[str]',
        'default_threshold_percentage': 'float',
        'ignore_exemptions': 'bool',
        'ignore_process_chemicals': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'legislation_names': 'LegislationNames',
        'default_threshold_percentage': 'DefaultThresholdPercentage',
        'ignore_exemptions': 'IgnoreExemptions',
        'ignore_process_chemicals': 'IgnoreProcessChemicals',
        'type': 'Type'
    }

    subtype_mapping = {
        
        
        
        
        
        
    }


    def __init__(self, name=None, legislation_names=None, default_threshold_percentage=None, ignore_exemptions=None, ignore_process_chemicals=None, type=None):  # noqa: E501
        """GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._legislation_names = None
        self._default_threshold_percentage = None
        self._ignore_exemptions = None
        self._ignore_process_chemicals = None
        self._type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if legislation_names is not None:
            self.legislation_names = legislation_names
        if default_threshold_percentage is not None:
            self.default_threshold_percentage = default_threshold_percentage
        if ignore_exemptions is not None:
            self.ignore_exemptions = ignore_exemptions
        if ignore_process_chemicals is not None:
            self.ignore_process_chemicals = ignore_process_chemicals
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501


        :return: The name of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.


        :param name: The name of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def legislation_names(self):
        """Gets the legislation_names of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501


        :return: The legislation_names of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._legislation_names

    @legislation_names.setter
    def legislation_names(self, legislation_names):
        """Sets the legislation_names of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.


        :param legislation_names: The legislation_names of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :type: list[str]
        """

        self._legislation_names = legislation_names

    @property
    def default_threshold_percentage(self):
        """Gets the default_threshold_percentage of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501


        :return: The default_threshold_percentage of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :rtype: float
        """
        return self._default_threshold_percentage

    @default_threshold_percentage.setter
    def default_threshold_percentage(self, default_threshold_percentage):
        """Sets the default_threshold_percentage of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.


        :param default_threshold_percentage: The default_threshold_percentage of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :type: float
        """

        self._default_threshold_percentage = default_threshold_percentage

    @property
    def ignore_exemptions(self):
        """Gets the ignore_exemptions of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501


        :return: The ignore_exemptions of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_exemptions

    @ignore_exemptions.setter
    def ignore_exemptions(self, ignore_exemptions):
        """Sets the ignore_exemptions of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.


        :param ignore_exemptions: The ignore_exemptions of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :type: bool
        """

        self._ignore_exemptions = ignore_exemptions

    @property
    def ignore_process_chemicals(self):
        """Gets the ignore_process_chemicals of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501


        :return: The ignore_process_chemicals of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_process_chemicals

    @ignore_process_chemicals.setter
    def ignore_process_chemicals(self, ignore_process_chemicals):
        """Sets the ignore_process_chemicals of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.


        :param ignore_process_chemicals: The ignore_process_chemicals of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :type: bool
        """

        self._ignore_process_chemicals = ignore_process_chemicals

    @property
    def type(self):
        """Gets the type of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501


        :return: The type of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.


        :param type: The type of this GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types.keys():
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
        if issubclass(GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition, dict):
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
        if not isinstance(other, GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
