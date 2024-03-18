"""
    Granta.BomAnalyticsServices.V1

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


class GetComplianceForBom2301Response(ModelBase):
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
        "parts": "list[CommonPartWithCompliance]",
    }

    attribute_map: Dict[str, str] = {
        "log_messages": "LogMessages",
        "parts": "Parts",
    }

    subtype_mapping: Dict[str, str] = {
        "Parts": "CommonPartWithCompliance",
        "LogMessages": "CommonLogEntry",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        log_messages: "Union[List[CommonLogEntry], Unset_Type]" = Unset,
        parts: "Union[List[CommonPartWithCompliance], Unset_Type]" = Unset,
    ) -> None:
        """GetComplianceForBom2301Response - a model defined in Swagger

        Parameters
        ----------
        log_messages: List[CommonLogEntry], optional
        parts: List[CommonPartWithCompliance], optional
        """
        self._parts: Union[List[CommonPartWithCompliance], Unset_Type] = Unset
        self._log_messages: Union[List[CommonLogEntry], Unset_Type] = Unset

        if parts is not Unset:
            self.parts = parts
        if log_messages is not Unset:
            self.log_messages = log_messages

    @property
    def parts(self) -> "Union[List[CommonPartWithCompliance], Unset_Type]":
        """Gets the parts of this GetComplianceForBom2301Response.

        Returns
        -------
        Union[List[CommonPartWithCompliance], Unset_Type]
            The parts of this GetComplianceForBom2301Response.
        """
        return self._parts

    @parts.setter
    def parts(self, parts: "Union[List[CommonPartWithCompliance], Unset_Type]") -> None:
        """Sets the parts of this GetComplianceForBom2301Response.

        Parameters
        ----------
        parts: Union[List[CommonPartWithCompliance], Unset_Type]
            The parts of this GetComplianceForBom2301Response.
        """
        # Field is not nullable
        if parts is None:
            raise ValueError("Invalid value for 'parts', must not be 'None'")
        self._parts = parts

    @property
    def log_messages(self) -> "Union[List[CommonLogEntry], Unset_Type]":
        """Gets the log_messages of this GetComplianceForBom2301Response.

        Returns
        -------
        Union[List[CommonLogEntry], Unset_Type]
            The log_messages of this GetComplianceForBom2301Response.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(
        self, log_messages: "Union[List[CommonLogEntry], Unset_Type]"
    ) -> None:
        """Sets the log_messages of this GetComplianceForBom2301Response.

        Parameters
        ----------
        log_messages: Union[List[CommonLogEntry], Unset_Type]
            The log_messages of this GetComplianceForBom2301Response.
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
        if not isinstance(other, GetComplianceForBom2301Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
