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

    """
    swagger_types = {
        "processes": "list[CommonSustainabilityProcessWithSustainability]",
        "substances": "list[CommonSubstanceReference]",
        "embodied_energy": "CommonValueWithUnit",
        "climate_change": "CommonValueWithUnit",
        "recyclable": "bool",
        "biodegradable": "bool",
        "functional_recycle": "bool",
        "reported_mass": "CommonValueWithUnit",
        "external_identity": "str",
        "name": "str",
        "reference_type": "str",
        "reference_value": "str",
        "id": "str",
    }

    attribute_map = {
        "processes": "Processes",
        "substances": "Substances",
        "embodied_energy": "EmbodiedEnergy",
        "climate_change": "ClimateChange",
        "recyclable": "Recyclable",
        "biodegradable": "Biodegradable",
        "functional_recycle": "FunctionalRecycle",
        "reported_mass": "ReportedMass",
        "external_identity": "ExternalIdentity",
        "name": "Name",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "id": "Id",
    }

    subtype_mapping = {
        "Processes": "CommonSustainabilityProcessWithSustainability",
        "Substances": "CommonSubstanceReference",
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
        "ReportedMass": "CommonValueWithUnit",
    }

    def __init__(
        self,
        *,
        biodegradable: "Optional[bool]" = None,
        climate_change: "Optional[CommonValueWithUnit]" = None,
        embodied_energy: "Optional[CommonValueWithUnit]" = None,
        external_identity: "Optional[str]" = None,
        functional_recycle: "Optional[bool]" = None,
        id: "Optional[str]" = None,
        name: "Optional[str]" = None,
        processes: "Optional[List[CommonSustainabilityProcessWithSustainability]]" = None,
        recyclable: "Optional[bool]" = None,
        reference_type: "Optional[str]" = None,
        reference_value: "Optional[str]" = None,
        reported_mass: "Optional[CommonValueWithUnit]" = None,
        substances: "Optional[List[CommonSubstanceReference]]" = None,
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
            substances: List[CommonSubstanceReference], optional
        """
        self._processes = None
        self._substances = None
        self._embodied_energy = None
        self._climate_change = None
        self._recyclable = None
        self._biodegradable = None
        self._functional_recycle = None
        self._reported_mass = None
        self._external_identity = None
        self._name = None
        self._reference_type = None
        self._reference_value = None
        self._id = None
        self.discriminator = None
        if processes is not None:
            self.processes = processes
        if substances is not None:
            self.substances = substances
        if embodied_energy is not None:
            self.embodied_energy = embodied_energy
        if climate_change is not None:
            self.climate_change = climate_change
        if recyclable is not None:
            self.recyclable = recyclable
        if biodegradable is not None:
            self.biodegradable = biodegradable
        if functional_recycle is not None:
            self.functional_recycle = functional_recycle
        if reported_mass is not None:
            self.reported_mass = reported_mass
        if external_identity is not None:
            self.external_identity = external_identity
        if name is not None:
            self.name = name
        if reference_type is not None:
            self.reference_type = reference_type
        if reference_value is not None:
            self.reference_value = reference_value
        if id is not None:
            self.id = id

    @property
    def processes(self) -> "list[CommonSustainabilityProcessWithSustainability]":
        """Gets the processes of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        list[CommonSustainabilityProcessWithSustainability]
            The processes of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._processes

    @processes.setter
    def processes(
        self, processes: "list[CommonSustainabilityProcessWithSustainability]"
    ) -> None:
        """Sets the processes of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        processes: list[CommonSustainabilityProcessWithSustainability]
            The processes of this CommonSustainabilityMaterialWithSustainability.
        """
        self._processes = processes

    @property
    def substances(self) -> "list[CommonSubstanceReference]":
        """Gets the substances of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        list[CommonSubstanceReference]
            The substances of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._substances

    @substances.setter
    def substances(self, substances: "list[CommonSubstanceReference]") -> None:
        """Sets the substances of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        substances: list[CommonSubstanceReference]
            The substances of this CommonSustainabilityMaterialWithSustainability.
        """
        self._substances = substances

    @property
    def embodied_energy(self) -> "CommonValueWithUnit":
        """Gets the embodied_energy of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "CommonValueWithUnit") -> None:
        """Sets the embodied_energy of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        embodied_energy: CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityMaterialWithSustainability.
        """
        self._embodied_energy = embodied_energy

    @property
    def climate_change(self) -> "CommonValueWithUnit":
        """Gets the climate_change of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        CommonValueWithUnit
            The climate_change of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "CommonValueWithUnit") -> None:
        """Sets the climate_change of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        climate_change: CommonValueWithUnit
            The climate_change of this CommonSustainabilityMaterialWithSustainability.
        """
        self._climate_change = climate_change

    @property
    def recyclable(self) -> "bool":
        """Gets the recyclable of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        bool
            The recyclable of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._recyclable

    @recyclable.setter
    def recyclable(self, recyclable: "bool") -> None:
        """Sets the recyclable of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        recyclable: bool
            The recyclable of this CommonSustainabilityMaterialWithSustainability.
        """
        self._recyclable = recyclable

    @property
    def biodegradable(self) -> "bool":
        """Gets the biodegradable of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        bool
            The biodegradable of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._biodegradable

    @biodegradable.setter
    def biodegradable(self, biodegradable: "bool") -> None:
        """Sets the biodegradable of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        biodegradable: bool
            The biodegradable of this CommonSustainabilityMaterialWithSustainability.
        """
        self._biodegradable = biodegradable

    @property
    def functional_recycle(self) -> "bool":
        """Gets the functional_recycle of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        bool
            The functional_recycle of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._functional_recycle

    @functional_recycle.setter
    def functional_recycle(self, functional_recycle: "bool") -> None:
        """Sets the functional_recycle of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        functional_recycle: bool
            The functional_recycle of this CommonSustainabilityMaterialWithSustainability.
        """
        self._functional_recycle = functional_recycle

    @property
    def reported_mass(self) -> "CommonValueWithUnit":
        """Gets the reported_mass of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        CommonValueWithUnit
            The reported_mass of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._reported_mass

    @reported_mass.setter
    def reported_mass(self, reported_mass: "CommonValueWithUnit") -> None:
        """Sets the reported_mass of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        reported_mass: CommonValueWithUnit
            The reported_mass of this CommonSustainabilityMaterialWithSustainability.
        """
        self._reported_mass = reported_mass

    @property
    def external_identity(self) -> "str":
        """Gets the external_identity of this CommonSustainabilityMaterialWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by             applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be             returned back to the client in this property. If the ExternalIdentity was not present in the input BoM,             this property is omitted.

        Returns
        -------
        str
            The external_identity of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "str") -> None:
        """Sets the external_identity of this CommonSustainabilityMaterialWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by             applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be             returned back to the client in this property. If the ExternalIdentity was not present in the input BoM,             this property is omitted.

        Parameters
        ----------
        external_identity: str
            The external_identity of this CommonSustainabilityMaterialWithSustainability.
        """
        self._external_identity = external_identity

    @property
    def name(self) -> "str":
        """Gets the name of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element.             If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM,             this property is omitted.

        Returns
        -------
        str
            The name of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element.             If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM,             this property is omitted.

        Parameters
        ----------
        name: str
            The name of this CommonSustainabilityMaterialWithSustainability.
        """
        self._name = name

    @property
    def reference_type(self) -> "str":
        """Gets the reference_type of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        str
            The reference_type of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "str") -> None:
        """Sets the reference_type of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        reference_type: str
            The reference_type of this CommonSustainabilityMaterialWithSustainability.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "str":
        """Gets the reference_value of this CommonSustainabilityMaterialWithSustainability.

        Returns
        -------
        str
            The reference_value of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "str") -> None:
        """Sets the reference_value of this CommonSustainabilityMaterialWithSustainability.

        Parameters
        ----------
        reference_value: str
            The reference_value of this CommonSustainabilityMaterialWithSustainability.
        """
        self._reference_value = reference_value

    @property
    def id(self) -> "str":
        """Gets the id of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set.             If this was set in the input BoM, its value is returned in this property.             If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        str
            The id of this CommonSustainabilityMaterialWithSustainability.
        """
        return self._id

    @id.setter
    def id(self, id: "str") -> None:
        """Sets the id of this CommonSustainabilityMaterialWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set.             If this was set in the input BoM, its value is returned in this property.             If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: str
            The id of this CommonSustainabilityMaterialWithSustainability.
        """
        self._id = id

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
        if issubclass(CommonSustainabilityMaterialWithSustainability, dict):
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
        if not isinstance(other, CommonSustainabilityMaterialWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
