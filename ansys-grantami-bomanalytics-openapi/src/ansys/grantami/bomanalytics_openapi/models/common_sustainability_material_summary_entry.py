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


class CommonSustainabilityMaterialSummaryEntry(ModelBase):
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
        "identity": "str",
        "record_reference": "CommonMaterialReference",
        "embodied_energy": "CommonValueWithUnit",
        "embodied_energy_percentage": "float",
        "climate_change": "CommonValueWithUnit",
        "climate_change_percentage": "float",
        "mass_before_processing": "CommonValueWithUnit",
        "mass_after_processing": "CommonValueWithUnit",
        "largest_contributors": "list[CommonSustainabilityMaterialContributingComponent]",
    }

    attribute_map = {
        "identity": "Identity",
        "record_reference": "RecordReference",
        "embodied_energy": "EmbodiedEnergy",
        "embodied_energy_percentage": "EmbodiedEnergyPercentage",
        "climate_change": "ClimateChange",
        "climate_change_percentage": "ClimateChangePercentage",
        "mass_before_processing": "MassBeforeProcessing",
        "mass_after_processing": "MassAfterProcessing",
        "largest_contributors": "LargestContributors",
    }

    subtype_mapping = {
        "RecordReference": "CommonMaterialReference",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
        "MassBeforeProcessing": "CommonValueWithUnit",
        "MassAfterProcessing": "CommonValueWithUnit",
        "LargestContributors": "CommonSustainabilityMaterialContributingComponent",
    }

    def __init__(
        self,
        *,
        climate_change: "Optional[CommonValueWithUnit]" = None,
        climate_change_percentage: "Optional[float]" = None,
        embodied_energy: "Optional[CommonValueWithUnit]" = None,
        embodied_energy_percentage: "Optional[float]" = None,
        identity: "Optional[str]" = None,
        largest_contributors: "Optional[List[CommonSustainabilityMaterialContributingComponent]]" = None,
        mass_after_processing: "Optional[GrantaBomAnalyticsServicesImplementationCommonValueWithUnit]" = None,
        mass_before_processing: "Optional[GrantaBomAnalyticsServicesImplementationCommonValueWithUnit]" = None,
        name: "Optional[str]" = None,
        record_reference: "Optional[CommonMaterialReference]" = None
    ) -> None:
        """CommonSustainabilityMaterialSummaryEntry - a model defined in Swagger

        Parameters
        ----------
            climate_change: CommonValueWithUnit, optional
            climate_change_percentage: float, optional
            embodied_energy: CommonValueWithUnit, optional
            embodied_energy_percentage: float, optional
            identity: str, optional
            largest_contributors: List[CommonSustainabilityMaterialContributingComponent], optional
            mass_after_processing: CommonValueWithUnit, optional
            mass_before_processing: CommonValueWithUnit, optional
            record_reference: CommonMaterialReference, optional
        """
        self._identity = None
        self._record_reference = None
        self._embodied_energy = None
        self._embodied_energy_percentage = None
        self._climate_change = None
        self._climate_change_percentage = None
        self._mass_before_processing = None
        self._mass_after_processing = None
        self._largest_contributors = None
        self.discriminator = None
        if identity is not None:
            self.identity = identity
        if record_reference is not None:
            self.record_reference = record_reference
        if embodied_energy is not None:
            self.embodied_energy = embodied_energy
        if embodied_energy_percentage is not None:
            self.embodied_energy_percentage = embodied_energy_percentage
        if climate_change is not None:
            self.climate_change = climate_change
        if climate_change_percentage is not None:
            self.climate_change_percentage = climate_change_percentage
        if mass_before_processing is not None:
            self.mass_before_processing = mass_before_processing
        if mass_after_processing is not None:
            self.mass_after_processing = mass_after_processing
        if largest_contributors is not None:
            self.largest_contributors = largest_contributors

    @property
    def identity(self) -> "str":
        """Gets the identity of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        str
            The identity of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "str") -> None:
        """Sets the identity of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        identity: str
            The identity of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._identity = identity

    @property
    def record_reference(self) -> "CommonMaterialReference":
        """Gets the record_reference of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        CommonMaterialReference
            The record_reference of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._record_reference

    @record_reference.setter
    def record_reference(self, record_reference: "CommonMaterialReference") -> None:
        """Sets the record_reference of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        record_reference: CommonMaterialReference
            The record_reference of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._record_reference = record_reference

    @property
    def embodied_energy(self) -> "CommonValueWithUnit":
        """Gets the embodied_energy of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "CommonValueWithUnit") -> None:
        """Sets the embodied_energy of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        embodied_energy: CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._embodied_energy = embodied_energy

    @property
    def embodied_energy_percentage(self) -> "float":
        """Gets the embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        float
            The embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._embodied_energy_percentage

    @embodied_energy_percentage.setter
    def embodied_energy_percentage(self, embodied_energy_percentage: "float") -> None:
        """Sets the embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        embodied_energy_percentage: float
            The embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._embodied_energy_percentage = embodied_energy_percentage

    @property
    def climate_change(self) -> "CommonValueWithUnit":
        """Gets the climate_change of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The climate_change of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "CommonValueWithUnit") -> None:
        """Sets the climate_change of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        climate_change: CommonValueWithUnit
            The climate_change of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._climate_change = climate_change

    @property
    def climate_change_percentage(self) -> "float":
        """Gets the climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        float
            The climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._climate_change_percentage

    @climate_change_percentage.setter
    def climate_change_percentage(self, climate_change_percentage: "float") -> None:
        """Sets the climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        climate_change_percentage: float
            The climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._climate_change_percentage = climate_change_percentage

    @property
    def mass_before_processing(self) -> "CommonValueWithUnit":
        """Gets the mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._mass_before_processing

    @mass_before_processing.setter
    def mass_before_processing(
        self, mass_before_processing: "CommonValueWithUnit"
    ) -> None:
        """Sets the mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        mass_before_processing: CommonValueWithUnit
            The mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._mass_before_processing = mass_before_processing

    @property
    def mass_after_processing(self) -> "CommonValueWithUnit":
        """Gets the mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        CommonValueWithUnit
            The mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._mass_after_processing

    @mass_after_processing.setter
    def mass_after_processing(
        self, mass_after_processing: "CommonValueWithUnit"
    ) -> None:
        """Sets the mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        mass_after_processing: CommonValueWithUnit
            The mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._mass_after_processing = mass_after_processing

    @property
    def largest_contributors(
        self,
    ) -> "list[CommonSustainabilityMaterialContributingComponent]":
        """Gets the largest_contributors of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        list[CommonSustainabilityMaterialContributingComponent]
            The largest_contributors of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._largest_contributors

    @largest_contributors.setter
    def largest_contributors(
        self,
        largest_contributors: "list[CommonSustainabilityMaterialContributingComponent]",
    ) -> None:
        """Sets the largest_contributors of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        largest_contributors: list[CommonSustainabilityMaterialContributingComponent]
            The largest_contributors of this CommonSustainabilityMaterialSummaryEntry.
        """
        self._largest_contributors = largest_contributors

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
        if issubclass(CommonSustainabilityMaterialSummaryEntry, dict):
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
        if not isinstance(other, CommonSustainabilityMaterialSummaryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
