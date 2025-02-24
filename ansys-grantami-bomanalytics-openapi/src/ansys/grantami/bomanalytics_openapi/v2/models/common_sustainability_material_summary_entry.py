# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Granta.BomAnalyticsServices.V2

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: V1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class CommonSustainabilityMaterialSummaryEntry(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "climate_change": "CommonValueWithUnit",
        "climate_change_percentage": "float",
        "embodied_energy": "CommonValueWithUnit",
        "embodied_energy_percentage": "float",
        "identity": "str",
        "largest_contributors": "list[CommonSustainabilityMaterialContributingComponent]",
        "mass_after_processing": "CommonValueWithUnit",
        "mass_before_processing": "CommonValueWithUnit",
        "record_reference": "CommonMaterialReference",
    }

    attribute_map: dict[str, str] = {
        "climate_change": "ClimateChange",
        "climate_change_percentage": "ClimateChangePercentage",
        "embodied_energy": "EmbodiedEnergy",
        "embodied_energy_percentage": "EmbodiedEnergyPercentage",
        "identity": "Identity",
        "largest_contributors": "LargestContributors",
        "mass_after_processing": "MassAfterProcessing",
        "mass_before_processing": "MassBeforeProcessing",
        "record_reference": "RecordReference",
    }

    subtype_mapping: dict[str, str] = {
        "RecordReference": "CommonMaterialReference",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
        "MassBeforeProcessing": "CommonValueWithUnit",
        "MassAfterProcessing": "CommonValueWithUnit",
        "LargestContributors": "CommonSustainabilityMaterialContributingComponent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        climate_change: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        climate_change_percentage: "Union[float, Unset_Type]" = Unset,
        embodied_energy: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        embodied_energy_percentage: "Union[float, Unset_Type]" = Unset,
        identity: "Union[str, Unset_Type]" = Unset,
        largest_contributors: "Union[list[CommonSustainabilityMaterialContributingComponent], Unset_Type]" = Unset,
        mass_after_processing: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        mass_before_processing: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        record_reference: "Union[CommonMaterialReference, Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityMaterialSummaryEntry - a model defined in Swagger

        Parameters
        ----------
        climate_change: CommonValueWithUnit, optional
        climate_change_percentage: float, optional
        embodied_energy: CommonValueWithUnit, optional
        embodied_energy_percentage: float, optional
        identity: str, optional
        largest_contributors: list[CommonSustainabilityMaterialContributingComponent], optional
        mass_after_processing: CommonValueWithUnit, optional
        mass_before_processing: CommonValueWithUnit, optional
        record_reference: CommonMaterialReference, optional
        """
        self._identity: Union[str, Unset_Type] = Unset
        self._record_reference: Union[CommonMaterialReference, Unset_Type] = Unset
        self._embodied_energy: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._embodied_energy_percentage: Union[float, Unset_Type] = Unset
        self._climate_change: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._climate_change_percentage: Union[float, Unset_Type] = Unset
        self._mass_before_processing: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._mass_after_processing: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._largest_contributors: Union[
            list[CommonSustainabilityMaterialContributingComponent], Unset_Type
        ] = Unset

        if identity is not Unset:
            self.identity = identity
        if record_reference is not Unset:
            self.record_reference = record_reference
        if embodied_energy is not Unset:
            self.embodied_energy = embodied_energy
        if embodied_energy_percentage is not Unset:
            self.embodied_energy_percentage = embodied_energy_percentage
        if climate_change is not Unset:
            self.climate_change = climate_change
        if climate_change_percentage is not Unset:
            self.climate_change_percentage = climate_change_percentage
        if mass_before_processing is not Unset:
            self.mass_before_processing = mass_before_processing
        if mass_after_processing is not Unset:
            self.mass_after_processing = mass_after_processing
        if largest_contributors is not Unset:
            self.largest_contributors = largest_contributors

    @property
    def identity(self) -> "Union[str, Unset_Type]":
        """Gets the identity of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[str, Unset_Type]
            The identity of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[str, Unset_Type]") -> None:
        """Sets the identity of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        identity: Union[str, Unset_Type]
            The identity of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def record_reference(self) -> "Union[CommonMaterialReference, Unset_Type]":
        """Gets the record_reference of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[CommonMaterialReference, Unset_Type]
            The record_reference of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._record_reference

    @record_reference.setter
    def record_reference(
        self, record_reference: "Union[CommonMaterialReference, Unset_Type]"
    ) -> None:
        """Sets the record_reference of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        record_reference: Union[CommonMaterialReference, Unset_Type]
            The record_reference of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if record_reference is None:
            raise ValueError("Invalid value for 'record_reference', must not be 'None'")
        self._record_reference = record_reference

    @property
    def embodied_energy(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the embodied_energy of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the embodied_energy of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        embodied_energy: Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if embodied_energy is None:
            raise ValueError("Invalid value for 'embodied_energy', must not be 'None'")
        self._embodied_energy = embodied_energy

    @property
    def embodied_energy_percentage(self) -> "Union[float, Unset_Type]":
        """Gets the embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[float, Unset_Type]
            The embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._embodied_energy_percentage

    @embodied_energy_percentage.setter
    def embodied_energy_percentage(
        self, embodied_energy_percentage: "Union[float, Unset_Type]"
    ) -> None:
        """Sets the embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        embodied_energy_percentage: Union[float, Unset_Type]
            The embodied_energy_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if embodied_energy_percentage is None:
            raise ValueError("Invalid value for 'embodied_energy_percentage', must not be 'None'")
        self._embodied_energy_percentage = embodied_energy_percentage

    @property
    def climate_change(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the climate_change of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the climate_change of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        climate_change: Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if climate_change is None:
            raise ValueError("Invalid value for 'climate_change', must not be 'None'")
        self._climate_change = climate_change

    @property
    def climate_change_percentage(self) -> "Union[float, Unset_Type]":
        """Gets the climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[float, Unset_Type]
            The climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._climate_change_percentage

    @climate_change_percentage.setter
    def climate_change_percentage(
        self, climate_change_percentage: "Union[float, Unset_Type]"
    ) -> None:
        """Sets the climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        climate_change_percentage: Union[float, Unset_Type]
            The climate_change_percentage of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if climate_change_percentage is None:
            raise ValueError("Invalid value for 'climate_change_percentage', must not be 'None'")
        self._climate_change_percentage = climate_change_percentage

    @property
    def mass_before_processing(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._mass_before_processing

    @mass_before_processing.setter
    def mass_before_processing(
        self, mass_before_processing: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        mass_before_processing: Union[CommonValueWithUnit, Unset_Type]
            The mass_before_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if mass_before_processing is None:
            raise ValueError("Invalid value for 'mass_before_processing', must not be 'None'")
        self._mass_before_processing = mass_before_processing

    @property
    def mass_after_processing(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._mass_after_processing

    @mass_after_processing.setter
    def mass_after_processing(
        self, mass_after_processing: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        mass_after_processing: Union[CommonValueWithUnit, Unset_Type]
            The mass_after_processing of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if mass_after_processing is None:
            raise ValueError("Invalid value for 'mass_after_processing', must not be 'None'")
        self._mass_after_processing = mass_after_processing

    @property
    def largest_contributors(
        self,
    ) -> "Union[list[CommonSustainabilityMaterialContributingComponent], Unset_Type]":
        """Gets the largest_contributors of this CommonSustainabilityMaterialSummaryEntry.

        Returns
        -------
        Union[list[CommonSustainabilityMaterialContributingComponent], Unset_Type]
            The largest_contributors of this CommonSustainabilityMaterialSummaryEntry.
        """
        return self._largest_contributors

    @largest_contributors.setter
    def largest_contributors(
        self,
        largest_contributors: "Union[list[CommonSustainabilityMaterialContributingComponent], Unset_Type]",
    ) -> None:
        """Sets the largest_contributors of this CommonSustainabilityMaterialSummaryEntry.

        Parameters
        ----------
        largest_contributors: Union[list[CommonSustainabilityMaterialContributingComponent], Unset_Type]
            The largest_contributors of this CommonSustainabilityMaterialSummaryEntry.
        """
        # Field is not nullable
        if largest_contributors is None:
            raise ValueError("Invalid value for 'largest_contributors', must not be 'None'")
        self._largest_contributors = largest_contributors

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
