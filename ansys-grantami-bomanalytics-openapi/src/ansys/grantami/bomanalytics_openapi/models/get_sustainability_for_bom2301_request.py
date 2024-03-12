"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GetSustainabilityForBom2301Request(ModelBase):
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
        "bom_xml2301": "str",
        "config": "CommonRequestConfig",
        "database_key": "str",
        "preferred_units": "CommonPreferredUnits",
    }

    attribute_map: Dict[str, str] = {
        "bom_xml2301": "BomXml2301",
        "config": "Config",
        "database_key": "DatabaseKey",
        "preferred_units": "PreferredUnits",
    }

    subtype_mapping: Dict[str, str] = {
        "PreferredUnits": "CommonPreferredUnits",
        "Config": "CommonRequestConfig",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        bom_xml2301: "Union[str, Unset_Type]" = Unset,
        config: "Union[CommonRequestConfig, Unset_Type]" = Unset,
        database_key: "Union[str, Unset_Type]" = Unset,
        preferred_units: "Union[CommonPreferredUnits, Unset_Type]" = Unset,
    ) -> None:
        """GetSustainabilityForBom2301Request - a model defined in Swagger

        Parameters
        ----------
        bom_xml2301: str, optional
        config: CommonRequestConfig, optional
        database_key: str, optional
        preferred_units: CommonPreferredUnits, optional
        """
        self._bom_xml2301: Union[str, Unset_Type] = Unset
        self._preferred_units: Union[CommonPreferredUnits, Unset_Type] = Unset
        self._database_key: Union[str, Unset_Type] = Unset
        self._config: Union[CommonRequestConfig, Unset_Type] = Unset

        if bom_xml2301 is not Unset:
            self.bom_xml2301 = bom_xml2301
        if preferred_units is not Unset:
            self.preferred_units = preferred_units
        if database_key is not Unset:
            self.database_key = database_key
        if config is not Unset:
            self.config = config

    @property
    def bom_xml2301(self) -> "Union[str, Unset_Type]":
        """Gets the bom_xml2301 of this GetSustainabilityForBom2301Request.

        Returns
        -------
        Union[str, Unset_Type]
            The bom_xml2301 of this GetSustainabilityForBom2301Request.
        """
        return self._bom_xml2301

    @bom_xml2301.setter
    def bom_xml2301(self, bom_xml2301: "Union[str, Unset_Type]") -> None:
        """Sets the bom_xml2301 of this GetSustainabilityForBom2301Request.

        Parameters
        ----------
        bom_xml2301: Union[str, Unset_Type]
            The bom_xml2301 of this GetSustainabilityForBom2301Request.
        """
        # Field is not nullable
        if bom_xml2301 is None:
            raise ValueError("Invalid value for 'bom_xml2301', must not be 'None'")
        self._bom_xml2301 = bom_xml2301

    @property
    def preferred_units(self) -> "Union[CommonPreferredUnits, Unset_Type]":
        """Gets the preferred_units of this GetSustainabilityForBom2301Request.

        Returns
        -------
        Union[CommonPreferredUnits, Unset_Type]
            The preferred_units of this GetSustainabilityForBom2301Request.
        """
        return self._preferred_units

    @preferred_units.setter
    def preferred_units(
        self, preferred_units: "Union[CommonPreferredUnits, Unset_Type]"
    ) -> None:
        """Sets the preferred_units of this GetSustainabilityForBom2301Request.

        Parameters
        ----------
        preferred_units: Union[CommonPreferredUnits, Unset_Type]
            The preferred_units of this GetSustainabilityForBom2301Request.
        """
        # Field is not nullable
        if preferred_units is None:
            raise ValueError("Invalid value for 'preferred_units', must not be 'None'")
        self._preferred_units = preferred_units

    @property
    def database_key(self) -> "Union[str, Unset_Type]":
        """Gets the database_key of this GetSustainabilityForBom2301Request.

        Returns
        -------
        Union[str, Unset_Type]
            The database_key of this GetSustainabilityForBom2301Request.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, Unset_Type]") -> None:
        """Sets the database_key of this GetSustainabilityForBom2301Request.

        Parameters
        ----------
        database_key: Union[str, Unset_Type]
            The database_key of this GetSustainabilityForBom2301Request.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        self._database_key = database_key

    @property
    def config(self) -> "Union[CommonRequestConfig, Unset_Type]":
        """Gets the config of this GetSustainabilityForBom2301Request.

        Returns
        -------
        Union[CommonRequestConfig, Unset_Type]
            The config of this GetSustainabilityForBom2301Request.
        """
        return self._config

    @config.setter
    def config(self, config: "Union[CommonRequestConfig, Unset_Type]") -> None:
        """Sets the config of this GetSustainabilityForBom2301Request.

        Parameters
        ----------
        config: Union[CommonRequestConfig, Unset_Type]
            The config of this GetSustainabilityForBom2301Request.
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
        if not isinstance(other, GetSustainabilityForBom2301Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
