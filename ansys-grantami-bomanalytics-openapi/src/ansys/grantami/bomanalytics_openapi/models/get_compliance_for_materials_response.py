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


class GetComplianceForMaterialsResponse(ModelBase):
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
        "log_messages": "list[CommonLogEntry]",
        "materials": "list[CommonMaterialWithCompliance]",
    }

    attribute_map: Dict[str, str] = {
        "log_messages": "LogMessages",
        "materials": "Materials",
    }

    subtype_mapping: Dict[str, str] = {
        "Materials": "CommonMaterialWithCompliance",
        "LogMessages": "CommonLogEntry",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        log_messages: "Union[List[CommonLogEntry], Unset_Type]" = Unset,
        materials: "Union[List[CommonMaterialWithCompliance], Unset_Type]" = Unset,
    ) -> None:
        """GetComplianceForMaterialsResponse - a model defined in Swagger

        Parameters
        ----------
        log_messages: List[CommonLogEntry], optional
        materials: List[CommonMaterialWithCompliance], optional
        """
        self._materials: Union[List[CommonMaterialWithCompliance], Unset_Type] = Unset
        self._log_messages: Union[List[CommonLogEntry], Unset_Type] = Unset

        if materials is not Unset:
            self.materials = materials
        if log_messages is not Unset:
            self.log_messages = log_messages

    @property
    def materials(self) -> "Union[List[CommonMaterialWithCompliance], Unset_Type]":
        """Gets the materials of this GetComplianceForMaterialsResponse.

        Returns
        -------
        Union[List[CommonMaterialWithCompliance], Unset_Type]
            The materials of this GetComplianceForMaterialsResponse.
        """
        return self._materials

    @materials.setter
    def materials(self, materials: "Union[List[CommonMaterialWithCompliance], Unset_Type]") -> None:
        """Sets the materials of this GetComplianceForMaterialsResponse.

        Parameters
        ----------
        materials: Union[List[CommonMaterialWithCompliance], Unset_Type]
            The materials of this GetComplianceForMaterialsResponse.
        """
        # Field is not nullable
        if materials is None:
            raise ValueError("Invalid value for 'materials', must not be 'None'")
        self._materials = materials

    @property
    def log_messages(self) -> "Union[List[CommonLogEntry], Unset_Type]":
        """Gets the log_messages of this GetComplianceForMaterialsResponse.

        Returns
        -------
        Union[List[CommonLogEntry], Unset_Type]
            The log_messages of this GetComplianceForMaterialsResponse.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "Union[List[CommonLogEntry], Unset_Type]") -> None:
        """Sets the log_messages of this GetComplianceForMaterialsResponse.

        Parameters
        ----------
        log_messages: Union[List[CommonLogEntry], Unset_Type]
            The log_messages of this GetComplianceForMaterialsResponse.
        """
        # Field is not nullable
        if log_messages is None:
            raise ValueError("Invalid value for 'log_messages', must not be 'None'")
        self._log_messages = log_messages

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
        if not isinstance(other, GetComplianceForMaterialsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
