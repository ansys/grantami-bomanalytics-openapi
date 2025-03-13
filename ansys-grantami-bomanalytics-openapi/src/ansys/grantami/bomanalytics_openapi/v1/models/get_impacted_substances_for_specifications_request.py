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


class GetImpactedSubstancesForSpecificationsRequest(ModelBase):
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
        "config": "CommonRequestConfig",
        "database_key": "str",
        "legislation_ids": "list[str]",
        "specifications": "list[CommonSpecificationReference]",
    }

    attribute_map: dict[str, str] = {
        "config": "Config",
        "database_key": "DatabaseKey",
        "legislation_ids": "LegislationIds",
        "specifications": "Specifications",
    }

    subtype_mapping: dict[str, str] = {
        "Specifications": "CommonSpecificationReference",
        "Config": "CommonRequestConfig",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        config: "Union[CommonRequestConfig, Unset_Type]" = Unset,
        database_key: "Union[str, Unset_Type]" = Unset,
        legislation_ids: "Union[list[str], None, Unset_Type]" = Unset,
        specifications: "Union[list[CommonSpecificationReference], None, Unset_Type]" = Unset,
    ) -> None:
        """GetImpactedSubstancesForSpecificationsRequest - a model defined in Swagger

        Parameters
        ----------
        config: CommonRequestConfig, optional
        database_key: str, optional
        legislation_ids: list[str], optional
        specifications: list[CommonSpecificationReference], optional
        """
        self._specifications: Union[list[CommonSpecificationReference], None, Unset_Type] = Unset
        self._legislation_ids: Union[list[str], None, Unset_Type] = Unset
        self._database_key: Union[str, Unset_Type] = Unset
        self._config: Union[CommonRequestConfig, Unset_Type] = Unset

        if specifications is not Unset:
            self.specifications = specifications
        if legislation_ids is not Unset:
            self.legislation_ids = legislation_ids
        if database_key is not Unset:
            self.database_key = database_key
        if config is not Unset:
            self.config = config

    @property
    def specifications(self) -> "Union[list[CommonSpecificationReference], None, Unset_Type]":
        """Gets the specifications of this GetImpactedSubstancesForSpecificationsRequest.

        Returns
        -------
        Union[list[CommonSpecificationReference], None, Unset_Type]
            The specifications of this GetImpactedSubstancesForSpecificationsRequest.
        """
        return self._specifications

    @specifications.setter
    def specifications(
        self, specifications: "Union[list[CommonSpecificationReference], None, Unset_Type]"
    ) -> None:
        """Sets the specifications of this GetImpactedSubstancesForSpecificationsRequest.

        Parameters
        ----------
        specifications: Union[list[CommonSpecificationReference], None, Unset_Type]
            The specifications of this GetImpactedSubstancesForSpecificationsRequest.
        """
        self._specifications = specifications

    @property
    def legislation_ids(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the legislation_ids of this GetImpactedSubstancesForSpecificationsRequest.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The legislation_ids of this GetImpactedSubstancesForSpecificationsRequest.
        """
        return self._legislation_ids

    @legislation_ids.setter
    def legislation_ids(self, legislation_ids: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the legislation_ids of this GetImpactedSubstancesForSpecificationsRequest.

        Parameters
        ----------
        legislation_ids: Union[list[str], None, Unset_Type]
            The legislation_ids of this GetImpactedSubstancesForSpecificationsRequest.
        """
        self._legislation_ids = legislation_ids

    @property
    def database_key(self) -> "Union[str, Unset_Type]":
        """Gets the database_key of this GetImpactedSubstancesForSpecificationsRequest.

        Returns
        -------
        Union[str, Unset_Type]
            The database_key of this GetImpactedSubstancesForSpecificationsRequest.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, Unset_Type]") -> None:
        """Sets the database_key of this GetImpactedSubstancesForSpecificationsRequest.

        Parameters
        ----------
        database_key: Union[str, Unset_Type]
            The database_key of this GetImpactedSubstancesForSpecificationsRequest.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        self._database_key = database_key

    @property
    def config(self) -> "Union[CommonRequestConfig, Unset_Type]":
        """Gets the config of this GetImpactedSubstancesForSpecificationsRequest.

        Returns
        -------
        Union[CommonRequestConfig, Unset_Type]
            The config of this GetImpactedSubstancesForSpecificationsRequest.
        """
        return self._config

    @config.setter
    def config(self, config: "Union[CommonRequestConfig, Unset_Type]") -> None:
        """Sets the config of this GetImpactedSubstancesForSpecificationsRequest.

        Parameters
        ----------
        config: Union[CommonRequestConfig, Unset_Type]
            The config of this GetImpactedSubstancesForSpecificationsRequest.
        """
        # Field is not nullable
        if config is None:
            raise ValueError("Invalid value for 'config', must not be 'None'")
        self._config = config

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
        if not isinstance(other, GetImpactedSubstancesForSpecificationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
