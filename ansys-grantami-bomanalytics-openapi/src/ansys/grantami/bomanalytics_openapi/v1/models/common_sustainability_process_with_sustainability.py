# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class CommonSustainabilityProcessWithSustainability(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "climate_change": "CommonValueWithUnit",
        "embodied_energy": "CommonValueWithUnit",
        "external_identity": "str",
        "id": "str",
        "name": "str",
        "reference_type": "str",
        "reference_value": "str",
        "transport_stages": "list[CommonSustainabilityTransportWithSustainability]",
    }

    attribute_map: dict[str, str] = {
        "climate_change": "ClimateChange",
        "embodied_energy": "EmbodiedEnergy",
        "external_identity": "ExternalIdentity",
        "id": "Id",
        "name": "Name",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "transport_stages": "TransportStages",
    }

    subtype_mapping: dict[str, str] = {
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
        "TransportStages": "CommonSustainabilityTransportWithSustainability",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        climate_change: "CommonValueWithUnit | Unset_Type" = Unset,
        embodied_energy: "CommonValueWithUnit | Unset_Type" = Unset,
        external_identity: "str | None | Unset_Type" = Unset,
        id: "str | None | Unset_Type" = Unset,
        name: "str | None | Unset_Type" = Unset,
        reference_type: "str | None | Unset_Type" = Unset,
        reference_value: "str | None | Unset_Type" = Unset,
        transport_stages: "list[CommonSustainabilityTransportWithSustainability] | None | Unset_Type" = Unset,
    ) -> None:
        """CommonSustainabilityProcessWithSustainability - a model defined in Swagger

        Parameters
        ----------
        climate_change: CommonValueWithUnit, optional
        embodied_energy: CommonValueWithUnit, optional
        external_identity: str | None, optional
        id: str | None, optional
        name: str | None, optional
        reference_type: str | None, optional
        reference_value: str | None, optional
        transport_stages: list[CommonSustainabilityTransportWithSustainability] | None, optional
        """
        self._embodied_energy: CommonValueWithUnit | Unset_Type = Unset
        self._climate_change: CommonValueWithUnit | Unset_Type = Unset
        self._transport_stages: (
            list[CommonSustainabilityTransportWithSustainability] | None | Unset_Type
        ) = Unset
        self._external_identity: str | None | Unset_Type = Unset
        self._name: str | None | Unset_Type = Unset
        self._reference_type: str | None | Unset_Type = Unset
        self._reference_value: str | None | Unset_Type = Unset
        self._id: str | None | Unset_Type = Unset

        if embodied_energy is not Unset:
            self.embodied_energy = embodied_energy
        if climate_change is not Unset:
            self.climate_change = climate_change
        if transport_stages is not Unset:
            self.transport_stages = transport_stages
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
    def embodied_energy(self) -> "CommonValueWithUnit | Unset_Type":
        """Gets the embodied_energy of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        CommonValueWithUnit | Unset_Type
            The embodied_energy of this CommonSustainabilityProcessWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "CommonValueWithUnit | Unset_Type") -> None:
        """Sets the embodied_energy of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        embodied_energy: CommonValueWithUnit | Unset_Type
            The embodied_energy of this CommonSustainabilityProcessWithSustainability.
        """
        # Field is not nullable
        if embodied_energy is None:
            raise ValueError("Invalid value for 'embodied_energy', must not be 'None'")
        self._embodied_energy = embodied_energy

    @property
    def climate_change(self) -> "CommonValueWithUnit | Unset_Type":
        """Gets the climate_change of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        CommonValueWithUnit | Unset_Type
            The climate_change of this CommonSustainabilityProcessWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "CommonValueWithUnit | Unset_Type") -> None:
        """Sets the climate_change of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        climate_change: CommonValueWithUnit | Unset_Type
            The climate_change of this CommonSustainabilityProcessWithSustainability.
        """
        # Field is not nullable
        if climate_change is None:
            raise ValueError("Invalid value for 'climate_change', must not be 'None'")
        self._climate_change = climate_change

    @property
    def transport_stages(
        self,
    ) -> "list[CommonSustainabilityTransportWithSustainability] | None | Unset_Type":
        """Gets the transport_stages of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        list[CommonSustainabilityTransportWithSustainability] | None | Unset_Type
            The transport_stages of this CommonSustainabilityProcessWithSustainability.
        """
        return self._transport_stages

    @transport_stages.setter
    def transport_stages(
        self,
        transport_stages: "list[CommonSustainabilityTransportWithSustainability] | None | Unset_Type",
    ) -> None:
        """Sets the transport_stages of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        transport_stages: list[CommonSustainabilityTransportWithSustainability] | None | Unset_Type
            The transport_stages of this CommonSustainabilityProcessWithSustainability.
        """
        self._transport_stages = transport_stages

    @property
    def external_identity(self) -> "str | None | Unset_Type":
        """Gets the external_identity of this CommonSustainabilityProcessWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        str | None | Unset_Type
            The external_identity of this CommonSustainabilityProcessWithSustainability.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "str | None | Unset_Type") -> None:
        """Sets the external_identity of this CommonSustainabilityProcessWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: str | None | Unset_Type
            The external_identity of this CommonSustainabilityProcessWithSustainability.
        """
        self._external_identity = external_identity

    @property
    def name(self) -> "str | None | Unset_Type":
        """Gets the name of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        str | None | Unset_Type
            The name of this CommonSustainabilityProcessWithSustainability.
        """
        return self._name

    @name.setter
    def name(self, name: "str | None | Unset_Type") -> None:
        """Sets the name of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: str | None | Unset_Type
            The name of this CommonSustainabilityProcessWithSustainability.
        """
        self._name = name

    @property
    def reference_type(self) -> "str | None | Unset_Type":
        """Gets the reference_type of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        str | None | Unset_Type
            The reference_type of this CommonSustainabilityProcessWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "str | None | Unset_Type") -> None:
        """Sets the reference_type of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        reference_type: str | None | Unset_Type
            The reference_type of this CommonSustainabilityProcessWithSustainability.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "str | None | Unset_Type":
        """Gets the reference_value of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        str | None | Unset_Type
            The reference_value of this CommonSustainabilityProcessWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "str | None | Unset_Type") -> None:
        """Sets the reference_value of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        reference_value: str | None | Unset_Type
            The reference_value of this CommonSustainabilityProcessWithSustainability.
        """
        self._reference_value = reference_value

    @property
    def id(self) -> "str | None | Unset_Type":
        """Gets the id of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        str | None | Unset_Type
            The id of this CommonSustainabilityProcessWithSustainability.
        """
        return self._id

    @id.setter
    def id(self, id: "str | None | Unset_Type") -> None:
        """Sets the id of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: str | None | Unset_Type
            The id of this CommonSustainabilityProcessWithSustainability.
        """
        self._id = id

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, CommonSustainabilityProcessWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
