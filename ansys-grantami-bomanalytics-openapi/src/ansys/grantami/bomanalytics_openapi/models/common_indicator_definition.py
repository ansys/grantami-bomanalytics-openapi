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


class CommonIndicatorDefinition(ModelBase):
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
        "default_threshold_percentage": "float",
        "ignore_exemptions": "bool",
        "ignore_process_chemicals": "bool",
        "legislation_ids": "list[str]",
        "name": "str",
        "type": "str",
    }

    attribute_map = {
        "default_threshold_percentage": "DefaultThresholdPercentage",
        "ignore_exemptions": "IgnoreExemptions",
        "ignore_process_chemicals": "IgnoreProcessChemicals",
        "legislation_ids": "LegislationIds",
        "name": "Name",
        "type": "Type",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        default_threshold_percentage: "Optional[float]" = None,
        ignore_exemptions: "Optional[bool]" = None,
        ignore_process_chemicals: "Optional[bool]" = None,
        legislation_ids: "Optional[List[str]]" = None,
        name: "Optional[str]" = None,
        type: "Optional[str]" = None,
    ) -> None:
        """CommonIndicatorDefinition - a model defined in Swagger

        Parameters
        ----------
            default_threshold_percentage: float, optional
            ignore_exemptions: bool, optional
            ignore_process_chemicals: bool, optional
            legislation_ids: List[str], optional
            name: str, optional
            type: str, optional
        """
        self._name = None
        self._legislation_ids = None
        self._default_threshold_percentage = None
        self._ignore_exemptions = None
        self._ignore_process_chemicals = None
        self._type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if legislation_ids is not None:
            self.legislation_ids = legislation_ids
        if default_threshold_percentage is not None:
            self.default_threshold_percentage = default_threshold_percentage
        if ignore_exemptions is not None:
            self.ignore_exemptions = ignore_exemptions
        if ignore_process_chemicals is not None:
            self.ignore_process_chemicals = ignore_process_chemicals
        if type is not None:
            self.type = type

    @property
    def name(self) -> "str":
        """Gets the name of this CommonIndicatorDefinition.

        Returns
        -------
        str
            The name of this CommonIndicatorDefinition.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this CommonIndicatorDefinition.

        Parameters
        ----------
        name: str
            The name of this CommonIndicatorDefinition.
        """
        self._name = name

    @property
    def legislation_ids(self) -> "list[str]":
        """Gets the legislation_ids of this CommonIndicatorDefinition.

        Returns
        -------
        list[str]
            The legislation_ids of this CommonIndicatorDefinition.
        """
        return self._legislation_ids

    @legislation_ids.setter
    def legislation_ids(self, legislation_ids: "list[str]") -> None:
        """Sets the legislation_ids of this CommonIndicatorDefinition.

        Parameters
        ----------
        legislation_ids: list[str]
            The legislation_ids of this CommonIndicatorDefinition.
        """
        self._legislation_ids = legislation_ids

    @property
    def default_threshold_percentage(self) -> "float":
        """Gets the default_threshold_percentage of this CommonIndicatorDefinition.

        Returns
        -------
        float
            The default_threshold_percentage of this CommonIndicatorDefinition.
        """
        return self._default_threshold_percentage

    @default_threshold_percentage.setter
    def default_threshold_percentage(
        self, default_threshold_percentage: "float"
    ) -> None:
        """Sets the default_threshold_percentage of this CommonIndicatorDefinition.

        Parameters
        ----------
        default_threshold_percentage: float
            The default_threshold_percentage of this CommonIndicatorDefinition.
        """
        self._default_threshold_percentage = default_threshold_percentage

    @property
    def ignore_exemptions(self) -> "bool":
        """Gets the ignore_exemptions of this CommonIndicatorDefinition.

        Returns
        -------
        bool
            The ignore_exemptions of this CommonIndicatorDefinition.
        """
        return self._ignore_exemptions

    @ignore_exemptions.setter
    def ignore_exemptions(self, ignore_exemptions: "bool") -> None:
        """Sets the ignore_exemptions of this CommonIndicatorDefinition.

        Parameters
        ----------
        ignore_exemptions: bool
            The ignore_exemptions of this CommonIndicatorDefinition.
        """
        self._ignore_exemptions = ignore_exemptions

    @property
    def ignore_process_chemicals(self) -> "bool":
        """Gets the ignore_process_chemicals of this CommonIndicatorDefinition.

        Returns
        -------
        bool
            The ignore_process_chemicals of this CommonIndicatorDefinition.
        """
        return self._ignore_process_chemicals

    @ignore_process_chemicals.setter
    def ignore_process_chemicals(self, ignore_process_chemicals: "bool") -> None:
        """Sets the ignore_process_chemicals of this CommonIndicatorDefinition.

        Parameters
        ----------
        ignore_process_chemicals: bool
            The ignore_process_chemicals of this CommonIndicatorDefinition.
        """
        self._ignore_process_chemicals = ignore_process_chemicals

    @property
    def type(self) -> "str":
        """Gets the type of this CommonIndicatorDefinition.

        Returns
        -------
        str
            The type of this CommonIndicatorDefinition.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this CommonIndicatorDefinition.

        Parameters
        ----------
        type: str
            The type of this CommonIndicatorDefinition.
        """
        self._type = type

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
        if issubclass(CommonIndicatorDefinition, dict):
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
        if not isinstance(other, CommonIndicatorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
