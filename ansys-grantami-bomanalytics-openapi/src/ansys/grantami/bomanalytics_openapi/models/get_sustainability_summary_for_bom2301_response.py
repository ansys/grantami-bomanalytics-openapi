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


class GetSustainabilitySummaryForBom2301Response(ModelBase):
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
        "log_messages": "list[CommonLogEntry]",
        "material_summary": "CommonSustainabilityMaterialSummary",
        "process_summary": "CommonSustainabilityProcessSummary",
        "transport_summary": "CommonSustainabilityTransportSummary",
    }

    attribute_map = {
        "log_messages": "LogMessages",
        "material_summary": "MaterialSummary",
        "process_summary": "ProcessSummary",
        "transport_summary": "TransportSummary",
    }

    subtype_mapping = {
        "MaterialSummary": "CommonSustainabilityMaterialSummary",
        "ProcessSummary": "CommonSustainabilityProcessSummary",
        "TransportSummary": "CommonSustainabilityTransportSummary",
        "LogMessages": "CommonLogEntry",
    }

    def __init__(
        self,
        *,
        log_messages: "Optional[List[CommonLogEntry]]" = None,
        material_summary: "Optional[CommonSustainabilityMaterialSummary]" = None,
        process_summary: "Optional[CommonSustainabilityProcessSummary]" = None,
        transport_summary: "Optional[CommonSustainabilityTransportSummary]" = None,
    ) -> None:
        """GetSustainabilitySummaryForBom2301Response - a model defined in Swagger

        Parameters
        ----------
            log_messages: List[CommonLogEntry], optional
            material_summary: CommonSustainabilityMaterialSummary, optional
            process_summary: CommonSustainabilityProcessSummary, optional
            transport_summary: CommonSustainabilityTransportSummary, optional
        """
        self._material_summary = None
        self._process_summary = None
        self._transport_summary = None
        self._log_messages = None
        self.discriminator = None
        if material_summary is not None:
            self.material_summary = material_summary
        if process_summary is not None:
            self.process_summary = process_summary
        if transport_summary is not None:
            self.transport_summary = transport_summary
        if log_messages is not None:
            self.log_messages = log_messages

    @property
    def material_summary(self) -> "CommonSustainabilityMaterialSummary":
        """Gets the material_summary of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        CommonSustainabilityMaterialSummary
            The material_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._material_summary

    @material_summary.setter
    def material_summary(
        self, material_summary: "CommonSustainabilityMaterialSummary"
    ) -> None:
        """Sets the material_summary of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        material_summary: CommonSustainabilityMaterialSummary
            The material_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        self._material_summary = material_summary

    @property
    def process_summary(self) -> "CommonSustainabilityProcessSummary":
        """Gets the process_summary of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        CommonSustainabilityProcessSummary
            The process_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._process_summary

    @process_summary.setter
    def process_summary(
        self, process_summary: "CommonSustainabilityProcessSummary"
    ) -> None:
        """Sets the process_summary of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        process_summary: CommonSustainabilityProcessSummary
            The process_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        self._process_summary = process_summary

    @property
    def transport_summary(self) -> "CommonSustainabilityTransportSummary":
        """Gets the transport_summary of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        CommonSustainabilityTransportSummary
            The transport_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._transport_summary

    @transport_summary.setter
    def transport_summary(
        self, transport_summary: "CommonSustainabilityTransportSummary"
    ) -> None:
        """Sets the transport_summary of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        transport_summary: CommonSustainabilityTransportSummary
            The transport_summary of this GetSustainabilitySummaryForBom2301Response.
        """
        self._transport_summary = transport_summary

    @property
    def log_messages(self) -> "list[CommonLogEntry]":
        """Gets the log_messages of this GetSustainabilitySummaryForBom2301Response.

        Returns
        -------
        list[CommonLogEntry]
            The log_messages of this GetSustainabilitySummaryForBom2301Response.
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages: "list[CommonLogEntry]") -> None:
        """Sets the log_messages of this GetSustainabilitySummaryForBom2301Response.

        Parameters
        ----------
        log_messages: list[CommonLogEntry]
            The log_messages of this GetSustainabilitySummaryForBom2301Response.
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
        if issubclass(GetSustainabilitySummaryForBom2301Response, dict):
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
        if not isinstance(other, GetSustainabilitySummaryForBom2301Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
