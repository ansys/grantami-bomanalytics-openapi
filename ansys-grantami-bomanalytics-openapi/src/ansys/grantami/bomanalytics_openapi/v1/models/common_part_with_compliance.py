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


class CommonPartWithCompliance(ModelBase):
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
        "external_identity": "str",
        "id": "str",
        "indicators": "list[CommonIndicatorResult]",
        "input_part_number": "str",
        "materials": "list[CommonMaterialWithCompliance]",
        "name": "str",
        "parts": "list[CommonPartWithCompliance]",
        "reference_type": "str",
        "reference_value": "str",
        "specifications": "list[CommonSpecificationWithCompliance]",
        "substances": "list[CommonSubstanceWithCompliance]",
    }

    attribute_map: dict[str, str] = {
        "external_identity": "ExternalIdentity",
        "id": "Id",
        "indicators": "Indicators",
        "input_part_number": "InputPartNumber",
        "materials": "Materials",
        "name": "Name",
        "parts": "Parts",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "specifications": "Specifications",
        "substances": "Substances",
    }

    subtype_mapping: dict[str, str] = {
        "Indicators": "CommonIndicatorResult",
        "Parts": "CommonPartWithCompliance",
        "Specifications": "CommonSpecificationWithCompliance",
        "Materials": "CommonMaterialWithCompliance",
        "Substances": "CommonSubstanceWithCompliance",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        external_identity: "Union[str, None, Unset_Type]" = Unset,
        id: "Union[str, None, Unset_Type]" = Unset,
        indicators: "Union[list[CommonIndicatorResult], None, Unset_Type]" = Unset,
        input_part_number: "Union[str, None, Unset_Type]" = Unset,
        materials: "Union[list[CommonMaterialWithCompliance], None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        parts: "Union[list[CommonPartWithCompliance], None, Unset_Type]" = Unset,
        reference_type: "Union[str, None, Unset_Type]" = Unset,
        reference_value: "Union[str, None, Unset_Type]" = Unset,
        specifications: "Union[list[CommonSpecificationWithCompliance], None, Unset_Type]" = Unset,
        substances: "Union[list[CommonSubstanceWithCompliance], None, Unset_Type]" = Unset,
    ) -> None:
        """CommonPartWithCompliance - a model defined in Swagger

        Parameters
        ----------
        external_identity: str, optional
        id: str, optional
        indicators: list[CommonIndicatorResult], optional
        input_part_number: str, optional
        materials: list[CommonMaterialWithCompliance], optional
        name: str, optional
        parts: list[CommonPartWithCompliance], optional
        reference_type: str, optional
        reference_value: str, optional
        specifications: list[CommonSpecificationWithCompliance], optional
        substances: list[CommonSubstanceWithCompliance], optional
        """
        self._indicators: Union[list[CommonIndicatorResult], None, Unset_Type] = Unset
        self._parts: Union[list[CommonPartWithCompliance], None, Unset_Type] = Unset
        self._specifications: Union[list[CommonSpecificationWithCompliance], None, Unset_Type] = (
            Unset
        )
        self._materials: Union[list[CommonMaterialWithCompliance], None, Unset_Type] = Unset
        self._substances: Union[list[CommonSubstanceWithCompliance], None, Unset_Type] = Unset
        self._input_part_number: Union[str, None, Unset_Type] = Unset
        self._external_identity: Union[str, None, Unset_Type] = Unset
        self._name: Union[str, None, Unset_Type] = Unset
        self._reference_type: Union[str, None, Unset_Type] = Unset
        self._reference_value: Union[str, None, Unset_Type] = Unset
        self._id: Union[str, None, Unset_Type] = Unset

        if indicators is not Unset:
            self.indicators = indicators
        if parts is not Unset:
            self.parts = parts
        if specifications is not Unset:
            self.specifications = specifications
        if materials is not Unset:
            self.materials = materials
        if substances is not Unset:
            self.substances = substances
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
    def indicators(self) -> "Union[list[CommonIndicatorResult], None, Unset_Type]":
        """Gets the indicators of this CommonPartWithCompliance.

        Returns
        -------
        Union[list[CommonIndicatorResult], None, Unset_Type]
            The indicators of this CommonPartWithCompliance.
        """
        return self._indicators

    @indicators.setter
    def indicators(
        self, indicators: "Union[list[CommonIndicatorResult], None, Unset_Type]"
    ) -> None:
        """Sets the indicators of this CommonPartWithCompliance.

        Parameters
        ----------
        indicators: Union[list[CommonIndicatorResult], None, Unset_Type]
            The indicators of this CommonPartWithCompliance.
        """
        self._indicators = indicators

    @property
    def parts(self) -> "Union[list[CommonPartWithCompliance], None, Unset_Type]":
        """Gets the parts of this CommonPartWithCompliance.

        Returns
        -------
        Union[list[CommonPartWithCompliance], None, Unset_Type]
            The parts of this CommonPartWithCompliance.
        """
        return self._parts

    @parts.setter
    def parts(self, parts: "Union[list[CommonPartWithCompliance], None, Unset_Type]") -> None:
        """Sets the parts of this CommonPartWithCompliance.

        Parameters
        ----------
        parts: Union[list[CommonPartWithCompliance], None, Unset_Type]
            The parts of this CommonPartWithCompliance.
        """
        self._parts = parts

    @property
    def specifications(self) -> "Union[list[CommonSpecificationWithCompliance], None, Unset_Type]":
        """Gets the specifications of this CommonPartWithCompliance.

        Returns
        -------
        Union[list[CommonSpecificationWithCompliance], None, Unset_Type]
            The specifications of this CommonPartWithCompliance.
        """
        return self._specifications

    @specifications.setter
    def specifications(
        self, specifications: "Union[list[CommonSpecificationWithCompliance], None, Unset_Type]"
    ) -> None:
        """Sets the specifications of this CommonPartWithCompliance.

        Parameters
        ----------
        specifications: Union[list[CommonSpecificationWithCompliance], None, Unset_Type]
            The specifications of this CommonPartWithCompliance.
        """
        self._specifications = specifications

    @property
    def materials(self) -> "Union[list[CommonMaterialWithCompliance], None, Unset_Type]":
        """Gets the materials of this CommonPartWithCompliance.

        Returns
        -------
        Union[list[CommonMaterialWithCompliance], None, Unset_Type]
            The materials of this CommonPartWithCompliance.
        """
        return self._materials

    @materials.setter
    def materials(
        self, materials: "Union[list[CommonMaterialWithCompliance], None, Unset_Type]"
    ) -> None:
        """Sets the materials of this CommonPartWithCompliance.

        Parameters
        ----------
        materials: Union[list[CommonMaterialWithCompliance], None, Unset_Type]
            The materials of this CommonPartWithCompliance.
        """
        self._materials = materials

    @property
    def substances(self) -> "Union[list[CommonSubstanceWithCompliance], None, Unset_Type]":
        """Gets the substances of this CommonPartWithCompliance.

        Returns
        -------
        Union[list[CommonSubstanceWithCompliance], None, Unset_Type]
            The substances of this CommonPartWithCompliance.
        """
        return self._substances

    @substances.setter
    def substances(
        self, substances: "Union[list[CommonSubstanceWithCompliance], None, Unset_Type]"
    ) -> None:
        """Sets the substances of this CommonPartWithCompliance.

        Parameters
        ----------
        substances: Union[list[CommonSubstanceWithCompliance], None, Unset_Type]
            The substances of this CommonPartWithCompliance.
        """
        self._substances = substances

    @property
    def input_part_number(self) -> "Union[str, None, Unset_Type]":
        """Gets the input_part_number of this CommonPartWithCompliance.
        This is set to the value of the PartNumber element in the input BoM.

        Returns
        -------
        Union[str, None, Unset_Type]
            The input_part_number of this CommonPartWithCompliance.
        """
        return self._input_part_number

    @input_part_number.setter
    def input_part_number(self, input_part_number: "Union[str, None, Unset_Type]") -> None:
        """Sets the input_part_number of this CommonPartWithCompliance.
        This is set to the value of the PartNumber element in the input BoM.

        Parameters
        ----------
        input_part_number: Union[str, None, Unset_Type]
            The input_part_number of this CommonPartWithCompliance.
        """
        self._input_part_number = input_part_number

    @property
    def external_identity(self) -> "Union[str, None, Unset_Type]":
        """Gets the external_identity of this CommonPartWithCompliance.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, None, Unset_Type]
            The external_identity of this CommonPartWithCompliance.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "Union[str, None, Unset_Type]") -> None:
        """Sets the external_identity of this CommonPartWithCompliance.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: Union[str, None, Unset_Type]
            The external_identity of this CommonPartWithCompliance.
        """
        self._external_identity = external_identity

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this CommonPartWithCompliance.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this CommonPartWithCompliance.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this CommonPartWithCompliance.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this CommonPartWithCompliance.
        """
        self._name = name

    @property
    def reference_type(self) -> "Union[str, None, Unset_Type]":
        """Gets the reference_type of this CommonPartWithCompliance.

        Returns
        -------
        Union[str, None, Unset_Type]
            The reference_type of this CommonPartWithCompliance.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "Union[str, None, Unset_Type]") -> None:
        """Sets the reference_type of this CommonPartWithCompliance.

        Parameters
        ----------
        reference_type: Union[str, None, Unset_Type]
            The reference_type of this CommonPartWithCompliance.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "Union[str, None, Unset_Type]":
        """Gets the reference_value of this CommonPartWithCompliance.

        Returns
        -------
        Union[str, None, Unset_Type]
            The reference_value of this CommonPartWithCompliance.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "Union[str, None, Unset_Type]") -> None:
        """Sets the reference_value of this CommonPartWithCompliance.

        Parameters
        ----------
        reference_value: Union[str, None, Unset_Type]
            The reference_value of this CommonPartWithCompliance.
        """
        self._reference_value = reference_value

    @property
    def id(self) -> "Union[str, None, Unset_Type]":
        """Gets the id of this CommonPartWithCompliance.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        Union[str, None, Unset_Type]
            The id of this CommonPartWithCompliance.
        """
        return self._id

    @id.setter
    def id(self, id: "Union[str, None, Unset_Type]") -> None:
        """Sets the id of this CommonPartWithCompliance.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: Union[str, None, Unset_Type]
            The id of this CommonPartWithCompliance.
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
        if not isinstance(other, CommonPartWithCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
