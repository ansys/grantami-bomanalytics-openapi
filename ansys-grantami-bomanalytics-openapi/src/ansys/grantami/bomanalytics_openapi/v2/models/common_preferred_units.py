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


class CommonPreferredUnits(ModelBase):
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
        "distance_unit": "str",
        "energy_unit": "str",
        "mass_unit": "str",
    }

    attribute_map: dict[str, str] = {
        "distance_unit": "DistanceUnit",
        "energy_unit": "EnergyUnit",
        "mass_unit": "MassUnit",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        distance_unit: "Union[str, None, Unset_Type]" = Unset,
        energy_unit: "Union[str, None, Unset_Type]" = Unset,
        mass_unit: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """CommonPreferredUnits - a model defined in Swagger

        Parameters
        ----------
        distance_unit: str, optional
        energy_unit: str, optional
        mass_unit: str, optional
        """
        self._mass_unit: Union[str, None, Unset_Type] = Unset
        self._energy_unit: Union[str, None, Unset_Type] = Unset
        self._distance_unit: Union[str, None, Unset_Type] = Unset

        if mass_unit is not Unset:
            self.mass_unit = mass_unit
        if energy_unit is not Unset:
            self.energy_unit = energy_unit
        if distance_unit is not Unset:
            self.distance_unit = distance_unit

    @property
    def mass_unit(self) -> "Union[str, None, Unset_Type]":
        """Gets the mass_unit of this CommonPreferredUnits.

        Returns
        -------
        Union[str, None, Unset_Type]
            The mass_unit of this CommonPreferredUnits.
        """
        return self._mass_unit

    @mass_unit.setter
    def mass_unit(self, mass_unit: "Union[str, None, Unset_Type]") -> None:
        """Sets the mass_unit of this CommonPreferredUnits.

        Parameters
        ----------
        mass_unit: Union[str, None, Unset_Type]
            The mass_unit of this CommonPreferredUnits.
        """
        self._mass_unit = mass_unit

    @property
    def energy_unit(self) -> "Union[str, None, Unset_Type]":
        """Gets the energy_unit of this CommonPreferredUnits.

        Returns
        -------
        Union[str, None, Unset_Type]
            The energy_unit of this CommonPreferredUnits.
        """
        return self._energy_unit

    @energy_unit.setter
    def energy_unit(self, energy_unit: "Union[str, None, Unset_Type]") -> None:
        """Sets the energy_unit of this CommonPreferredUnits.

        Parameters
        ----------
        energy_unit: Union[str, None, Unset_Type]
            The energy_unit of this CommonPreferredUnits.
        """
        self._energy_unit = energy_unit

    @property
    def distance_unit(self) -> "Union[str, None, Unset_Type]":
        """Gets the distance_unit of this CommonPreferredUnits.

        Returns
        -------
        Union[str, None, Unset_Type]
            The distance_unit of this CommonPreferredUnits.
        """
        return self._distance_unit

    @distance_unit.setter
    def distance_unit(self, distance_unit: "Union[str, None, Unset_Type]") -> None:
        """Sets the distance_unit of this CommonPreferredUnits.

        Parameters
        ----------
        distance_unit: Union[str, None, Unset_Type]
            The distance_unit of this CommonPreferredUnits.
        """
        self._distance_unit = distance_unit

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
        if not isinstance(other, CommonPreferredUnits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
