# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import (TYPE_CHECKING, Any, BinaryIO, Dict, List,  # noqa: F401
                    Optional, Union)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    import pathlib
    from datetime import datetime

    from . import *


class CommonSustainabilityPartWithSustainability(ModelBase):
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
    swagger_types: Dict[str, str] = {
        "climate_change": "CommonValueWithUnit",
        "embodied_energy": "CommonValueWithUnit",
        "external_identity": "str",
        "id": "str",
        "input_part_number": "str",
        "materials": "list[CommonSustainabilityMaterialWithSustainability]",
        "name": "str",
        "parts": "list[CommonSustainabilityPartWithSustainability]",
        "processes": "list[CommonSustainabilityProcessWithSustainability]",
        "reference_type": "str",
        "reference_value": "str",
        "reported_mass": "CommonValueWithUnit",
    }

    attribute_map: Dict[str, str] = {
        "climate_change": "ClimateChange",
        "embodied_energy": "EmbodiedEnergy",
        "external_identity": "ExternalIdentity",
        "id": "Id",
        "input_part_number": "InputPartNumber",
        "materials": "Materials",
        "name": "Name",
        "parts": "Parts",
        "processes": "Processes",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "reported_mass": "ReportedMass",
    }

    subtype_mapping: Dict[str, str] = {
        "Parts": "CommonSustainabilityPartWithSustainability",
        "Materials": "CommonSustainabilityMaterialWithSustainability",
        "Processes": "CommonSustainabilityProcessWithSustainability",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
        "ReportedMass": "CommonValueWithUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        climate_change: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        embodied_energy: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        external_identity: "Union[str, Unset_Type]" = Unset,
        id: "Union[str, Unset_Type]" = Unset,
        input_part_number: "Union[str, Unset_Type]" = Unset,
        materials: "Union[List[CommonSustainabilityMaterialWithSustainability], Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        parts: "Union[List[CommonSustainabilityPartWithSustainability], Unset_Type]" = Unset,
        processes: "Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]" = Unset,
        reference_type: "Union[str, Unset_Type]" = Unset,
        reference_value: "Union[str, Unset_Type]" = Unset,
        reported_mass: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityPartWithSustainability - a model defined in Swagger

        Parameters
        ----------
        climate_change: CommonValueWithUnit, optional
        embodied_energy: CommonValueWithUnit, optional
        external_identity: str, optional
        id: str, optional
        input_part_number: str, optional
        materials: List[CommonSustainabilityMaterialWithSustainability], optional
        name: str, optional
        parts: List[CommonSustainabilityPartWithSustainability], optional
        processes: List[CommonSustainabilityProcessWithSustainability], optional
        reference_type: str, optional
        reference_value: str, optional
        reported_mass: CommonValueWithUnit, optional
        """
        self._parts: Union[
            List[CommonSustainabilityPartWithSustainability], Unset_Type
        ] = Unset
        self._materials: Union[
            List[CommonSustainabilityMaterialWithSustainability], Unset_Type
        ] = Unset
        self._processes: Union[
            List[CommonSustainabilityProcessWithSustainability], Unset_Type
        ] = Unset
        self._embodied_energy: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._climate_change: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._reported_mass: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._input_part_number: Union[str, Unset_Type] = Unset
        self._external_identity: Union[str, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._reference_type: Union[str, Unset_Type] = Unset
        self._reference_value: Union[str, Unset_Type] = Unset
        self._id: Union[str, Unset_Type] = Unset

        if parts is not Unset:
            self.parts = parts
        if materials is not Unset:
            self.materials = materials
        if processes is not Unset:
            self.processes = processes
        if embodied_energy is not Unset:
            self.embodied_energy = embodied_energy
        if climate_change is not Unset:
            self.climate_change = climate_change
        if reported_mass is not Unset:
            self.reported_mass = reported_mass
        if input_part_number is not Unset:
            self.input_part_number = input_part_number
        if external_identity is not Unset:
            self.external_identity = external_identity
        if name is not Unset:
            self.name = name
        if reference_type is not Unset:
            self.reference_type = reference_type
        if reference_value is not Unset:
            self.reference_value = reference_value
        if id is not Unset:
            self.id = id

    @property
    def parts(
        self,
    ) -> "Union[List[CommonSustainabilityPartWithSustainability], Unset_Type]":
        """Gets the parts of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[List[CommonSustainabilityPartWithSustainability], Unset_Type]
            The parts of this CommonSustainabilityPartWithSustainability.
        """
        return self._parts

    @parts.setter
    def parts(
        self,
        parts: "Union[List[CommonSustainabilityPartWithSustainability], Unset_Type]",
    ) -> None:
        """Sets the parts of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        parts: Union[List[CommonSustainabilityPartWithSustainability], Unset_Type]
            The parts of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if parts is None:
            raise ValueError("Invalid value for 'parts', must not be 'None'")
        self._parts = parts

    @property
    def materials(
        self,
    ) -> "Union[List[CommonSustainabilityMaterialWithSustainability], Unset_Type]":
        """Gets the materials of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[List[CommonSustainabilityMaterialWithSustainability], Unset_Type]
            The materials of this CommonSustainabilityPartWithSustainability.
        """
        return self._materials

    @materials.setter
    def materials(
        self,
        materials: "Union[List[CommonSustainabilityMaterialWithSustainability], Unset_Type]",
    ) -> None:
        """Sets the materials of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        materials: Union[List[CommonSustainabilityMaterialWithSustainability], Unset_Type]
            The materials of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if materials is None:
            raise ValueError("Invalid value for 'materials', must not be 'None'")
        self._materials = materials

    @property
    def processes(
        self,
    ) -> "Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]":
        """Gets the processes of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]
            The processes of this CommonSustainabilityPartWithSustainability.
        """
        return self._processes

    @processes.setter
    def processes(
        self,
        processes: "Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]",
    ) -> None:
        """Sets the processes of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        processes: Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]
            The processes of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if processes is None:
            raise ValueError("Invalid value for 'processes', must not be 'None'")
        self._processes = processes

    @property
    def embodied_energy(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the embodied_energy of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityPartWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(
        self, embodied_energy: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the embodied_energy of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        embodied_energy: Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if embodied_energy is None:
            raise ValueError("Invalid value for 'embodied_energy', must not be 'None'")
        self._embodied_energy = embodied_energy

    @property
    def climate_change(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the climate_change of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityPartWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(
        self, climate_change: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the climate_change of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        climate_change: Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if climate_change is None:
            raise ValueError("Invalid value for 'climate_change', must not be 'None'")
        self._climate_change = climate_change

    @property
    def reported_mass(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the reported_mass of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The reported_mass of this CommonSustainabilityPartWithSustainability.
        """
        return self._reported_mass

    @reported_mass.setter
    def reported_mass(
        self, reported_mass: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the reported_mass of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        reported_mass: Union[CommonValueWithUnit, Unset_Type]
            The reported_mass of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if reported_mass is None:
            raise ValueError("Invalid value for 'reported_mass', must not be 'None'")
        self._reported_mass = reported_mass

    @property
    def input_part_number(self) -> "Union[str, Unset_Type]":
        """Gets the input_part_number of this CommonSustainabilityPartWithSustainability.
        This is set to the value of the PartNumber element in the input BoM.

        Returns
        -------
        Union[str, Unset_Type]
            The input_part_number of this CommonSustainabilityPartWithSustainability.
        """
        return self._input_part_number

    @input_part_number.setter
    def input_part_number(self, input_part_number: "Union[str, Unset_Type]") -> None:
        """Sets the input_part_number of this CommonSustainabilityPartWithSustainability.
        This is set to the value of the PartNumber element in the input BoM.

        Parameters
        ----------
        input_part_number: Union[str, Unset_Type]
            The input_part_number of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if input_part_number is None:
            raise ValueError(
                "Invalid value for 'input_part_number', must not be 'None'"
            )
        self._input_part_number = input_part_number

    @property
    def external_identity(self) -> "Union[str, Unset_Type]":
        """Gets the external_identity of this CommonSustainabilityPartWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, Unset_Type]
            The external_identity of this CommonSustainabilityPartWithSustainability.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "Union[str, Unset_Type]") -> None:
        """Sets the external_identity of this CommonSustainabilityPartWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: Union[str, Unset_Type]
            The external_identity of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if external_identity is None:
            raise ValueError(
                "Invalid value for 'external_identity', must not be 'None'"
            )
        self._external_identity = external_identity

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this CommonSustainabilityPartWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this CommonSustainabilityPartWithSustainability.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this CommonSustainabilityPartWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def reference_type(self) -> "Union[str, Unset_Type]":
        """Gets the reference_type of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_type of this CommonSustainabilityPartWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "Union[str, Unset_Type]") -> None:
        """Sets the reference_type of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        reference_type: Union[str, Unset_Type]
            The reference_type of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if reference_type is None:
            raise ValueError("Invalid value for 'reference_type', must not be 'None'")
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "Union[str, Unset_Type]":
        """Gets the reference_value of this CommonSustainabilityPartWithSustainability.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_value of this CommonSustainabilityPartWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "Union[str, Unset_Type]") -> None:
        """Sets the reference_value of this CommonSustainabilityPartWithSustainability.

        Parameters
        ----------
        reference_value: Union[str, Unset_Type]
            The reference_value of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if reference_value is None:
            raise ValueError("Invalid value for 'reference_value', must not be 'None'")
        self._reference_value = reference_value

    @property
    def id(self) -> "Union[str, Unset_Type]":
        """Gets the id of this CommonSustainabilityPartWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        Union[str, Unset_Type]
            The id of this CommonSustainabilityPartWithSustainability.
        """
        return self._id

    @id.setter
    def id(self, id: "Union[str, Unset_Type]") -> None:
        """Sets the id of this CommonSustainabilityPartWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: Union[str, Unset_Type]
            The id of this CommonSustainabilityPartWithSustainability.
        """
        # Field is not nullable
        if id is None:
            raise ValueError("Invalid value for 'id', must not be 'None'")
        self._id = id

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, CommonSustainabilityPartWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
