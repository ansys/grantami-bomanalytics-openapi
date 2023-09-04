"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GetImpactedSubstancesForMaterialsMaterial(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.

    """
    swagger_types = {
        "legislations": "list[CommonLegislationWithImpactedSubstances]",
        "reference_type": "str",
        "reference_value": "str",
    }

    attribute_map = {
        "legislations": "Legislations",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
    }

    subtype_mapping = {
        "Legislations": "CommonLegislationWithImpactedSubstances",
    }

    def __init__(
        self,
        *,
        legislations: "Optional[List[CommonLegislationWithImpactedSubstances]]" = None,
        reference_type: "Optional[str]" = None,
        reference_value: "Optional[str]" = None,
    ) -> None:
        """GetImpactedSubstancesForMaterialsMaterial - a model defined in Swagger

        Parameters
        ----------
            legislations: List[CommonLegislationWithImpactedSubstances], optional
            reference_type: str, optional
            reference_value: str, optional
        """
        self._legislations = None
        self._reference_type = None
        self._reference_value = None
        self.discriminator = None
        if legislations is not None:
            self.legislations = legislations
        if reference_type is not None:
            self.reference_type = reference_type
        if reference_value is not None:
            self.reference_value = reference_value

    @property
    def legislations(self) -> "list[CommonLegislationWithImpactedSubstances]":
        """Gets the legislations of this GetImpactedSubstancesForMaterialsMaterial.

        Returns
        -------
        list[CommonLegislationWithImpactedSubstances]
            The legislations of this GetImpactedSubstancesForMaterialsMaterial.
        """
        return self._legislations

    @legislations.setter
    def legislations(
        self, legislations: "list[CommonLegislationWithImpactedSubstances]"
    ) -> None:
        """Sets the legislations of this GetImpactedSubstancesForMaterialsMaterial.

        Parameters
        ----------
        legislations: list[CommonLegislationWithImpactedSubstances]
            The legislations of this GetImpactedSubstancesForMaterialsMaterial.
        """
        self._legislations = legislations

    @property
    def reference_type(self) -> "str":
        """Gets the reference_type of this GetImpactedSubstancesForMaterialsMaterial.

        Returns
        -------
        str
            The reference_type of this GetImpactedSubstancesForMaterialsMaterial.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "str") -> None:
        """Sets the reference_type of this GetImpactedSubstancesForMaterialsMaterial.

        Parameters
        ----------
        reference_type: str
            The reference_type of this GetImpactedSubstancesForMaterialsMaterial.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "str":
        """Gets the reference_value of this GetImpactedSubstancesForMaterialsMaterial.

        Returns
        -------
        str
            The reference_value of this GetImpactedSubstancesForMaterialsMaterial.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "str") -> None:
        """Sets the reference_value of this GetImpactedSubstancesForMaterialsMaterial.

        Parameters
        ----------
        reference_value: str
            The reference_value of this GetImpactedSubstancesForMaterialsMaterial.
        """
        self._reference_value = reference_value

    def get_real_child_model(self, data: ModelBase) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
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
        if issubclass(GetImpactedSubstancesForMaterialsMaterial, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GetImpactedSubstancesForMaterialsMaterial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
