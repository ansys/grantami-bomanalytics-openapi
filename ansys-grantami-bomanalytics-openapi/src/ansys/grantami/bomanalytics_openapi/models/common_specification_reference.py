# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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


class CommonSpecificationReference(ModelBase):
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
        "external_identity": "str",
        "id": "str",
        "name": "str",
        "reference_type": "str",
        "reference_value": "str",
    }

    attribute_map: Dict[str, str] = {
        "external_identity": "ExternalIdentity",
        "id": "Id",
        "name": "Name",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        external_identity: "Union[str, Unset_Type]" = Unset,
        id: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        reference_type: "Union[str, Unset_Type]" = Unset,
        reference_value: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """CommonSpecificationReference - a model defined in Swagger

        Parameters
        ----------
        external_identity: str, optional
        id: str, optional
        name: str, optional
        reference_type: str, optional
        reference_value: str, optional
        """
        self._external_identity: Union[str, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._reference_type: Union[str, Unset_Type] = Unset
        self._reference_value: Union[str, Unset_Type] = Unset
        self._id: Union[str, Unset_Type] = Unset

        if external_identity is not Unset:
            self.external_identity = external_identity
        if name is not Unset:
            self.name = name
        if reference_type is not Unset:
            self.reference_type = reference_type
        if reference_value is not Unset:
            self.reference_value = reference_value
        if id is not Unset:
            self.id = id

    @property
    def external_identity(self) -> "Union[str, Unset_Type]":
        """Gets the external_identity of this CommonSpecificationReference.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, Unset_Type]
            The external_identity of this CommonSpecificationReference.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "Union[str, Unset_Type]") -> None:
        """Sets the external_identity of this CommonSpecificationReference.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: Union[str, Unset_Type]
            The external_identity of this CommonSpecificationReference.
        """
        # Field is not nullable
        if external_identity is None:
            raise ValueError("Invalid value for 'external_identity', must not be 'None'")
        self._external_identity = external_identity

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this CommonSpecificationReference.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this CommonSpecificationReference.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this CommonSpecificationReference.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this CommonSpecificationReference.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def reference_type(self) -> "Union[str, Unset_Type]":
        """Gets the reference_type of this CommonSpecificationReference.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_type of this CommonSpecificationReference.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "Union[str, Unset_Type]") -> None:
        """Sets the reference_type of this CommonSpecificationReference.

        Parameters
        ----------
        reference_type: Union[str, Unset_Type]
            The reference_type of this CommonSpecificationReference.
        """
        # Field is not nullable
        if reference_type is None:
            raise ValueError("Invalid value for 'reference_type', must not be 'None'")
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "Union[str, Unset_Type]":
        """Gets the reference_value of this CommonSpecificationReference.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_value of this CommonSpecificationReference.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "Union[str, Unset_Type]") -> None:
        """Sets the reference_value of this CommonSpecificationReference.

        Parameters
        ----------
        reference_value: Union[str, Unset_Type]
            The reference_value of this CommonSpecificationReference.
        """
        # Field is not nullable
        if reference_value is None:
            raise ValueError("Invalid value for 'reference_value', must not be 'None'")
        self._reference_value = reference_value

    @property
    def id(self) -> "Union[str, Unset_Type]":
        """Gets the id of this CommonSpecificationReference.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        Union[str, Unset_Type]
            The id of this CommonSpecificationReference.
        """
        return self._id

    @id.setter
    def id(self, id: "Union[str, Unset_Type]") -> None:
        """Sets the id of this CommonSpecificationReference.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: Union[str, Unset_Type]
            The id of this CommonSpecificationReference.
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
        if not isinstance(other, CommonSpecificationReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
