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


class CommonSpecificationWithCompliance(Model):
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
        'indicators': 'list[CommonIndicatorResult]',
        'specifications': 'list[CommonSpecificationWithCompliance]',
        'coatings': 'list[CommonCoatingWithCompliance]',
        'materials': 'list[CommonMaterialWithCompliance]',
        'substances': 'list[CommonSubstanceWithCompliance]',
        'reference_type': 'str',
        'reference_value': 'str'
    }

    attribute_map = {
        'indicators': 'Indicators',
        'specifications': 'Specifications',
        'coatings': 'Coatings',
        'materials': 'Materials',
        'substances': 'Substances',
        'reference_type': 'ReferenceType',
        'reference_value': 'ReferenceValue'
    }

    subtype_mapping = {
        'Indicators': 'CommonIndicatorResult',
        'Specifications': 'CommonSpecificationWithCompliance',
        'Coatings': 'CommonCoatingWithCompliance',
        'Materials': 'CommonMaterialWithCompliance',
        'Substances': 'CommonSubstanceWithCompliance',
    }


    def __init__(self, indicators=None, specifications=None, coatings=None, materials=None, substances=None, reference_type=None, reference_value=None):  # noqa: E501
        """CommonSpecificationWithCompliance - a model defined in Swagger"""  # noqa: E501
        self._indicators = None
        self._specifications = None
        self._coatings = None
        self._materials = None
        self._substances = None
        self._reference_type = None
        self._reference_value = None
        self.discriminator = None
        if indicators is not None:
            self.indicators = indicators
        if specifications is not None:
            self.specifications = specifications
        if coatings is not None:
            self.coatings = coatings
        if materials is not None:
            self.materials = materials
        if substances is not None:
            self.substances = substances
        if reference_type is not None:
            self.reference_type = reference_type
        if reference_value is not None:
            self.reference_value = reference_value

    @property
    def indicators(self):
        """Gets the indicators of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The indicators of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: list[CommonIndicatorResult]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this CommonSpecificationWithCompliance.

        :param indicators: The indicators of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: list[CommonIndicatorResult]
        """
        self._indicators = indicators

    @property
    def specifications(self):
        """Gets the specifications of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The specifications of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: list[CommonSpecificationWithCompliance]
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this CommonSpecificationWithCompliance.

        :param specifications: The specifications of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: list[CommonSpecificationWithCompliance]
        """
        self._specifications = specifications

    @property
    def coatings(self):
        """Gets the coatings of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The coatings of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: list[CommonCoatingWithCompliance]
        """
        return self._coatings

    @coatings.setter
    def coatings(self, coatings):
        """Sets the coatings of this CommonSpecificationWithCompliance.

        :param coatings: The coatings of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: list[CommonCoatingWithCompliance]
        """
        self._coatings = coatings

    @property
    def materials(self):
        """Gets the materials of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The materials of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: list[CommonMaterialWithCompliance]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this CommonSpecificationWithCompliance.

        :param materials: The materials of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: list[CommonMaterialWithCompliance]
        """
        self._materials = materials

    @property
    def substances(self):
        """Gets the substances of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The substances of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: list[CommonSubstanceWithCompliance]
        """
        return self._substances

    @substances.setter
    def substances(self, substances):
        """Sets the substances of this CommonSpecificationWithCompliance.

        :param substances: The substances of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: list[CommonSubstanceWithCompliance]
        """
        self._substances = substances

    @property
    def reference_type(self):
        """Gets the reference_type of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The reference_type of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this CommonSpecificationWithCompliance.

        :param reference_type: The reference_type of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: str
        """
        self._reference_type = reference_type

    @property
    def reference_value(self):
        """Gets the reference_value of this CommonSpecificationWithCompliance.  # noqa: E501

        :return: The reference_value of this CommonSpecificationWithCompliance.  # noqa: E501
        :rtype: str
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value):
        """Sets the reference_value of this CommonSpecificationWithCompliance.

        :param reference_value: The reference_value of this CommonSpecificationWithCompliance.  # noqa: E501
        :type: str
        """
        self._reference_value = reference_value

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
        if issubclass(CommonSpecificationWithCompliance, dict):
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
        if not isinstance(other, CommonSpecificationWithCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
