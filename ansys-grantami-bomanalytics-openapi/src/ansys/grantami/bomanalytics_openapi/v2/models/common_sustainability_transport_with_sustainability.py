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


class CommonSustainabilityTransportWithSustainability(ModelBase):
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
        "embodied_energy": "CommonValueWithUnit",
        "id": "str",
        "reference_type": "str",
        "reference_value": "str",
        "stage_name": "str",
    }

    attribute_map: dict[str, str] = {
        "climate_change": "ClimateChange",
        "embodied_energy": "EmbodiedEnergy",
        "id": "Id",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "stage_name": "StageName",
    }

    subtype_mapping: dict[str, str] = {
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        climate_change: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        embodied_energy: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        id: "Union[str, None, Unset_Type]" = Unset,
        reference_type: "Union[str, None, Unset_Type]" = Unset,
        reference_value: "Union[str, None, Unset_Type]" = Unset,
        stage_name: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityTransportWithSustainability - a model defined in Swagger

        Parameters
        ----------
        climate_change: CommonValueWithUnit, optional
        embodied_energy: CommonValueWithUnit, optional
        id: str, optional
        reference_type: str, optional
        reference_value: str, optional
        stage_name: str, optional
        """
        self._stage_name: Union[str, None, Unset_Type] = Unset
        self._embodied_energy: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._climate_change: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._reference_type: Union[str, None, Unset_Type] = Unset
        self._reference_value: Union[str, None, Unset_Type] = Unset
        self._id: Union[str, None, Unset_Type] = Unset

        if stage_name is not Unset:
            self.stage_name = stage_name
        if embodied_energy is not Unset:
            self.embodied_energy = embodied_energy
        if climate_change is not Unset:
            self.climate_change = climate_change
        if reference_type is not Unset:
            self.reference_type = reference_type
        if reference_value is not Unset:
            self.reference_value = reference_value
        if id is not Unset:
            self.id = id

    @property
    def stage_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the stage_name of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        Union[str, None, Unset_Type]
            The stage_name of this CommonSustainabilityTransportWithSustainability.
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the stage_name of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        stage_name: Union[str, None, Unset_Type]
            The stage_name of this CommonSustainabilityTransportWithSustainability.
        """
        self._stage_name = stage_name

    @property
    def embodied_energy(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the embodied_energy of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityTransportWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the embodied_energy of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        embodied_energy: Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityTransportWithSustainability.
        """
        # Field is not nullable
        if embodied_energy is None:
            raise ValueError("Invalid value for 'embodied_energy', must not be 'None'")
        self._embodied_energy = embodied_energy

    @property
    def climate_change(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the climate_change of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityTransportWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "Union[CommonValueWithUnit, Unset_Type]") -> None:
        """Sets the climate_change of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        climate_change: Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityTransportWithSustainability.
        """
        # Field is not nullable
        if climate_change is None:
            raise ValueError("Invalid value for 'climate_change', must not be 'None'")
        self._climate_change = climate_change

    @property
    def reference_type(self) -> "Union[str, None, Unset_Type]":
        """Gets the reference_type of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        Union[str, None, Unset_Type]
            The reference_type of this CommonSustainabilityTransportWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "Union[str, None, Unset_Type]") -> None:
        """Sets the reference_type of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        reference_type: Union[str, None, Unset_Type]
            The reference_type of this CommonSustainabilityTransportWithSustainability.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "Union[str, None, Unset_Type]":
        """Gets the reference_value of this CommonSustainabilityTransportWithSustainability.

        Returns
        -------
        Union[str, None, Unset_Type]
            The reference_value of this CommonSustainabilityTransportWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "Union[str, None, Unset_Type]") -> None:
        """Sets the reference_value of this CommonSustainabilityTransportWithSustainability.

        Parameters
        ----------
        reference_value: Union[str, None, Unset_Type]
            The reference_value of this CommonSustainabilityTransportWithSustainability.
        """
        self._reference_value = reference_value

    @property
    def id(self) -> "Union[str, None, Unset_Type]":
        """Gets the id of this CommonSustainabilityTransportWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        Union[str, None, Unset_Type]
            The id of this CommonSustainabilityTransportWithSustainability.
        """
        return self._id

    @id.setter
    def id(self, id: "Union[str, None, Unset_Type]") -> None:
        """Sets the id of this CommonSustainabilityTransportWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: Union[str, None, Unset_Type]
            The id of this CommonSustainabilityTransportWithSustainability.
        """
        self._id = id

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
        if not isinstance(other, CommonSustainabilityTransportWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
