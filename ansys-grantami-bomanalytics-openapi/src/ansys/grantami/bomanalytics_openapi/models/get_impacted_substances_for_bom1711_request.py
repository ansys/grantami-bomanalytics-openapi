# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import ModelBase


class GetImpactedSubstancesForBom1711Request(ModelBase):
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
        "bom_xml1711": "str",
        "legislation_names": "list[str]",
        "database_key": "str",
        "config": "CommonRequestConfig",
    }

    attribute_map = {
        "bom_xml1711": "BomXml1711",
        "legislation_names": "LegislationNames",
        "database_key": "DatabaseKey",
        "config": "Config",
    }

    subtype_mapping = {"Config": "CommonRequestConfig"}

    def __init__(
        self, bom_xml1711=None, legislation_names=None, database_key=None, config=None
    ):  # noqa: E501
        """GetImpactedSubstancesForBom1711Request - a model defined in Swagger"""  # noqa: E501
        self._bom_xml1711 = None
        self._legislation_names = None
        self._database_key = None
        self._config = None
        self.discriminator = None
        if bom_xml1711 is not None:
            self.bom_xml1711 = bom_xml1711
        if legislation_names is not None:
            self.legislation_names = legislation_names
        if database_key is not None:
            self.database_key = database_key
        if config is not None:
            self.config = config

    @property
    def bom_xml1711(self):
        """Gets the bom_xml1711 of this GetImpactedSubstancesForBom1711Request.  # noqa: E501

        :return: The bom_xml1711 of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :rtype: str
        """
        return self._bom_xml1711

    @bom_xml1711.setter
    def bom_xml1711(self, bom_xml1711):
        """Sets the bom_xml1711 of this GetImpactedSubstancesForBom1711Request.

        :param bom_xml1711: The bom_xml1711 of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :type: str
        """
        self._bom_xml1711 = bom_xml1711

    @property
    def legislation_names(self):
        """Gets the legislation_names of this GetImpactedSubstancesForBom1711Request.  # noqa: E501

        :return: The legislation_names of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :rtype: list[str]
        """
        return self._legislation_names

    @legislation_names.setter
    def legislation_names(self, legislation_names):
        """Sets the legislation_names of this GetImpactedSubstancesForBom1711Request.

        :param legislation_names: The legislation_names of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :type: list[str]
        """
        self._legislation_names = legislation_names

    @property
    def database_key(self):
        """Gets the database_key of this GetImpactedSubstancesForBom1711Request.  # noqa: E501

        :return: The database_key of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GetImpactedSubstancesForBom1711Request.

        :param database_key: The database_key of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    @property
    def config(self):
        """Gets the config of this GetImpactedSubstancesForBom1711Request.  # noqa: E501

        :return: The config of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :rtype: CommonRequestConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetImpactedSubstancesForBom1711Request.

        :param config: The config of this GetImpactedSubstancesForBom1711Request.  # noqa: E501
        :type: CommonRequestConfig
        """
        self._config = config

    def get_real_child_model(self, data):
        """Raises a NotImplementedError for a type without a discriminator defined."""
        raise NotImplementedError()

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GetImpactedSubstancesForBom1711Request, dict):
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
        if not isinstance(other, GetImpactedSubstancesForBom1711Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
