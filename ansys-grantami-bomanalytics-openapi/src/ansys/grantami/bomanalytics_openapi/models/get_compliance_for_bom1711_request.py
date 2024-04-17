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


class GetComplianceForBom1711Request(ModelBase):
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
        "bom_xml1711": "str",
        "config": "CommonRequestConfig",
        "database_key": "str",
        "indicators": "list[CommonIndicatorDefinition]",
    }

    attribute_map: Dict[str, str] = {
        "bom_xml1711": "BomXml1711",
        "config": "Config",
        "database_key": "DatabaseKey",
        "indicators": "Indicators",
    }

    subtype_mapping: Dict[str, str] = {
        "Indicators": "CommonIndicatorDefinition",
        "Config": "CommonRequestConfig",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        bom_xml1711: "Union[str, Unset_Type]" = Unset,
        config: "Union[CommonRequestConfig, Unset_Type]" = Unset,
        database_key: "Union[str, Unset_Type]" = Unset,
        indicators: "Union[List[CommonIndicatorDefinition], Unset_Type]" = Unset,
    ) -> None:
        """GetComplianceForBom1711Request - a model defined in Swagger

        Parameters
        ----------
        bom_xml1711: str, optional
        config: CommonRequestConfig, optional
        database_key: str, optional
        indicators: List[CommonIndicatorDefinition], optional
        """
        self._bom_xml1711: Union[str, Unset_Type] = Unset
        self._indicators: Union[List[CommonIndicatorDefinition], Unset_Type] = Unset
        self._database_key: Union[str, Unset_Type] = Unset
        self._config: Union[CommonRequestConfig, Unset_Type] = Unset

        if bom_xml1711 is not Unset:
            self.bom_xml1711 = bom_xml1711
        if indicators is not Unset:
            self.indicators = indicators
        if database_key is not Unset:
            self.database_key = database_key
        if config is not Unset:
            self.config = config

    @property
    def bom_xml1711(self) -> "Union[str, Unset_Type]":
        """Gets the bom_xml1711 of this GetComplianceForBom1711Request.

        Returns
        -------
        Union[str, Unset_Type]
            The bom_xml1711 of this GetComplianceForBom1711Request.
        """
        return self._bom_xml1711

    @bom_xml1711.setter
    def bom_xml1711(self, bom_xml1711: "Union[str, Unset_Type]") -> None:
        """Sets the bom_xml1711 of this GetComplianceForBom1711Request.

        Parameters
        ----------
        bom_xml1711: Union[str, Unset_Type]
            The bom_xml1711 of this GetComplianceForBom1711Request.
        """
        # Field is not nullable
        if bom_xml1711 is None:
            raise ValueError("Invalid value for 'bom_xml1711', must not be 'None'")
        self._bom_xml1711 = bom_xml1711

    @property
    def indicators(self) -> "Union[List[CommonIndicatorDefinition], Unset_Type]":
        """Gets the indicators of this GetComplianceForBom1711Request.

        Returns
        -------
        Union[List[CommonIndicatorDefinition], Unset_Type]
            The indicators of this GetComplianceForBom1711Request.
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators: "Union[List[CommonIndicatorDefinition], Unset_Type]") -> None:
        """Sets the indicators of this GetComplianceForBom1711Request.

        Parameters
        ----------
        indicators: Union[List[CommonIndicatorDefinition], Unset_Type]
            The indicators of this GetComplianceForBom1711Request.
        """
        # Field is not nullable
        if indicators is None:
            raise ValueError("Invalid value for 'indicators', must not be 'None'")
        self._indicators = indicators

    @property
    def database_key(self) -> "Union[str, Unset_Type]":
        """Gets the database_key of this GetComplianceForBom1711Request.

        Returns
        -------
        Union[str, Unset_Type]
            The database_key of this GetComplianceForBom1711Request.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, Unset_Type]") -> None:
        """Sets the database_key of this GetComplianceForBom1711Request.

        Parameters
        ----------
        database_key: Union[str, Unset_Type]
            The database_key of this GetComplianceForBom1711Request.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        self._database_key = database_key

    @property
    def config(self) -> "Union[CommonRequestConfig, Unset_Type]":
        """Gets the config of this GetComplianceForBom1711Request.

        Returns
        -------
        Union[CommonRequestConfig, Unset_Type]
            The config of this GetComplianceForBom1711Request.
        """
        return self._config

    @config.setter
    def config(self, config: "Union[CommonRequestConfig, Unset_Type]") -> None:
        """Sets the config of this GetComplianceForBom1711Request.

        Parameters
        ----------
        config: Union[CommonRequestConfig, Unset_Type]
            The config of this GetComplianceForBom1711Request.
        """
        # Field is not nullable
        if config is None:
            raise ValueError("Invalid value for 'config', must not be 'None'")
        self._config = config

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
        if not isinstance(other, GetComplianceForBom1711Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
