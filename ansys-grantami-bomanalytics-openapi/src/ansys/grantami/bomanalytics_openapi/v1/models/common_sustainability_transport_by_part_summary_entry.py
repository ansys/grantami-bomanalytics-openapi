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
Granta.BomAnalyticsServices.V1

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


class CommonSustainabilityTransportByPartSummaryEntry(ModelBase):
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
        "category": "str",
        "climate_change": "CommonValueWithUnit",
        "climate_change_percentage": "float",
        "distance": "CommonValueWithUnit",
        "embodied_energy": "CommonValueWithUnit",
        "embodied_energy_percentage": "float",
        "parent_part_name": "str",
        "part_name": "str",
        "transport_types": "list[str]",
    }

    attribute_map: dict[str, str] = {
        "category": "Category",
        "climate_change": "ClimateChange",
        "climate_change_percentage": "ClimateChangePercentage",
        "distance": "Distance",
        "embodied_energy": "EmbodiedEnergy",
        "embodied_energy_percentage": "EmbodiedEnergyPercentage",
        "parent_part_name": "ParentPartName",
        "part_name": "PartName",
        "transport_types": "TransportTypes",
    }

    subtype_mapping: dict[str, str] = {
        "Distance": "CommonValueWithUnit",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        category: "Union[str, Unset_Type]" = Unset,
        climate_change: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        climate_change_percentage: "Union[float, Unset_Type]" = Unset,
        distance: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        embodied_energy: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        embodied_energy_percentage: "Union[float, Unset_Type]" = Unset,
        parent_part_name: "Union[str, Unset_Type]" = Unset,
        part_name: "Union[str, Unset_Type]" = Unset,
        transport_types: "Union[list[str], Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityTransportByPartSummaryEntry - a model defined in Swagger

        Parameters
        ----------
        category: str, optional
        climate_change: CommonValueWithUnit, optional
        climate_change_percentage: float, optional
        distance: CommonValueWithUnit, optional
        embodied_energy: CommonValueWithUnit, optional
        embodied_energy_percentage: float, optional
        parent_part_name: str, optional
        part_name: str, optional
        transport_types: list[str], optional
        """
        self._parent_part_name: Union[str, Unset_Type] = Unset
        self._part_name: Union[str, Unset_Type] = Unset
        self._category: Union[str, Unset_Type] = Unset
        self._transport_types: Union[list[str], Unset_Type] = Unset
        self._distance: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._embodied_energy: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._embodied_energy_percentage: Union[float, Unset_Type] = Unset
        self._climate_change: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._climate_change_percentage: Union[float, Unset_Type] = Unset

        if parent_part_name is not Unset:
            self.parent_part_name = parent_part_name
        if part_name is not Unset:
            self.part_name = part_name
        if category is not Unset:
            self.category = category
        if transport_types is not Unset:
            self.transport_types = transport_types
        if distance is not Unset:
            self.distance = distance
        if embodied_energy is not Unset:
            self.embodied_energy = embodied_energy
        if embodied_energy_percentage is not Unset:
            self.embodied_energy_percentage = embodied_energy_percentage
        if climate_change is not Unset:
            self.climate_change = climate_change
        if climate_change_percentage is not Unset:
            self.climate_change_percentage = climate_change_percentage

    @property
    def parent_part_name(self) -> "Union[str, Unset_Type]":
        """Gets the parent_part_name of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[str, Unset_Type]
            The parent_part_name of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._parent_part_name

    @parent_part_name.setter
    def parent_part_name(self, parent_part_name: "Union[str, Unset_Type]") -> None:
        """Sets the parent_part_name of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        parent_part_name: Union[str, Unset_Type]
            The parent_part_name of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if parent_part_name is None:
            raise ValueError("Invalid value for 'parent_part_name', must not be 'None'")
        self._parent_part_name = parent_part_name

    @property
    def part_name(self) -> "Union[str, Unset_Type]":
        """Gets the part_name of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[str, Unset_Type]
            The part_name of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._part_name

    @part_name.setter
    def part_name(self, part_name: "Union[str, Unset_Type]") -> None:
        """Sets the part_name of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        part_name: Union[str, Unset_Type]
            The part_name of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if part_name is None:
            raise ValueError("Invalid value for 'part_name', must not be 'None'")
        self._part_name = part_name

    @property
    def category(self) -> "Union[str, Unset_Type]":
        """Gets the category of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[str, Unset_Type]
            The category of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._category

    @category.setter
    def category(self, category: "Union[str, Unset_Type]") -> None:
        """Sets the category of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        category: Union[str, Unset_Type]
            The category of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if category is None:
            raise ValueError("Invalid value for 'category', must not be 'None'")
        self._category = category

    @property
    def transport_types(self) -> "Union[list[str], Unset_Type]":
        """Gets the transport_types of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[list[str], Unset_Type]
            The transport_types of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._transport_types

    @transport_types.setter
    def transport_types(self, transport_types: "Union[list[str], Unset_Type]") -> None:
        """Sets the transport_types of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        transport_types: Union[list[str], Unset_Type]
            The transport_types of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if transport_types is None:
            raise ValueError("Invalid value for 'transport_types', must not be 'None'")
        self._transport_types = transport_types

    @property
    def distance(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the distance of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The distance of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._distance

    @distance.setter
    def distance(self, distance: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the distance of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        distance: Union[CommonValueWithUnit, Unset_Type]
            The distance of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if distance is None:
            raise ValueError("Invalid value for 'distance', must not be 'None'")
        self._distance = distance

    @property
    def embodied_energy(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the embodied_energy of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the embodied_energy of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        embodied_energy: Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if embodied_energy is None:
            raise ValueError("Invalid value for 'embodied_energy', must not be 'None'")
        self._embodied_energy = embodied_energy

    @property
    def embodied_energy_percentage(self) -> "Union[float, Unset_Type]":
        """Gets the embodied_energy_percentage of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[float, Unset_Type]
            The embodied_energy_percentage of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._embodied_energy_percentage

    @embodied_energy_percentage.setter
    def embodied_energy_percentage(
        self, embodied_energy_percentage: "Union[float, Unset_Type]"
    ) -> None:
        """Sets the embodied_energy_percentage of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        embodied_energy_percentage: Union[float, Unset_Type]
            The embodied_energy_percentage of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if embodied_energy_percentage is None:
            raise ValueError("Invalid value for 'embodied_energy_percentage', must not be 'None'")
        self._embodied_energy_percentage = embodied_energy_percentage

    @property
    def climate_change(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the climate_change of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the climate_change of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        climate_change: Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if climate_change is None:
            raise ValueError("Invalid value for 'climate_change', must not be 'None'")
        self._climate_change = climate_change

    @property
    def climate_change_percentage(self) -> "Union[float, Unset_Type]":
        """Gets the climate_change_percentage of this CommonSustainabilityTransportByPartSummaryEntry.

        Returns
        -------
        Union[float, Unset_Type]
            The climate_change_percentage of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        return self._climate_change_percentage

    @climate_change_percentage.setter
    def climate_change_percentage(
        self, climate_change_percentage: "Union[float, Unset_Type]"
    ) -> None:
        """Sets the climate_change_percentage of this CommonSustainabilityTransportByPartSummaryEntry.

        Parameters
        ----------
        climate_change_percentage: Union[float, Unset_Type]
            The climate_change_percentage of this CommonSustainabilityTransportByPartSummaryEntry.
        """
        # Field is not nullable
        if climate_change_percentage is None:
            raise ValueError("Invalid value for 'climate_change_percentage', must not be 'None'")
        self._climate_change_percentage = climate_change_percentage

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
        if not isinstance(other, CommonSustainabilityTransportByPartSummaryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
