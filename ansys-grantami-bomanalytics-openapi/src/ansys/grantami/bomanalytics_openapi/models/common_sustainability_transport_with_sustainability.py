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


class CommonSustainabilityTransportWithSustainability(ModelBase):
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
        "embodied_energy": "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit",
        "climate_change": "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit",
        "reference_type": "str",
        "reference_value": "str",
    }

    attribute_map = {
        "embodied_energy": "EmbodiedEnergy",
        "climate_change": "ClimateChange",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
    }

    subtype_mapping = {
        "EmbodiedEnergy": "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit",
        "ClimateChange": "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit",
    }

    def __init__(
        self,
        *,
        climate_change: "Optional[GrantaBomAnalyticsServicesImplementationCommonValueWithUnit]" = None,
        embodied_energy: "Optional[GrantaBomAnalyticsServicesImplementationCommonValueWithUnit]" = None,
        reference_type: "Optional[str]" = None,
        reference_value: "Optional[str]" = None,
    ) -> None:
        """CommonSustainabilityTransportWithSustainability - a model defined in Swagger

        Parameters
        ----------
            climate_change: GrantaBomAnalyticsServicesImplementationCommonValueWithUnit, optional
            embodied_energy: GrantaBomAnalyticsServicesImplementationCommonValueWithUnit, optional
            reference_type: str, optional
            reference_value: str, optional
        """
        self._embodied_energy = None
        self._climate_change = None
        self._reference_type = None
        self._reference_value = None
        self.discriminator = None
        if embodied_energy is not None:
            self.embodied_energy = embodied_energy
        if climate_change is not None:
            self.climate_change = climate_change
        if reference_type is not None:
            self.reference_type = reference_type
        if reference_value is not None:
            self.reference_value = reference_value

    @property
    def embodied_energy(
        self,
    ) -> "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit":
        """Gets the embodied_energy of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        GrantaBomAnalyticsServicesImplementationCommonValueWithUnit
            The embodied_energy of this CommonSustainabilityTransportWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(
        self,
        embodied_energy: "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit",
    ) -> None:
        """Sets the embodied_energy of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        embodied_energy: GrantaBomAnalyticsServicesImplementationCommonValueWithUnit
            The embodied_energy of this CommonSustainabilityTransportWithSustainability.
        """
        self._embodied_energy = embodied_energy

    @property
    def climate_change(
        self,
    ) -> "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit":
        """Gets the climate_change of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        GrantaBomAnalyticsServicesImplementationCommonValueWithUnit
            The climate_change of this CommonSustainabilityTransportWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(
        self,
        climate_change: "GrantaBomAnalyticsServicesImplementationCommonValueWithUnit",
    ) -> None:
        """Sets the climate_change of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        climate_change: GrantaBomAnalyticsServicesImplementationCommonValueWithUnit
            The climate_change of this CommonSustainabilityTransportWithSustainability.
        """
        self._climate_change = climate_change

    @property
    def reference_type(self) -> "str":
        """Gets the reference_type of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        str
            The reference_type of this CommonSustainabilityTransportWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "str") -> None:
        """Sets the reference_type of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        reference_type: str
            The reference_type of this CommonSustainabilityTransportWithSustainability.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "str":
        """Gets the reference_value of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        str
            The reference_value of this CommonSustainabilityTransportWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "str") -> None:
        """Sets the reference_value of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        reference_value: str
            The reference_value of this CommonSustainabilityTransportWithSustainability.
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
        if issubclass(CommonSustainabilityTransportWithSustainability, dict):
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
        if not isinstance(other, CommonSustainabilityTransportWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
