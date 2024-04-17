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


class CommonTransportReference(ModelBase):
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
        "id": "str",
        "reference_type": "str",
        "reference_value": "str",
    }

    attribute_map: Dict[str, str] = {
        "id": "Id",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
    }

    subtype_mapping: Dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, id: "Union[str, Unset_Type]" = Unset, reference_type: "Union[str, Unset_Type]" = Unset, reference_value: "Union[str, Unset_Type]" = Unset,) -> None:
        """CommonTransportReference - a model defined in Swagger

        Parameters
        ----------
        id: str, optional
        reference_type: str, optional
        reference_value: str, optional
        """
        self._reference_type: Union[str, Unset_Type] = Unset
        self._reference_value: Union[str, Unset_Type] = Unset
        self._id: Union[str, Unset_Type] = Unset

        if reference_type is not Unset:
            self.reference_type = reference_type
        if reference_value is not Unset:
            self.reference_value = reference_value
        if id is not Unset:
            self.id = id

    @property
    def reference_type(self) -> "Union[str, Unset_Type]":
        """Gets the reference_type of this CommonTransportReference.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_type of this CommonTransportReference.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "Union[str, Unset_Type]") -> None:
        """Sets the reference_type of this CommonTransportReference.

        Parameters
        ----------
        reference_type: Union[str, Unset_Type]
            The reference_type of this CommonTransportReference.
        """
        # Field is not nullable
        if reference_type is None:
            raise ValueError("Invalid value for 'reference_type', must not be 'None'")
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "Union[str, Unset_Type]":
        """Gets the reference_value of this CommonTransportReference.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_value of this CommonTransportReference.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "Union[str, Unset_Type]") -> None:
        """Sets the reference_value of this CommonTransportReference.

        Parameters
        ----------
        reference_value: Union[str, Unset_Type]
            The reference_value of this CommonTransportReference.
        """
        # Field is not nullable
        if reference_value is None:
            raise ValueError("Invalid value for 'reference_value', must not be 'None'")
        self._reference_value = reference_value

    @property
    def id(self) -> "Union[str, Unset_Type]":
        """Gets the id of this CommonTransportReference.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        Union[str, Unset_Type]
            The id of this CommonTransportReference.
        """
        return self._id

    @id.setter
    def id(self, id: "Union[str, Unset_Type]") -> None:
        """Sets the id of this CommonTransportReference.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: Union[str, Unset_Type]
            The id of this CommonTransportReference.
        """
        # Field is not nullable
        if id is None:
            raise ValueError("Invalid value for 'id', must not be 'None'")
        self._id = id

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
        if not isinstance(other, CommonTransportReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

