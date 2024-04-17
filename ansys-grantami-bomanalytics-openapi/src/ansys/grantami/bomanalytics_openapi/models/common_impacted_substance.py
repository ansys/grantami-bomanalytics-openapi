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
from typing import List  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, Optional, Union

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class CommonImpactedSubstance(ModelBase):
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
        "cas_number": "str",
        "ec_number": "str",
        "legislation_threshold": "float",
        "max_percentage_amount_in_material": "float",
        "substance_name": "str",
    }

    attribute_map: Dict[str, str] = {
        "cas_number": "CasNumber",
        "ec_number": "EcNumber",
        "legislation_threshold": "LegislationThreshold",
        "max_percentage_amount_in_material": "MaxPercentageAmountInMaterial",
        "substance_name": "SubstanceName",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        cas_number: "Union[str, Unset_Type]" = Unset,
        ec_number: "Union[str, Unset_Type]" = Unset,
        legislation_threshold: "Union[float, None, Unset_Type]" = Unset,
        max_percentage_amount_in_material: "Union[float, None, Unset_Type]" = Unset,
        substance_name: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """CommonImpactedSubstance - a model defined in Swagger

        Parameters
        ----------
        cas_number: str, optional
        ec_number: str, optional
        legislation_threshold: float, optional
        max_percentage_amount_in_material: float, optional
        substance_name: str, optional
        """
        self._substance_name: Union[str, Unset_Type] = Unset
        self._cas_number: Union[str, Unset_Type] = Unset
        self._ec_number: Union[str, Unset_Type] = Unset
        self._max_percentage_amount_in_material: Union[float, None, Unset_Type] = Unset
        self._legislation_threshold: Union[float, None, Unset_Type] = Unset

        if substance_name is not Unset:
            self.substance_name = substance_name
        if cas_number is not Unset:
            self.cas_number = cas_number
        if ec_number is not Unset:
            self.ec_number = ec_number
        if max_percentage_amount_in_material is not Unset:
            self.max_percentage_amount_in_material = max_percentage_amount_in_material
        if legislation_threshold is not Unset:
            self.legislation_threshold = legislation_threshold

    @property
    def substance_name(self) -> "Union[str, Unset_Type]":
        """Gets the substance_name of this CommonImpactedSubstance.

        Returns
        -------
        Union[str, Unset_Type]
            The substance_name of this CommonImpactedSubstance.
        """
        return self._substance_name

    @substance_name.setter
    def substance_name(self, substance_name: "Union[str, Unset_Type]") -> None:
        """Sets the substance_name of this CommonImpactedSubstance.

        Parameters
        ----------
        substance_name: Union[str, Unset_Type]
            The substance_name of this CommonImpactedSubstance.
        """
        # Field is not nullable
        if substance_name is None:
            raise ValueError("Invalid value for 'substance_name', must not be 'None'")
        self._substance_name = substance_name

    @property
    def cas_number(self) -> "Union[str, Unset_Type]":
        """Gets the cas_number of this CommonImpactedSubstance.

        Returns
        -------
        Union[str, Unset_Type]
            The cas_number of this CommonImpactedSubstance.
        """
        return self._cas_number

    @cas_number.setter
    def cas_number(self, cas_number: "Union[str, Unset_Type]") -> None:
        """Sets the cas_number of this CommonImpactedSubstance.

        Parameters
        ----------
        cas_number: Union[str, Unset_Type]
            The cas_number of this CommonImpactedSubstance.
        """
        # Field is not nullable
        if cas_number is None:
            raise ValueError("Invalid value for 'cas_number', must not be 'None'")
        self._cas_number = cas_number

    @property
    def ec_number(self) -> "Union[str, Unset_Type]":
        """Gets the ec_number of this CommonImpactedSubstance.

        Returns
        -------
        Union[str, Unset_Type]
            The ec_number of this CommonImpactedSubstance.
        """
        return self._ec_number

    @ec_number.setter
    def ec_number(self, ec_number: "Union[str, Unset_Type]") -> None:
        """Sets the ec_number of this CommonImpactedSubstance.

        Parameters
        ----------
        ec_number: Union[str, Unset_Type]
            The ec_number of this CommonImpactedSubstance.
        """
        # Field is not nullable
        if ec_number is None:
            raise ValueError("Invalid value for 'ec_number', must not be 'None'")
        self._ec_number = ec_number

    @property
    def max_percentage_amount_in_material(self) -> "Union[float, None, Unset_Type]":
        """Gets the max_percentage_amount_in_material of this CommonImpactedSubstance.

        Returns
        -------
        Union[float, None, Unset_Type]
            The max_percentage_amount_in_material of this CommonImpactedSubstance.
        """
        return self._max_percentage_amount_in_material

    @max_percentage_amount_in_material.setter
    def max_percentage_amount_in_material(
        self, max_percentage_amount_in_material: "Union[float, None, Unset_Type]"
    ) -> None:
        """Sets the max_percentage_amount_in_material of this CommonImpactedSubstance.

        Parameters
        ----------
        max_percentage_amount_in_material: Union[float, None, Unset_Type]
            The max_percentage_amount_in_material of this CommonImpactedSubstance.
        """
        self._max_percentage_amount_in_material = max_percentage_amount_in_material

    @property
    def legislation_threshold(self) -> "Union[float, None, Unset_Type]":
        """Gets the legislation_threshold of this CommonImpactedSubstance.

        Returns
        -------
        Union[float, None, Unset_Type]
            The legislation_threshold of this CommonImpactedSubstance.
        """
        return self._legislation_threshold

    @legislation_threshold.setter
    def legislation_threshold(
        self, legislation_threshold: "Union[float, None, Unset_Type]"
    ) -> None:
        """Sets the legislation_threshold of this CommonImpactedSubstance.

        Parameters
        ----------
        legislation_threshold: Union[float, None, Unset_Type]
            The legislation_threshold of this CommonImpactedSubstance.
        """
        self._legislation_threshold = legislation_threshold

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
        if not isinstance(other, CommonImpactedSubstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
