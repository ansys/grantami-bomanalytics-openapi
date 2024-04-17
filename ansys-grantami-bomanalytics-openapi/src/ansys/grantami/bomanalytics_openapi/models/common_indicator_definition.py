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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "default_threshold_percentage": "float",
        "ignore_exemptions": "bool",
        "ignore_process_chemicals": "bool",
        "legislation_ids": "list[str]",
        "name": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_threshold_percentage": "DefaultThresholdPercentage",
        "ignore_exemptions": "IgnoreExemptions",
        "ignore_process_chemicals": "IgnoreProcessChemicals",
        "legislation_ids": "LegislationIds",
        "name": "Name",
        "type": "Type",
    }

    subtype_mapping: Dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, default_threshold_percentage: "Union[float, Unset_Type]" = Unset, ignore_exemptions: "Union[bool, Unset_Type]" = Unset, ignore_process_chemicals: "Union[bool, Unset_Type]" = Unset, legislation_ids: "Union[List[str], Unset_Type]" = Unset, name: "Union[str, Unset_Type]" = Unset, type: "Union[str, Unset_Type]" = Unset,) -> None:
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
        self._name: Union[str, Unset_Type] = Unset
        self._legislation_ids: Union[List[str], Unset_Type] = Unset
        self._default_threshold_percentage: Union[float, Unset_Type] = Unset
        self._ignore_exemptions: Union[bool, Unset_Type] = Unset
        self._ignore_process_chemicals: Union[bool, Unset_Type] = Unset
        self._type: Union[str, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if legislation_ids is not Unset:
            self.legislation_ids = legislation_ids
        if default_threshold_percentage is not Unset:
            self.default_threshold_percentage = default_threshold_percentage
        if ignore_exemptions is not Unset:
            self.ignore_exemptions = ignore_exemptions
        if ignore_process_chemicals is not Unset:
            self.ignore_process_chemicals = ignore_process_chemicals
        if type is not Unset:
            self.type = type

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this CommonIndicatorDefinition.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this CommonIndicatorDefinition.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this CommonIndicatorDefinition.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this CommonIndicatorDefinition.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def legislation_ids(self) -> "Union[List[str], Unset_Type]":
        """Gets the legislation_ids of this CommonIndicatorDefinition.

        Returns
        -------
        Union[List[str], Unset_Type]
            The legislation_ids of this CommonIndicatorDefinition.
        """
        return self._legislation_ids

    @legislation_ids.setter
    def legislation_ids(self, legislation_ids: "Union[List[str], Unset_Type]") -> None:
        """Sets the legislation_ids of this CommonIndicatorDefinition.

        Parameters
        ----------
        legislation_ids: Union[List[str], Unset_Type]
            The legislation_ids of this CommonIndicatorDefinition.
        """
        # Field is not nullable
        if legislation_ids is None:
            raise ValueError("Invalid value for 'legislation_ids', must not be 'None'")
        self._legislation_ids = legislation_ids

    @property
    def default_threshold_percentage(self) -> "Union[float, Unset_Type]":
        """Gets the default_threshold_percentage of this CommonIndicatorDefinition.

        Returns
        -------
        Union[float, Unset_Type]
            The default_threshold_percentage of this CommonIndicatorDefinition.
        """
        return self._default_threshold_percentage

    @default_threshold_percentage.setter
    def default_threshold_percentage(self, default_threshold_percentage: "Union[float, Unset_Type]") -> None:
        """Sets the default_threshold_percentage of this CommonIndicatorDefinition.

        Parameters
        ----------
        default_threshold_percentage: Union[float, Unset_Type]
            The default_threshold_percentage of this CommonIndicatorDefinition.
        """
        # Field is not nullable
        if default_threshold_percentage is None:
            raise ValueError("Invalid value for 'default_threshold_percentage', must not be 'None'")
        self._default_threshold_percentage = default_threshold_percentage

    @property
    def ignore_exemptions(self) -> "Union[bool, Unset_Type]":
        """Gets the ignore_exemptions of this CommonIndicatorDefinition.

        Returns
        -------
        Union[bool, Unset_Type]
            The ignore_exemptions of this CommonIndicatorDefinition.
        """
        return self._ignore_exemptions

    @ignore_exemptions.setter
    def ignore_exemptions(self, ignore_exemptions: "Union[bool, Unset_Type]") -> None:
        """Sets the ignore_exemptions of this CommonIndicatorDefinition.

        Parameters
        ----------
        ignore_exemptions: Union[bool, Unset_Type]
            The ignore_exemptions of this CommonIndicatorDefinition.
        """
        # Field is not nullable
        if ignore_exemptions is None:
            raise ValueError("Invalid value for 'ignore_exemptions', must not be 'None'")
        self._ignore_exemptions = ignore_exemptions

    @property
    def ignore_process_chemicals(self) -> "Union[bool, Unset_Type]":
        """Gets the ignore_process_chemicals of this CommonIndicatorDefinition.

        Returns
        -------
        Union[bool, Unset_Type]
            The ignore_process_chemicals of this CommonIndicatorDefinition.
        """
        return self._ignore_process_chemicals

    @ignore_process_chemicals.setter
    def ignore_process_chemicals(self, ignore_process_chemicals: "Union[bool, Unset_Type]") -> None:
        """Sets the ignore_process_chemicals of this CommonIndicatorDefinition.

        Parameters
        ----------
        ignore_process_chemicals: Union[bool, Unset_Type]
            The ignore_process_chemicals of this CommonIndicatorDefinition.
        """
        # Field is not nullable
        if ignore_process_chemicals is None:
            raise ValueError("Invalid value for 'ignore_process_chemicals', must not be 'None'")
        self._ignore_process_chemicals = ignore_process_chemicals

    @property
    def type(self) -> "Union[str, Unset_Type]":
        """Gets the type of this CommonIndicatorDefinition.

        Returns
        -------
        Union[str, Unset_Type]
            The type of this CommonIndicatorDefinition.
        """
        return self._type

    @type.setter
    def type(self, type: "Union[str, Unset_Type]") -> None:
        """Sets the type of this CommonIndicatorDefinition.

        Parameters
        ----------
        type: Union[str, Unset_Type]
            The type of this CommonIndicatorDefinition.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
        if not isinstance(other, CommonIndicatorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

