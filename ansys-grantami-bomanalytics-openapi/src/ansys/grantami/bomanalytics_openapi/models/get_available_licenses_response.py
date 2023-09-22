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


class GetAvailableLicensesResponse(ModelBase):
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
        "restricted_substances": "bool",
        "sustainability": "bool",
        "log_messages": "list[CommonLogEntry]",
    }

    attribute_map = {
        "restricted_substances": "RestrictedSubstances",
        "sustainability": "Sustainability",
        "log_messages": "LogMessages",
    }

    subtype_mapping = {
        "LogMessages": "CommonLogEntry",
    }

    def __init__(
        self,
        *,
        log_messages: "Optional[List[CommonLogEntry]]" = None,
        restricted_substances: "Optional[bool]" = None,
        sustainability: "Optional[bool]" = None
    ) -> None:
        """GetAvailableLicensesResponse - a model defined in Swagger

        Parameters
        ----------
            log_messages: List[CommonLogEntry], optional
            restricted_substances: bool, optional
            sustainability: bool, optional
        """
        self._restricted_substances = None
        self._sustainability = None
        self._log_messages = None
        self.discriminator = None
        if restricted_substances is not None:
            self.restricted_substances = restricted_substances
        if sustainability is not None:
            self.sustainability = sustainability
        if log_messages is not None:
            self.log_messages = log_messages

    @property
    def restricted_substances(self) -> "bool":
        """Gets the restricted_substances of this GetAvailableLicensesResponse.

        Returns
        -------
        bool
            The restricted_substances of this GetAvailableLicensesResponse.
        """
        return self._restricted_substances

    @restricted_substances.setter
    def restricted_substances(self, restricted_substances: "bool") -> None:
        """Sets the restricted_substances of this GetAvailableLicensesResponse.

        Parameters
        ----------
        restricted_substances: bool
            The restricted_substances of this GetAvailableLicensesResponse.
        """
        self._restricted_substances = restricted_substances

    @property
    def sustainability(self) -> "bool":
        """Gets the sustainability of this GetAvailableLicensesResponse.

        Returns
        -------
        bool
            The sustainability of this GetAvailableLicensesResponse.
        """
        return self._sustainability

    @sustainability.setter
    def sustainability(self, sustainability: "bool") -> None:
        """Sets the sustainability of this GetAvailableLicensesResponse.

        Parameters
        ----------
        sustainability: bool
            The sustainability of this GetAvailableLicensesResponse.
        """
        self._sustainability = sustainability

    @property
    def log_messages(self) -> "list[CommonLogEntry]":
        """Gets the log_messages of this GetAvailableLicensesResponse.

        Returns
        -------
        list[CommonLogEntry]
            The log_messages of this GetAvailableLicensesResponse.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "list[CommonLogEntry]") -> None:
        """Sets the log_messages of this GetAvailableLicensesResponse.

        Parameters
        ----------
        log_messages: list[CommonLogEntry]
            The log_messages of this GetAvailableLicensesResponse.
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
        if issubclass(GetAvailableLicensesResponse, dict):
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
        if not isinstance(other, GetAvailableLicensesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
