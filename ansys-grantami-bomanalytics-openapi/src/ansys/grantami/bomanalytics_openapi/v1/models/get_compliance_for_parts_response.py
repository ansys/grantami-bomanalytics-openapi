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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GetComplianceForPartsResponse(ModelBase):
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
        "parts": "list[CommonPartWithCompliance]",
    }

    attribute_map: dict[str, str] = {
        "log_messages": "LogMessages",
        "parts": "Parts",
    }

    subtype_mapping: dict[str, str] = {
        "Parts": "CommonPartWithCompliance",
        "LogMessages": "CommonLogEntry",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        log_messages: "list[CommonLogEntry] | None | Unset_Type" = Unset,
        parts: "list[CommonPartWithCompliance] | None | Unset_Type" = Unset,
    ) -> None:
        """GetComplianceForPartsResponse - a model defined in Swagger

        Parameters
        ----------
        log_messages: list[CommonLogEntry] | None, optional
        parts: list[CommonPartWithCompliance] | None, optional
        """
        self._parts: list[CommonPartWithCompliance] | None | Unset_Type = Unset
        self._log_messages: list[CommonLogEntry] | None | Unset_Type = Unset

        if parts is not Unset:
            self.parts = parts
        if log_messages is not Unset:
            self.log_messages = log_messages

    @property
    def parts(self) -> "list[CommonPartWithCompliance] | None | Unset_Type":
        """Gets the parts of this GetComplianceForPartsResponse.

        Returns
        -------
        list[CommonPartWithCompliance] | None | Unset_Type
            The parts of this GetComplianceForPartsResponse.
        """
        return self._parts

    @parts.setter
    def parts(self, parts: "list[CommonPartWithCompliance] | None | Unset_Type") -> None:
        """Sets the parts of this GetComplianceForPartsResponse.

        Parameters
        ----------
        parts: list[CommonPartWithCompliance] | None | Unset_Type
            The parts of this GetComplianceForPartsResponse.
        """
        self._parts = parts

    @property
    def log_messages(self) -> "list[CommonLogEntry] | None | Unset_Type":
        """Gets the log_messages of this GetComplianceForPartsResponse.

        Returns
        -------
        list[CommonLogEntry] | None | Unset_Type
            The log_messages of this GetComplianceForPartsResponse.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "list[CommonLogEntry] | None | Unset_Type") -> None:
        """Sets the log_messages of this GetComplianceForPartsResponse.

        Parameters
        ----------
        log_messages: list[CommonLogEntry] | None | Unset_Type
            The log_messages of this GetComplianceForPartsResponse.
        """
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
        if not isinstance(other, GetComplianceForPartsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
