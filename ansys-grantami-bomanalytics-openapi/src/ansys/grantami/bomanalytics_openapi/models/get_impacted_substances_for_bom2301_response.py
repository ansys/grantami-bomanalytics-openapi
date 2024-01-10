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
    swagger_types = {
        "legislations": "list[CommonLegislationWithImpactedSubstances]",
        "log_messages": "list[CommonLogEntry]",
    }

    attribute_map = {
        "legislations": "Legislations",
        "log_messages": "LogMessages",
    }

    subtype_mapping = {
        "Legislations": "CommonLegislationWithImpactedSubstances",
        "LogMessages": "CommonLogEntry",
    }

    discriminator = None

    def __init__(
        self,
        *,
        legislations: "Optional[List[CommonLegislationWithImpactedSubstances]]" = None,
        log_messages: "Optional[List[CommonLogEntry]]" = None,
    ) -> None:
        """GetImpactedSubstancesForBom2301Response - a model defined in Swagger

        Parameters
        ----------
            legislations: List[CommonLegislationWithImpactedSubstances], optional
            log_messages: List[CommonLogEntry], optional
        """
        self._legislations = None
        self._log_messages = None

        if legislations is not None:
            self.legislations = legislations
        if log_messages is not None:
            self.log_messages = log_messages

    @property
    def legislations(self) -> "list[CommonLegislationWithImpactedSubstances]":
        """Gets the legislations of this GetImpactedSubstancesForBom2301Response.

        Returns
        -------
        list[CommonLegislationWithImpactedSubstances]
            The legislations of this GetImpactedSubstancesForBom2301Response.
        """
        return self._legislations

    @legislations.setter
    def legislations(
        self, legislations: "list[CommonLegislationWithImpactedSubstances]"
    ) -> None:
        """Sets the legislations of this GetImpactedSubstancesForBom2301Response.

        Parameters
        ----------
        legislations: list[CommonLegislationWithImpactedSubstances]
            The legislations of this GetImpactedSubstancesForBom2301Response.
        """
        self._legislations = legislations

    @property
    def log_messages(self) -> "list[CommonLogEntry]":
        """Gets the log_messages of this GetImpactedSubstancesForBom2301Response.

        Returns
        -------
        list[CommonLogEntry]
            The log_messages of this GetImpactedSubstancesForBom2301Response.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "list[CommonLogEntry]") -> None:
        """Sets the log_messages of this GetImpactedSubstancesForBom2301Response.

        Parameters
        ----------
        log_messages: list[CommonLogEntry]
            The log_messages of this GetImpactedSubstancesForBom2301Response.
        """
        self._log_messages = log_messages

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
        if issubclass(GetImpactedSubstancesForBom2301Response, dict):
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
        if not isinstance(other, GetImpactedSubstancesForBom2301Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other