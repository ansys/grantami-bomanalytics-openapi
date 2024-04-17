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


class CommonSustainabilityMaterialContributingComponent(ModelBase):
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
        "component_name": "str",
        "component_part_number": "str",
        "material_mass_before_processing": "CommonValueWithUnit",
        "record_reference": "CommonPartReference",
    }

    attribute_map: Dict[str, str] = {
        "component_name": "ComponentName",
        "component_part_number": "ComponentPartNumber",
        "material_mass_before_processing": "MaterialMassBeforeProcessing",
        "record_reference": "RecordReference",
    }

    subtype_mapping: Dict[str, str] = {
        "RecordReference": "CommonPartReference",
        "MaterialMassBeforeProcessing": "CommonValueWithUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        component_name: "Union[str, Unset_Type]" = Unset,
        component_part_number: "Union[str, Unset_Type]" = Unset,
        material_mass_before_processing: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        record_reference: "Union[CommonPartReference, Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityMaterialContributingComponent - a model defined in Swagger

        Parameters
        ----------
        component_name: str, optional
        component_part_number: str, optional
        material_mass_before_processing: CommonValueWithUnit, optional
        record_reference: CommonPartReference, optional
        """
        self._component_name: Union[str, Unset_Type] = Unset
        self._component_part_number: Union[str, Unset_Type] = Unset
        self._record_reference: Union[CommonPartReference, Unset_Type] = Unset
        self._material_mass_before_processing: Union[
            CommonValueWithUnit, Unset_Type
        ] = Unset

        if component_name is not Unset:
            self.component_name = component_name
        if component_part_number is not Unset:
            self.component_part_number = component_part_number
        if record_reference is not Unset:
            self.record_reference = record_reference
        if material_mass_before_processing is not Unset:
            self.material_mass_before_processing = material_mass_before_processing

    @property
    def component_name(self) -> "Union[str, Unset_Type]":
        """Gets the component_name of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        Union[str, Unset_Type]
            The component_name of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name: "Union[str, Unset_Type]") -> None:
        """Sets the component_name of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        component_name: Union[str, Unset_Type]
            The component_name of this CommonSustainabilityMaterialContributingComponent.
        """
        # Field is not nullable
        if component_name is None:
            raise ValueError("Invalid value for 'component_name', must not be 'None'")
        self._component_name = component_name

    @property
    def component_part_number(self) -> "Union[str, Unset_Type]":
        """Gets the component_part_number of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        Union[str, Unset_Type]
            The component_part_number of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._component_part_number

    @component_part_number.setter
    def component_part_number(
        self, component_part_number: "Union[str, Unset_Type]"
    ) -> None:
        """Sets the component_part_number of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        component_part_number: Union[str, Unset_Type]
            The component_part_number of this CommonSustainabilityMaterialContributingComponent.
        """
        # Field is not nullable
        if component_part_number is None:
            raise ValueError(
                "Invalid value for 'component_part_number', must not be 'None'"
            )
        self._component_part_number = component_part_number

    @property
    def record_reference(self) -> "Union[CommonPartReference, Unset_Type]":
        """Gets the record_reference of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        Union[CommonPartReference, Unset_Type]
            The record_reference of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._record_reference

    @record_reference.setter
    def record_reference(
        self, record_reference: "Union[CommonPartReference, Unset_Type]"
    ) -> None:
        """Sets the record_reference of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        record_reference: Union[CommonPartReference, Unset_Type]
            The record_reference of this CommonSustainabilityMaterialContributingComponent.
        """
        # Field is not nullable
        if record_reference is None:
            raise ValueError("Invalid value for 'record_reference', must not be 'None'")
        self._record_reference = record_reference

    @property
    def material_mass_before_processing(
        self,
    ) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.
        """
        return self._material_mass_before_processing

    @material_mass_before_processing.setter
    def material_mass_before_processing(
        self, material_mass_before_processing: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.

        Parameters
        ----------
        material_mass_before_processing: Union[CommonValueWithUnit, Unset_Type]
            The material_mass_before_processing of this CommonSustainabilityMaterialContributingComponent.
        """
        # Field is not nullable
        if material_mass_before_processing is None:
            raise ValueError(
                "Invalid value for 'material_mass_before_processing', must not be 'None'"
            )
        self._material_mass_before_processing = material_mass_before_processing

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
        if not isinstance(other, CommonSustainabilityMaterialContributingComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
