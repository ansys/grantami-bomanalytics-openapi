"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
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
    swagger_types = {
        "config": "CommonRequestConfig",
        "database_key": "str",
        "indicators": "list[CommonIndicatorDefinition]",
        "materials": "list[CommonMaterialReference]",
    }

    attribute_map = {
        "config": "Config",
        "database_key": "DatabaseKey",
        "indicators": "Indicators",
        "materials": "Materials",
    }

    subtype_mapping = {
        "Materials": "CommonMaterialReference",
        "Indicators": "CommonIndicatorDefinition",
        "Config": "CommonRequestConfig",
    }

    discriminator = None

    def __init__(
        self,
        *,
        config: "Optional[CommonRequestConfig]" = None,
        database_key: "Optional[str]" = None,
        indicators: "Optional[List[CommonIndicatorDefinition]]" = None,
        materials: "Optional[List[CommonMaterialReference]]" = None,
    ) -> None:
        """GetComplianceForMaterialsRequest - a model defined in Swagger

        Parameters
        ----------
            config: CommonRequestConfig, optional
            database_key: str, optional
            indicators: List[CommonIndicatorDefinition], optional
            materials: List[CommonMaterialReference], optional
        """
        self._materials = None
        self._indicators = None
        self._database_key = None
        self._config = None

        if materials is not None:
            self.materials = materials
        if indicators is not None:
            self.indicators = indicators
        if database_key is not None:
            self.database_key = database_key
        if config is not None:
            self.config = config

    @property
    def materials(self) -> "list[CommonMaterialReference]":
        """Gets the materials of this GetComplianceForMaterialsRequest.

        Returns
        -------
        list[CommonMaterialReference]
            The materials of this GetComplianceForMaterialsRequest.
        """
        return self._materials

    @materials.setter
    def materials(self, materials: "list[CommonMaterialReference]") -> None:
        """Sets the materials of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        materials: list[CommonMaterialReference]
            The materials of this GetComplianceForMaterialsRequest.
        """
        self._materials = materials

    @property
    def indicators(self) -> "list[CommonIndicatorDefinition]":
        """Gets the indicators of this GetComplianceForMaterialsRequest.

        Returns
        -------
        list[CommonIndicatorDefinition]
            The indicators of this GetComplianceForMaterialsRequest.
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators: "list[CommonIndicatorDefinition]") -> None:
        """Sets the indicators of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        indicators: list[CommonIndicatorDefinition]
            The indicators of this GetComplianceForMaterialsRequest.
        """
        self._indicators = indicators

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GetComplianceForMaterialsRequest.

        Returns
        -------
        str
            The database_key of this GetComplianceForMaterialsRequest.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        database_key: str
            The database_key of this GetComplianceForMaterialsRequest.
        """
        self._database_key = database_key

    @property
    def config(self) -> "CommonRequestConfig":
        """Gets the config of this GetComplianceForMaterialsRequest.

        Returns
        -------
        CommonRequestConfig
            The config of this GetComplianceForMaterialsRequest.
        """
        return self._config

    @config.setter
    def config(self, config: "CommonRequestConfig") -> None:
        """Sets the config of this GetComplianceForMaterialsRequest.

        Parameters
        ----------
        config: CommonRequestConfig
            The config of this GetComplianceForMaterialsRequest.
        """
        self._config = config

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GetComplianceForMaterialsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

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
