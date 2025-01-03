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


class CommonIndicatorResult(ModelBase):
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
        "flag": "str",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "flag": "Flag",
        "name": "Name",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        flag: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """CommonIndicatorResult - a model defined in Swagger

        Parameters
        ----------
        flag: str, optional
        name: str, optional
        """
        self._name: Union[str, Unset_Type] = Unset
        self._flag: Union[str, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if flag is not Unset:
            self.flag = flag

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this CommonIndicatorResult.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this CommonIndicatorResult.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this CommonIndicatorResult.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this CommonIndicatorResult.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def flag(self) -> "Union[str, Unset_Type]":
        """Gets the flag of this CommonIndicatorResult.

        Returns
        -------
        Union[str, Unset_Type]
            The flag of this CommonIndicatorResult.
        """
        return self._flag

    @flag.setter
    def flag(self, flag: "Union[str, Unset_Type]") -> None:
        """Sets the flag of this CommonIndicatorResult.

        Parameters
        ----------
        flag: Union[str, Unset_Type]
            The flag of this CommonIndicatorResult.
        """
        # Field is not nullable
        if flag is None:
            raise ValueError("Invalid value for 'flag', must not be 'None'")
        self._flag = flag

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
        if not isinstance(other, CommonIndicatorResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
