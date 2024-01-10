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


class CommonSustainabilityTransportSummaryEntry(ModelBase):
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

    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "climate_change": "CommonValueWithUnit",
        "climate_change_percentage": "float",
        "distance": "CommonValueWithUnit",
        "embodied_energy": "CommonValueWithUnit",
        "embodied_energy_percentage": "float",
        "record_reference": "CommonTransportReference",
        "stage_name": "str",
    }

    attribute_map = {
        "climate_change": "ClimateChange",
        "climate_change_percentage": "ClimateChangePercentage",
        "distance": "Distance",
        "embodied_energy": "EmbodiedEnergy",
        "embodied_energy_percentage": "EmbodiedEnergyPercentage",
        "record_reference": "RecordReference",
        "stage_name": "StageName",
    }

    subtype_mapping = {
        "RecordReference": "CommonTransportReference",
        "Distance": "CommonValueWithUnit",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
    }

    discriminator = None

    def __init__(
        self,
        *,
        climate_change: "Optional[CommonValueWithUnit]" = None,
        climate_change_percentage: "Optional[float]" = None,
        distance: "Optional[CommonValueWithUnit]" = None,
        embodied_energy: "Optional[CommonValueWithUnit]" = None,
        embodied_energy_percentage: "Optional[float]" = None,
        record_reference: "Optional[CommonTransportReference]" = None,
        stage_name: "Optional[str]" = None,
    ) -> None:
        """CommonSustainabilityTransportSummaryEntry - a model defined in Swagger

        Parameters
        ----------
            climate_change: CommonValueWithUnit, optional
            climate_change_percentage: float, optional
            distance: CommonValueWithUnit, optional
            embodied_energy: CommonValueWithUnit, optional
            embodied_energy_percentage: float, optional
            record_reference: CommonTransportReference, optional
            stage_name: str, optional
        """
        self._stage_name = None
        self._record_reference = None
        self._distance = None
        self._embodied_energy = None
        self._embodied_energy_percentage = None
        self._climate_change = None
        self._climate_change_percentage = None

        if stage_name is not None:
            self.stage_name = stage_name
        if record_reference is not None:
            self.record_reference = record_reference
        if distance is not None:
            self.distance = distance
        if embodied_energy is not None:
            self.embodied_energy = embodied_energy
        if embodied_energy_percentage is not None:
            self.embodied_energy_percentage = embodied_energy_percentage
        if climate_change is not None:
            self.climate_change = climate_change
        if climate_change_percentage is not None:
            self.climate_change_percentage = climate_change_percentage

    @property
    def stage_name(self) -> "str":
        """Gets the stage_name of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        str
            The stage_name of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name: "str") -> None:
        """Sets the stage_name of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        stage_name: str
            The stage_name of this CommonSustainabilityTransportSummaryEntry.
        """
        self._stage_name = stage_name

    @property
    def record_reference(self) -> "CommonTransportReference":
        """Gets the record_reference of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        CommonTransportReference
            The record_reference of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._record_reference

    @record_reference.setter
    def record_reference(self, record_reference: "CommonTransportReference") -> None:
        """Sets the record_reference of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        record_reference: CommonTransportReference
            The record_reference of this CommonSustainabilityTransportSummaryEntry.
        """
        self._record_reference = record_reference

    @property
    def distance(self) -> "CommonValueWithUnit":
        """Gets the distance of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The distance of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._distance

    @distance.setter
    def distance(self, distance: "CommonValueWithUnit") -> None:
        """Sets the distance of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        distance: CommonValueWithUnit
            The distance of this CommonSustainabilityTransportSummaryEntry.
        """
        self._distance = distance

    @property
    def embodied_energy(self) -> "CommonValueWithUnit":
        """Gets the embodied_energy of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "CommonValueWithUnit") -> None:
        """Sets the embodied_energy of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        embodied_energy: CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityTransportSummaryEntry.
        """
        self._embodied_energy = embodied_energy

    @property
    def embodied_energy_percentage(self) -> "float":
        """Gets the embodied_energy_percentage of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        float
            The embodied_energy_percentage of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._embodied_energy_percentage

    @embodied_energy_percentage.setter
    def embodied_energy_percentage(self, embodied_energy_percentage: "float") -> None:
        """Sets the embodied_energy_percentage of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        embodied_energy_percentage: float
            The embodied_energy_percentage of this CommonSustainabilityTransportSummaryEntry.
        """
        self._embodied_energy_percentage = embodied_energy_percentage

    @property
    def climate_change(self) -> "CommonValueWithUnit":
        """Gets the climate_change of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The climate_change of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "CommonValueWithUnit") -> None:
        """Sets the climate_change of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        climate_change: CommonValueWithUnit
            The climate_change of this CommonSustainabilityTransportSummaryEntry.
        """
        self._climate_change = climate_change

    @property
    def climate_change_percentage(self) -> "float":
        """Gets the climate_change_percentage of this CommonSustainabilityTransportSummaryEntry.

        Returns
        -------
        float
            The climate_change_percentage of this CommonSustainabilityTransportSummaryEntry.
        """
        return self._climate_change_percentage

    @climate_change_percentage.setter
    def climate_change_percentage(self, climate_change_percentage: "float") -> None:
        """Sets the climate_change_percentage of this CommonSustainabilityTransportSummaryEntry.

        Parameters
        ----------
        climate_change_percentage: float
            The climate_change_percentage of this CommonSustainabilityTransportSummaryEntry.
        """
        self._climate_change_percentage = climate_change_percentage

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
        if issubclass(CommonSustainabilityTransportSummaryEntry, dict):
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
        if not isinstance(other, CommonSustainabilityTransportSummaryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other