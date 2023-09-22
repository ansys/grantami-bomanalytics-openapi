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


class GetComplianceForPartsResponse(ModelBase):
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

    """
    swagger_types = {
        "parts": "list[CommonPartWithCompliance]",
        "log_messages": "list[CommonLogEntry]",
    }

    attribute_map = {
        "parts": "Parts",
        "log_messages": "LogMessages",
    }

    subtype_mapping = {
        "Parts": "CommonPartWithCompliance",
        "LogMessages": "CommonLogEntry",
    }

    def __init__(
        self,
        *,
        log_messages: "Optional[List[CommonLogEntry]]" = None,
        parts: "Optional[List[CommonPartWithCompliance]]" = None
    ) -> None:
        """GetComplianceForPartsResponse - a model defined in Swagger

        Parameters
        ----------
            log_messages: List[CommonLogEntry], optional
            parts: List[CommonPartWithCompliance], optional
        """
        self._parts = None
        self._log_messages = None
        self.discriminator = None
        if parts is not None:
            self.parts = parts
        if log_messages is not None:
            self.log_messages = log_messages

    @property
    def parts(self) -> "list[CommonPartWithCompliance]":
        """Gets the parts of this GetComplianceForPartsResponse.

        Returns
        -------
        list[CommonPartWithCompliance]
            The parts of this GetComplianceForPartsResponse.
        """
        return self._parts

    @parts.setter
    def parts(self, parts: "list[CommonPartWithCompliance]") -> None:
        """Sets the parts of this GetComplianceForPartsResponse.

        Parameters
        ----------
        parts: list[CommonPartWithCompliance]
            The parts of this GetComplianceForPartsResponse.
        """
        self._parts = parts

    @property
    def log_messages(self) -> "list[CommonLogEntry]":
        """Gets the log_messages of this GetComplianceForPartsResponse.

        Returns
        -------
        list[CommonLogEntry]
            The log_messages of this GetComplianceForPartsResponse.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "list[CommonLogEntry]") -> None:
        """Sets the log_messages of this GetComplianceForPartsResponse.

        Parameters
        ----------
        log_messages: list[CommonLogEntry]
            The log_messages of this GetComplianceForPartsResponse.
        """
        self._log_messages = log_messages

    def get_real_child_model(self, data: ModelBase) -> str:
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
        if issubclass(GetComplianceForPartsResponse, dict):
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
        if not isinstance(other, GetComplianceForPartsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
