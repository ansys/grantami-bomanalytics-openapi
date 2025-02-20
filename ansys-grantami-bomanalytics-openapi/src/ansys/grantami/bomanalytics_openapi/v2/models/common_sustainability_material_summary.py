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


class CommonSustainabilityMaterialSummary(ModelBase):
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
        "phase_summary": "CommonSustainabilityPhaseSummary",
        "summary": "list[CommonSustainabilityMaterialSummaryEntry]",
    }

    attribute_map: dict[str, str] = {
        "phase_summary": "PhaseSummary",
        "summary": "Summary",
    }

    subtype_mapping: dict[str, str] = {
        "Summary": "CommonSustainabilityMaterialSummaryEntry",
        "PhaseSummary": "CommonSustainabilityPhaseSummary",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        phase_summary: "Union[CommonSustainabilityPhaseSummary, Unset_Type]" = Unset,
        summary: "Union[list[CommonSustainabilityMaterialSummaryEntry], Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityMaterialSummary - a model defined in Swagger

        Parameters
        ----------
        phase_summary: CommonSustainabilityPhaseSummary, optional
        summary: list[CommonSustainabilityMaterialSummaryEntry], optional
        """
        self._summary: Union[list[CommonSustainabilityMaterialSummaryEntry], Unset_Type] = Unset
        self._phase_summary: Union[CommonSustainabilityPhaseSummary, Unset_Type] = Unset

        if summary is not Unset:
            self.summary = summary
        if phase_summary is not Unset:
            self.phase_summary = phase_summary

    @property
    def summary(self) -> "Union[list[CommonSustainabilityMaterialSummaryEntry], Unset_Type]":
        """Gets the summary of this CommonSustainabilityMaterialSummary.

        Returns
        -------
        Union[list[CommonSustainabilityMaterialSummaryEntry], Unset_Type]
            The summary of this CommonSustainabilityMaterialSummary.
        """
        return self._summary

    @summary.setter
    def summary(
        self, summary: "Union[list[CommonSustainabilityMaterialSummaryEntry], Unset_Type]"
    ) -> None:
        """Sets the summary of this CommonSustainabilityMaterialSummary.

        Parameters
        ----------
        summary: Union[list[CommonSustainabilityMaterialSummaryEntry], Unset_Type]
            The summary of this CommonSustainabilityMaterialSummary.
        """
        # Field is not nullable
        if summary is None:
            raise ValueError("Invalid value for 'summary', must not be 'None'")
        self._summary = summary

    @property
    def phase_summary(self) -> "Union[CommonSustainabilityPhaseSummary, Unset_Type]":
        """Gets the phase_summary of this CommonSustainabilityMaterialSummary.

        Returns
        -------
        Union[CommonSustainabilityPhaseSummary, Unset_Type]
            The phase_summary of this CommonSustainabilityMaterialSummary.
        """
        return self._phase_summary

    @phase_summary.setter
    def phase_summary(
        self, phase_summary: "Union[CommonSustainabilityPhaseSummary, Unset_Type]"
    ) -> None:
        """Sets the phase_summary of this CommonSustainabilityMaterialSummary.

        Parameters
        ----------
        phase_summary: Union[CommonSustainabilityPhaseSummary, Unset_Type]
            The phase_summary of this CommonSustainabilityMaterialSummary.
        """
        # Field is not nullable
        if phase_summary is None:
            raise ValueError("Invalid value for 'phase_summary', must not be 'None'")
        self._phase_summary = phase_summary

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
        if not isinstance(other, CommonSustainabilityMaterialSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
