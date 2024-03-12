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


class GetImpactedSubstancesForBom2301Response(ModelBase):
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
        "legislations": "list[CommonLegislationWithImpactedSubstances]",
        "log_messages": "list[CommonLogEntry]",
    }

    attribute_map: Dict[str, str] = {
        "legislations": "Legislations",
        "log_messages": "LogMessages",
    }

    subtype_mapping: Dict[str, str] = {
        "Legislations": "CommonLegislationWithImpactedSubstances",
        "LogMessages": "CommonLogEntry",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        legislations: "Union[List[CommonLegislationWithImpactedSubstances], Unset_Type]" = Unset,
        log_messages: "Union[List[CommonLogEntry], Unset_Type]" = Unset,
    ) -> None:
        """GetImpactedSubstancesForBom2301Response - a model defined in Swagger

        Parameters
        ----------
        legislations: List[CommonLegislationWithImpactedSubstances], optional
        log_messages: List[CommonLogEntry], optional
        """
        self._legislations: Union[
            List[CommonLegislationWithImpactedSubstances], Unset_Type
        ] = Unset
        self._log_messages: Union[List[CommonLogEntry], Unset_Type] = Unset

        if legislations is not Unset:
            self.legislations = legislations
        if log_messages is not Unset:
            self.log_messages = log_messages

    @property
    def legislations(
        self,
    ) -> "Union[List[CommonLegislationWithImpactedSubstances], Unset_Type]":
        """Gets the legislations of this GetImpactedSubstancesForBom2301Response.

        Returns
        -------
        Union[List[CommonLegislationWithImpactedSubstances], Unset_Type]
            The legislations of this GetImpactedSubstancesForBom2301Response.
        """
        return self._legislations

    @legislations.setter
    def legislations(
        self,
        legislations: "Union[List[CommonLegislationWithImpactedSubstances], Unset_Type]",
    ) -> None:
        """Sets the legislations of this GetImpactedSubstancesForBom2301Response.

        Parameters
        ----------
        legislations: Union[List[CommonLegislationWithImpactedSubstances], Unset_Type]
            The legislations of this GetImpactedSubstancesForBom2301Response.
        """
        # Field is not nullable
        if legislations is None:
            raise ValueError("Invalid value for 'legislations', must not be 'None'")
        self._legislations = legislations

    @property
    def log_messages(self) -> "Union[List[CommonLogEntry], Unset_Type]":
        """Gets the log_messages of this GetImpactedSubstancesForBom2301Response.

        Returns
        -------
        Union[List[CommonLogEntry], Unset_Type]
            The log_messages of this GetImpactedSubstancesForBom2301Response.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(
        self, log_messages: "Union[List[CommonLogEntry], Unset_Type]"
    ) -> None:
        """Sets the log_messages of this GetImpactedSubstancesForBom2301Response.

        Parameters
        ----------
        log_messages: Union[List[CommonLogEntry], Unset_Type]
            The log_messages of this GetImpactedSubstancesForBom2301Response.
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
        if not isinstance(other, GetImpactedSubstancesForBom2301Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
