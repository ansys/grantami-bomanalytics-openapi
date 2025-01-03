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


class GetSustainabilitySummaryForBom2301Response(ModelBase):
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
        "log_messages": "list[CommonLogEntry]",
        "material_summary": "CommonSustainabilityMaterialSummary",
        "process_summary": "CommonSustainabilityProcessSummary",
        "transport_summary": "CommonSustainabilityTransportSummary",
    }

    attribute_map: dict[str, str] = {
        "log_messages": "LogMessages",
        "material_summary": "MaterialSummary",
        "process_summary": "ProcessSummary",
        "transport_summary": "TransportSummary",
    }

    subtype_mapping: dict[str, str] = {
        "MaterialSummary": "CommonSustainabilityMaterialSummary",
        "ProcessSummary": "CommonSustainabilityProcessSummary",
        "TransportSummary": "CommonSustainabilityTransportSummary",
        "LogMessages": "CommonLogEntry",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        log_messages: "Union[list[CommonLogEntry], Unset_Type]" = Unset,
        material_summary: "Union[CommonSustainabilityMaterialSummary, Unset_Type]" = Unset,
        process_summary: "Union[CommonSustainabilityProcessSummary, Unset_Type]" = Unset,
        transport_summary: "Union[CommonSustainabilityTransportSummary, Unset_Type]" = Unset,
    ) -> None:
        """GetSustainabilitySummaryForBom2301Response - a model defined in Swagger

        Parameters
        ----------
        log_messages: list[CommonLogEntry], optional
        material_summary: CommonSustainabilityMaterialSummary, optional
        process_summary: CommonSustainabilityProcessSummary, optional
        transport_summary: CommonSustainabilityTransportSummary, optional
        """
        self._material_summary: Union[CommonSustainabilityMaterialSummary, Unset_Type] = Unset
        self._process_summary: Union[CommonSustainabilityProcessSummary, Unset_Type] = Unset
        self._transport_summary: Union[CommonSustainabilityTransportSummary, Unset_Type] = Unset
        self._log_messages: Union[list[CommonLogEntry], Unset_Type] = Unset

        if material_summary is not Unset:
            self.material_summary = material_summary
        if process_summary is not Unset:
            self.process_summary = process_summary
        if transport_summary is not Unset:
            self.transport_summary = transport_summary
        if log_messages is not Unset:
            self.log_messages = log_messages

    @property
    def material_summary(self) -> "Union[CommonSustainabilityMaterialSummary, Unset_Type]":
        """Gets the material_summary of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        Union[CommonSustainabilityMaterialSummary, Unset_Type]
            The material_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._material_summary

    @material_summary.setter
    def material_summary(
        self, material_summary: "Union[CommonSustainabilityMaterialSummary, Unset_Type]"
    ) -> None:
        """Sets the material_summary of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        material_summary: Union[CommonSustainabilityMaterialSummary, Unset_Type]
            The material_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        # Field is not nullable
        if material_summary is None:
            raise ValueError("Invalid value for 'material_summary', must not be 'None'")
        self._material_summary = material_summary

    @property
    def process_summary(self) -> "Union[CommonSustainabilityProcessSummary, Unset_Type]":
        """Gets the process_summary of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        Union[CommonSustainabilityProcessSummary, Unset_Type]
            The process_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._process_summary

    @process_summary.setter
    def process_summary(
        self, process_summary: "Union[CommonSustainabilityProcessSummary, Unset_Type]"
    ) -> None:
        """Sets the process_summary of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        process_summary: Union[CommonSustainabilityProcessSummary, Unset_Type]
            The process_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        # Field is not nullable
        if process_summary is None:
            raise ValueError("Invalid value for 'process_summary', must not be 'None'")
        self._process_summary = process_summary

    @property
    def transport_summary(self) -> "Union[CommonSustainabilityTransportSummary, Unset_Type]":
        """Gets the transport_summary of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        Union[CommonSustainabilityTransportSummary, Unset_Type]
            The transport_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._transport_summary

    @transport_summary.setter
    def transport_summary(
        self, transport_summary: "Union[CommonSustainabilityTransportSummary, Unset_Type]"
    ) -> None:
        """Sets the transport_summary of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        transport_summary: Union[CommonSustainabilityTransportSummary, Unset_Type]
            The transport_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        # Field is not nullable
        if transport_summary is None:
            raise ValueError("Invalid value for 'transport_summary', must not be 'None'")
        self._transport_summary = transport_summary

    @property
    def log_messages(self) -> "Union[list[CommonLogEntry], Unset_Type]":
        """Gets the log_messages of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        Union[list[CommonLogEntry], Unset_Type]
            The log_messages of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "Union[list[CommonLogEntry], Unset_Type]") -> None:
        """Sets the log_messages of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        log_messages: Union[list[CommonLogEntry], Unset_Type]
            The log_messages of this GetSustainabilitySummaryForBom2301Response.
        """
        # Field is not nullable
        if log_messages is None:
            raise ValueError("Invalid value for 'log_messages', must not be 'None'")
        self._log_messages = log_messages

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
        if not isinstance(other, GetSustainabilitySummaryForBom2301Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
