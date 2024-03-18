"""
    Granta.BomAnalyticsServices.V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class CommonSustainabilityMaterialWithSustainability(ModelBase):
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
        "biodegradable": "bool",
        "climate_change": "CommonValueWithUnit",
        "embodied_energy": "CommonValueWithUnit",
        "external_identity": "str",
        "functional_recycle": "bool",
        "id": "str",
        "name": "str",
        "processes": "list[CommonSustainabilityProcessWithSustainability]",
        "recyclable": "bool",
        "reference_type": "str",
        "reference_value": "str",
        "reported_mass": "CommonValueWithUnit",
    }

    attribute_map: Dict[str, str] = {
        "biodegradable": "Biodegradable",
        "climate_change": "ClimateChange",
        "embodied_energy": "EmbodiedEnergy",
        "external_identity": "ExternalIdentity",
        "functional_recycle": "FunctionalRecycle",
        "id": "Id",
        "name": "Name",
        "processes": "Processes",
        "recyclable": "Recyclable",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "reported_mass": "ReportedMass",
    }

    subtype_mapping: Dict[str, str] = {
        "Processes": "CommonSustainabilityProcessWithSustainability",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
        "ReportedMass": "CommonValueWithUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        biodegradable: "Union[bool, None, Unset_Type]" = Unset,
        climate_change: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        embodied_energy: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
        external_identity: "Union[str, Unset_Type]" = Unset,
        functional_recycle: "Union[bool, None, Unset_Type]" = Unset,
        id: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        processes: "Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]" = Unset,
        recyclable: "Union[bool, None, Unset_Type]" = Unset,
        reference_type: "Union[str, Unset_Type]" = Unset,
        reference_value: "Union[str, Unset_Type]" = Unset,
        reported_mass: "Union[CommonValueWithUnit, Unset_Type]" = Unset,
    ) -> None:
        """CommonSustainabilityMaterialWithSustainability - a model defined in Swagger

        Parameters
        ----------
        biodegradable: bool, optional
        climate_change: CommonValueWithUnit, optional
        embodied_energy: CommonValueWithUnit, optional
        external_identity: str, optional
        functional_recycle: bool, optional
        id: str, optional
        name: str, optional
        processes: List[CommonSustainabilityProcessWithSustainability], optional
        recyclable: bool, optional
        reference_type: str, optional
        reference_value: str, optional
        reported_mass: CommonValueWithUnit, optional
        """
        self._processes: Union[
            List[CommonSustainabilityProcessWithSustainability], Unset_Type
        ] = Unset
        self._embodied_energy: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._climate_change: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._recyclable: Union[bool, None, Unset_Type] = Unset
        self._biodegradable: Union[bool, None, Unset_Type] = Unset
        self._functional_recycle: Union[bool, None, Unset_Type] = Unset
        self._reported_mass: Union[CommonValueWithUnit, Unset_Type] = Unset
        self._external_identity: Union[str, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._reference_type: Union[str, Unset_Type] = Unset
        self._reference_value: Union[str, Unset_Type] = Unset
        self._id: Union[str, Unset_Type] = Unset

        if processes is not Unset:
            self.processes = processes
        if embodied_energy is not Unset:
            self.embodied_energy = embodied_energy
        if climate_change is not Unset:
            self.climate_change = climate_change
        if recyclable is not Unset:
            self.recyclable = recyclable
        if biodegradable is not Unset:
            self.biodegradable = biodegradable
        if functional_recycle is not Unset:
            self.functional_recycle = functional_recycle
        if reported_mass is not Unset:
            self.reported_mass = reported_mass
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
    def processes(
        self,
    ) -> "Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]":
        """Gets the processes of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]
            The processes of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._processes

    @processes.setter
    def processes(
        self,
        processes: "Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]",
    ) -> None:
        """Sets the processes of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        processes: Union[List[CommonSustainabilityProcessWithSustainability], Unset_Type]
            The processes of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if processes is None:
            raise ValueError("Invalid value for 'processes', must not be 'None'")
        self._processes = processes

    @property
    def embodied_energy(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the embodied_energy of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(
        self, embodied_energy: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the embodied_energy of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        embodied_energy: Union[CommonValueWithUnit, Unset_Type]
            The embodied_energy of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if embodied_energy is None:
            raise ValueError("Invalid value for 'embodied_energy', must not be 'None'")
        self._embodied_energy = embodied_energy

    @property
    def climate_change(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the climate_change of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(
        self, climate_change: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the climate_change of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        climate_change: Union[CommonValueWithUnit, Unset_Type]
            The climate_change of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if climate_change is None:
            raise ValueError("Invalid value for 'climate_change', must not be 'None'")
        self._climate_change = climate_change

    @property
    def recyclable(self) -> "Union[bool, None, Unset_Type]":
        """Gets the recyclable of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The recyclable of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._recyclable

    @recyclable.setter
    def recyclable(self, recyclable: "Union[bool, None, Unset_Type]") -> None:
        """Sets the recyclable of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        recyclable: Union[bool, None, Unset_Type]
            The recyclable of this CommonSustainabilityMaterialWithSustainability.
        """
        self._recyclable = recyclable

    @property
    def biodegradable(self) -> "Union[bool, None, Unset_Type]":
        """Gets the biodegradable of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The biodegradable of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._biodegradable

    @biodegradable.setter
    def biodegradable(self, biodegradable: "Union[bool, None, Unset_Type]") -> None:
        """Sets the biodegradable of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        biodegradable: Union[bool, None, Unset_Type]
            The biodegradable of this CommonSustainabilityMaterialWithSustainability.
        """
        self._biodegradable = biodegradable

    @property
    def functional_recycle(self) -> "Union[bool, None, Unset_Type]":
        """Gets the functional_recycle of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The functional_recycle of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._functional_recycle

    @functional_recycle.setter
    def functional_recycle(
        self, functional_recycle: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the functional_recycle of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        functional_recycle: Union[bool, None, Unset_Type]
            The functional_recycle of this CommonSustainabilityMaterialWithSustainability.
        """
        self._functional_recycle = functional_recycle

    @property
    def reported_mass(self) -> "Union[CommonValueWithUnit, Unset_Type]":
        """Gets the reported_mass of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[CommonValueWithUnit, Unset_Type]
            The reported_mass of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._reported_mass

    @reported_mass.setter
    def reported_mass(
        self, reported_mass: "Union[CommonValueWithUnit, Unset_Type]"
    ) -> None:
        """Sets the reported_mass of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        reported_mass: Union[CommonValueWithUnit, Unset_Type]
            The reported_mass of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if reported_mass is None:
            raise ValueError("Invalid value for 'reported_mass', must not be 'None'")
        self._reported_mass = reported_mass

    @property
    def external_identity(self) -> "Union[str, Unset_Type]":
        """Gets the external_identity of this CommonSustainabilityMaterialWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, Unset_Type]
            The external_identity of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "Union[str, Unset_Type]") -> None:
        """Sets the external_identity of this CommonSustainabilityMaterialWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: Union[str, Unset_Type]
            The external_identity of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if external_identity is None:
            raise ValueError(
                "Invalid value for 'external_identity', must not be 'None'"
            )
        self._external_identity = external_identity

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def reference_type(self) -> "Union[str, Unset_Type]":
        """Gets the reference_type of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_type of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "Union[str, Unset_Type]") -> None:
        """Sets the reference_type of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        reference_type: Union[str, Unset_Type]
            The reference_type of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if reference_type is None:
            raise ValueError("Invalid value for 'reference_type', must not be 'None'")
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "Union[str, Unset_Type]":
        """Gets the reference_value of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        Union[str, Unset_Type]
            The reference_value of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "Union[str, Unset_Type]") -> None:
        """Sets the reference_value of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        reference_value: Union[str, Unset_Type]
            The reference_value of this CommonSustainabilityMaterialWithSustainability.
        """
        # Field is not nullable
        if reference_value is None:
            raise ValueError("Invalid value for 'reference_value', must not be 'None'")
        self._reference_value = reference_value

    @property
    def id(self) -> "Union[str, Unset_Type]":
        """Gets the id of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        Union[str, Unset_Type]
            The id of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._id

    @id.setter
    def id(self, id: "Union[str, Unset_Type]") -> None:
        """Sets the id of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: Union[str, Unset_Type]
            The id of this CommonSustainabilityMaterialWithSustainability.
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
        if not isinstance(other, CommonSustainabilityMaterialWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
