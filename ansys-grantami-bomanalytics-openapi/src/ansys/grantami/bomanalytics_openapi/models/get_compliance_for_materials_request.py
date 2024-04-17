"""
    Granta.BomAnalyticsServices.V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GetComplianceForMaterialsRequest(ModelBase):
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
        "config": "CommonRequestConfig",
        "database_key": "str",
        "indicators": "list[CommonIndicatorDefinition]",
        "materials": "list[CommonMaterialReference]",
    }

    attribute_map: Dict[str, str] = {
        "config": "Config",
        "database_key": "DatabaseKey",
        "indicators": "Indicators",
        "materials": "Materials",
    }

    subtype_mapping: Dict[str, str] = {
        "Materials": "CommonMaterialReference",
        "Indicators": "CommonIndicatorDefinition",
        "Config": "CommonRequestConfig",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, config: "Union[CommonRequestConfig, Unset_Type]" = Unset, database_key: "Union[str, Unset_Type]" = Unset, indicators: "Union[List[CommonIndicatorDefinition], Unset_Type]" = Unset, materials: "Union[List[CommonMaterialReference], Unset_Type]" = Unset,) -> None:
        """GetComplianceForMaterialsRequest - a model defined in Swagger

        Parameters
        ----------
        config: CommonRequestConfig, optional
        database_key: str, optional
        indicators: List[CommonIndicatorDefinition], optional
        materials: List[CommonMaterialReference], optional
        """
        self._materials: Union[List[CommonMaterialReference], Unset_Type] = Unset
        self._indicators: Union[List[CommonIndicatorDefinition], Unset_Type] = Unset
        self._database_key: Union[str, Unset_Type] = Unset
        self._config: Union[CommonRequestConfig, Unset_Type] = Unset

        if materials is not Unset:
            self.materials = materials
        if indicators is not Unset:
            self.indicators = indicators
        if database_key is not Unset:
            self.database_key = database_key
        if config is not Unset:
            self.config = config

    @property
    def materials(self) -> "Union[List[CommonMaterialReference], Unset_Type]":
        """Gets the materials of this GetComplianceForMaterialsRequest.

        Returns
        -------
        Union[List[CommonMaterialReference], Unset_Type]
            The materials of this GetComplianceForMaterialsRequest.
        """
        return self._materials

    @materials.setter
    def materials(self, materials: "Union[List[CommonMaterialReference], Unset_Type]") -> None:
        """Sets the materials of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        materials: Union[List[CommonMaterialReference], Unset_Type]
            The materials of this GetComplianceForMaterialsRequest.
        """
        # Field is not nullable
        if materials is None:
            raise ValueError("Invalid value for 'materials', must not be 'None'")
        self._materials = materials

    @property
    def indicators(self) -> "Union[List[CommonIndicatorDefinition], Unset_Type]":
        """Gets the indicators of this GetComplianceForMaterialsRequest.

        Returns
        -------
        Union[List[CommonIndicatorDefinition], Unset_Type]
            The indicators of this GetComplianceForMaterialsRequest.
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators: "Union[List[CommonIndicatorDefinition], Unset_Type]") -> None:
        """Sets the indicators of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        indicators: Union[List[CommonIndicatorDefinition], Unset_Type]
            The indicators of this GetComplianceForMaterialsRequest.
        """
        # Field is not nullable
        if indicators is None:
            raise ValueError("Invalid value for 'indicators', must not be 'None'")
        self._indicators = indicators

    @property
    def database_key(self) -> "Union[str, Unset_Type]":
        """Gets the database_key of this GetComplianceForMaterialsRequest.

        Returns
        -------
        Union[str, Unset_Type]
            The database_key of this GetComplianceForMaterialsRequest.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, Unset_Type]") -> None:
        """Sets the database_key of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        database_key: Union[str, Unset_Type]
            The database_key of this GetComplianceForMaterialsRequest.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        self._database_key = database_key

    @property
    def config(self) -> "Union[CommonRequestConfig, Unset_Type]":
        """Gets the config of this GetComplianceForMaterialsRequest.

        Returns
        -------
        Union[CommonRequestConfig, Unset_Type]
            The config of this GetComplianceForMaterialsRequest.
        """
        return self._config

    @config.setter
    def config(self, config: "Union[CommonRequestConfig, Unset_Type]") -> None:
        """Sets the config of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        config: Union[CommonRequestConfig, Unset_Type]
            The config of this GetComplianceForMaterialsRequest.
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
        if not isinstance(other, GetComplianceForMaterialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

