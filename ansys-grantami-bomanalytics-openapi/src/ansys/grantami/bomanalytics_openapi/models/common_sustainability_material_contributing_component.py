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


class CommonSustainabilityMaterialContributingComponent(ModelBase):
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
        "component_name": "str",
        "record_reference": "CommonPartReference",
        "material_mass_before_processing": "CommonValueWithUnit",
    }

    attribute_map = {
        "component_name": "ComponentName",
        "record_reference": "RecordReference",
        "material_mass_before_processing": "MaterialMassBeforeProcessing",
    }

    subtype_mapping = {
        "RecordReference": "CommonPartReference",
        "MaterialMassBeforeProcessing": "CommonValueWithUnit",
    }

    def __init__(
        self,
        *,
        component_name: "Optional[str]" = None,
        material_mass_before_processing: "Optional[CommonValueWithUnit]" = None,
        record_reference: "Optional[CommonPartReference]" = None,
    ) -> None:
        """CommonSustainabilityMaterialContributingComponent - a model defined in Swagger

        Parameters
        ----------
            component_name: str, optional
            material_mass_before_processing: CommonValueWithUnit, optional
            record_reference: CommonPartReference, optional
        """
        self._component_name = None
        self._record_reference = None
        self._material_mass_before_processing = None
        self.discriminator = None
        if component_name is not None:
            self.component_name = component_name
        if record_reference is not None:
            self.record_reference = record_reference
        if material_mass_before_processing is not None:
            self.material_mass_before_processing = material_mass_before_processing

    @property
    def component_name(self) -> "str":
        """Gets the component_name of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        str
            The component_name of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name: "str") -> None:
        """Sets the component_name of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        component_name: str
            The component_name of this CommonSustainabilityMaterialContributingComponent.
        """
        self._component_name = component_name

    @property
    def record_reference(self) -> "CommonPartReference":
        """Gets the record_reference of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        CommonPartReference
            The record_reference of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._record_reference

    @record_reference.setter
    def record_reference(self, record_reference: "CommonPartReference") -> None:
        """Sets the record_reference of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        record_reference: CommonPartReference
            The record_reference of this CommonSustainabilityMaterialContributingComponent.
        """
        self._record_reference = record_reference

    @property
    def material_mass_before_processing(self) -> "CommonValueWithUnit":
        """Gets the material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        CommonValueWithUnit
            The material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._material_mass_before_processing

    @material_mass_before_processing.setter
    def material_mass_before_processing(
        self, material_mass_before_processing: "CommonValueWithUnit"
    ) -> None:
        """Sets the material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        material_mass_before_processing: CommonValueWithUnit
            The material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.
        """
        self._material_mass_before_processing = material_mass_before_processing

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
        if issubclass(CommonSustainabilityMaterialContributingComponent, dict):
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
        if not isinstance(other, CommonSustainabilityMaterialContributingComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
