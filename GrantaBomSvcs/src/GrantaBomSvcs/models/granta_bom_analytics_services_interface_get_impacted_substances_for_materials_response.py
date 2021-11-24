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


class GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse(Model):
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
        'materials': 'list[GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsMaterial]'
    }

    attribute_map = {
        'materials': 'Materials'
    }

    subtype_mapping = {
        'Materials': 'GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsMaterial'
    }


    def __init__(self, materials=None):  # noqa: E501
        """GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse - a model defined in Swagger"""  # noqa: E501
        self._materials = None
        self.discriminator = None
        if materials is not None:
            self.materials = materials

    @property
    def materials(self):
        """Gets the materials of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse.  # noqa: E501

        :return: The materials of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse.  # noqa: E501
        :rtype: list[GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsMaterial]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse.

        :param materials: The materials of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse.  # noqa: E501
        :type: list[GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsMaterial]
        """
        self._materials = materials

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
        if issubclass(GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse, dict):
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
        if not isinstance(other, GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
