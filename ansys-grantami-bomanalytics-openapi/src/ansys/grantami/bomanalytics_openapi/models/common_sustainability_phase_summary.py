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


class CommonSustainabilityPhaseSummary(ModelBase):
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
        "climate_change": "CommonValueWithUnit",
        "climate_change_percentage": "float",
        "embodied_energy": "CommonValueWithUnit",
        "embodied_energy_percentage": "float",
        "phase": "str",
    }

    attribute_map = {
        "climate_change": "ClimateChange",
        "climate_change_percentage": "ClimateChangePercentage",
        "embodied_energy": "EmbodiedEnergy",
        "embodied_energy_percentage": "EmbodiedEnergyPercentage",
        "phase": "Phase",
    }

    subtype_mapping = {
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
    }

    def __init__(
        self,
        *,
        climate_change: "Optional[CommonValueWithUnit]" = None,
        climate_change_percentage: "Optional[float]" = None,
        embodied_energy: "Optional[CommonValueWithUnit]" = None,
        embodied_energy_percentage: "Optional[float]" = None,
        phase: "Optional[str]" = None,
    ) -> None:
        """CommonSustainabilityPhaseSummary - a model defined in Swagger

        Parameters
        ----------
            climate_change: CommonValueWithUnit, optional
            climate_change_percentage: float, optional
            embodied_energy: CommonValueWithUnit, optional
            embodied_energy_percentage: float, optional
            phase: str, optional
        """
        self._phase = None
        self._embodied_energy = None
        self._embodied_energy_percentage = None
        self._climate_change = None
        self._climate_change_percentage = None
        self.discriminator = None
        if phase is not None:
            self.phase = phase
        if embodied_energy is not None:
            self.embodied_energy = embodied_energy
        if embodied_energy_percentage is not None:
            self.embodied_energy_percentage = embodied_energy_percentage
        if climate_change is not None:
            self.climate_change = climate_change
        if climate_change_percentage is not None:
            self.climate_change_percentage = climate_change_percentage

    @property
    def phase(self) -> "str":
        """Gets the phase of this CommonSustainabilityPhaseSummary.

        Returns
        -------
        str
            The phase of this CommonSustainabilityPhaseSummary.
        """
        return self._phase

    @phase.setter
    def phase(self, phase: "str") -> None:
        """Sets the phase of this CommonSustainabilityPhaseSummary.

        Parameters
        ----------
        phase: str
            The phase of this CommonSustainabilityPhaseSummary.
        """
        self._phase = phase

    @property
    def embodied_energy(self) -> "CommonValueWithUnit":
        """Gets the embodied_energy of this CommonSustainabilityPhaseSummary.

        Returns
        -------
        CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityPhaseSummary.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "CommonValueWithUnit") -> None:
        """Sets the embodied_energy of this CommonSustainabilityPhaseSummary.

        Parameters
        ----------
        embodied_energy: CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityPhaseSummary.
        """
        self._embodied_energy = embodied_energy

    @property
    def embodied_energy_percentage(self) -> "float":
        """Gets the embodied_energy_percentage of this CommonSustainabilityPhaseSummary.

        Returns
        -------
        float
            The embodied_energy_percentage of this CommonSustainabilityPhaseSummary.
        """
        return self._embodied_energy_percentage

    @embodied_energy_percentage.setter
    def embodied_energy_percentage(self, embodied_energy_percentage: "float") -> None:
        """Sets the embodied_energy_percentage of this CommonSustainabilityPhaseSummary.

        Parameters
        ----------
        embodied_energy_percentage: float
            The embodied_energy_percentage of this CommonSustainabilityPhaseSummary.
        """
        self._embodied_energy_percentage = embodied_energy_percentage

    @property
    def climate_change(self) -> "CommonValueWithUnit":
        """Gets the climate_change of this CommonSustainabilityPhaseSummary.

        Returns
        -------
        CommonValueWithUnit
            The climate_change of this CommonSustainabilityPhaseSummary.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "CommonValueWithUnit") -> None:
        """Sets the climate_change of this CommonSustainabilityPhaseSummary.

        Parameters
        ----------
        climate_change: CommonValueWithUnit
            The climate_change of this CommonSustainabilityPhaseSummary.
        """
        self._climate_change = climate_change

    @property
    def climate_change_percentage(self) -> "float":
        """Gets the climate_change_percentage of this CommonSustainabilityPhaseSummary.

        Returns
        -------
        float
            The climate_change_percentage of this CommonSustainabilityPhaseSummary.
        """
        return self._climate_change_percentage

    @climate_change_percentage.setter
    def climate_change_percentage(self, climate_change_percentage: "float") -> None:
        """Sets the climate_change_percentage of this CommonSustainabilityPhaseSummary.

        Parameters
        ----------
        climate_change_percentage: float
            The climate_change_percentage of this CommonSustainabilityPhaseSummary.
        """
        self._climate_change_percentage = climate_change_percentage

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
        if issubclass(CommonSustainabilityPhaseSummary, dict):
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
        if not isinstance(other, CommonSustainabilityPhaseSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
