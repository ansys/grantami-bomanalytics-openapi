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


class CommonSustainabilityTransportSummary(ModelBase):
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
        "phase_summary": "CommonSustainabilityPhaseSummary",
        "summary": "list[CommonSustainabilityTransportSummaryEntry]",
    }

    attribute_map: Dict[str, str] = {
        "phase_summary": "PhaseSummary",
        "summary": "Summary",
    }

    subtype_mapping: Dict[str, str] = {
        "Summary": "CommonSustainabilityTransportSummaryEntry",
        "PhaseSummary": "CommonSustainabilityPhaseSummary",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, phase_summary: "Union[CommonSustainabilityPhaseSummary, Unset_Type]" = Unset, summary: "Union[List[CommonSustainabilityTransportSummaryEntry], Unset_Type]" = Unset,) -> None:
        """CommonSustainabilityTransportSummary - a model defined in Swagger

        Parameters
        ----------
        phase_summary: CommonSustainabilityPhaseSummary, optional
        summary: List[CommonSustainabilityTransportSummaryEntry], optional
        """
        self._summary: Union[List[CommonSustainabilityTransportSummaryEntry], Unset_Type] = Unset
        self._phase_summary: Union[CommonSustainabilityPhaseSummary, Unset_Type] = Unset

        if summary is not Unset:
            self.summary = summary
        if phase_summary is not Unset:
            self.phase_summary = phase_summary

    @property
    def summary(self) -> "Union[List[CommonSustainabilityTransportSummaryEntry], Unset_Type]":
        """Gets the summary of this CommonSustainabilityTransportSummary.

        Returns
        -------
        Union[List[CommonSustainabilityTransportSummaryEntry], Unset_Type]
            The summary of this CommonSustainabilityTransportSummary.
        """
        return self._summary

    @summary.setter
    def summary(self, summary: "Union[List[CommonSustainabilityTransportSummaryEntry], Unset_Type]") -> None:
        """Sets the summary of this CommonSustainabilityTransportSummary.

        Parameters
        ----------
        summary: Union[List[CommonSustainabilityTransportSummaryEntry], Unset_Type]
            The summary of this CommonSustainabilityTransportSummary.
        """
        # Field is not nullable
        if summary is None:
            raise ValueError("Invalid value for 'summary', must not be 'None'")
        self._summary = summary

    @property
    def phase_summary(self) -> "Union[CommonSustainabilityPhaseSummary, Unset_Type]":
        """Gets the phase_summary of this CommonSustainabilityTransportSummary.

        Returns
        -------
        Union[CommonSustainabilityPhaseSummary, Unset_Type]
            The phase_summary of this CommonSustainabilityTransportSummary.
        """
        return self._phase_summary

    @phase_summary.setter
    def phase_summary(self, phase_summary: "Union[CommonSustainabilityPhaseSummary, Unset_Type]") -> None:
        """Sets the phase_summary of this CommonSustainabilityTransportSummary.

        Parameters
        ----------
        phase_summary: Union[CommonSustainabilityPhaseSummary, Unset_Type]
            The phase_summary of this CommonSustainabilityTransportSummary.
        """
        # Field is not nullable
        if phase_summary is None:
            raise ValueError("Invalid value for 'phase_summary', must not be 'None'")
        self._phase_summary = phase_summary

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
        if not isinstance(other, CommonSustainabilityTransportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

