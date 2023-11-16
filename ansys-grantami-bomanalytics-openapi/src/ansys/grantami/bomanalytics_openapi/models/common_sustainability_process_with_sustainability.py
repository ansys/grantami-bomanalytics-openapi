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


class CommonSustainabilityProcessWithSustainability(ModelBase):
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
    swagger_types = {
        "climate_change": "CommonValueWithUnit",
        "embodied_energy": "CommonValueWithUnit",
        "external_identity": "str",
        "id": "str",
        "name": "str",
        "reference_type": "str",
        "reference_value": "str",
    }

    attribute_map = {
        "climate_change": "ClimateChange",
        "embodied_energy": "EmbodiedEnergy",
        "external_identity": "ExternalIdentity",
        "id": "Id",
        "name": "Name",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
    }

    subtype_mapping = {
        "EmbodiedEnergy": "CommonValueWithUnit",
        "ClimateChange": "CommonValueWithUnit",
    }

    discriminator = None

    def __init__(
        self,
        *,
        climate_change: "Optional[CommonValueWithUnit]" = None,
        embodied_energy: "Optional[CommonValueWithUnit]" = None,
        external_identity: "Optional[str]" = None,
        id: "Optional[str]" = None,
        name: "Optional[str]" = None,
        reference_type: "Optional[str]" = None,
        reference_value: "Optional[str]" = None,
    ) -> None:
        """CommonSustainabilityProcessWithSustainability - a model defined in Swagger

        Parameters
        ----------
            climate_change: CommonValueWithUnit, optional
            embodied_energy: CommonValueWithUnit, optional
            external_identity: str, optional
            id: str, optional
            name: str, optional
            reference_type: str, optional
            reference_value: str, optional
        """
        self._embodied_energy = None
        self._climate_change = None
        self._external_identity = None
        self._name = None
        self._reference_type = None
        self._reference_value = None
        self._id = None

        if embodied_energy is not None:
            self.embodied_energy = embodied_energy
        if climate_change is not None:
            self.climate_change = climate_change
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
    def embodied_energy(self) -> "CommonValueWithUnit":
        """Gets the embodied_energy of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityProcessWithSustainability.
        """
        return self._embodied_energy

    @embodied_energy.setter
    def embodied_energy(self, embodied_energy: "CommonValueWithUnit") -> None:
        """Sets the embodied_energy of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        embodied_energy: CommonValueWithUnit
            The embodied_energy of this CommonSustainabilityProcessWithSustainability.
        """
        self._embodied_energy = embodied_energy

    @property
    def climate_change(self) -> "CommonValueWithUnit":
        """Gets the climate_change of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        CommonValueWithUnit
            The climate_change of this CommonSustainabilityProcessWithSustainability.
        """
        return self._climate_change

    @climate_change.setter
    def climate_change(self, climate_change: "CommonValueWithUnit") -> None:
        """Sets the climate_change of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        climate_change: CommonValueWithUnit
            The climate_change of this CommonSustainabilityProcessWithSustainability.
        """
        self._climate_change = climate_change

    @property
    def external_identity(self) -> "str":
        """Gets the external_identity of this CommonSustainabilityProcessWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        str
            The external_identity of this CommonSustainabilityProcessWithSustainability.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "str") -> None:
        """Sets the external_identity of this CommonSustainabilityProcessWithSustainability.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: str
            The external_identity of this CommonSustainabilityProcessWithSustainability.
        """
        self._external_identity = external_identity

    @property
    def name(self) -> "str":
        """Gets the name of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        str
            The name of this CommonSustainabilityProcessWithSustainability.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: str
            The name of this CommonSustainabilityProcessWithSustainability.
        """
        self._name = name

    @property
    def reference_type(self) -> "str":
        """Gets the reference_type of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        str
            The reference_type of this CommonSustainabilityProcessWithSustainability.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "str") -> None:
        """Sets the reference_type of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        reference_type: str
            The reference_type of this CommonSustainabilityProcessWithSustainability.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "str":
        """Gets the reference_value of this CommonSustainabilityProcessWithSustainability.

        Returns
        -------
        str
            The reference_value of this CommonSustainabilityProcessWithSustainability.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "str") -> None:
        """Sets the reference_value of this CommonSustainabilityProcessWithSustainability.

        Parameters
        ----------
        reference_value: str
            The reference_value of this CommonSustainabilityProcessWithSustainability.
        """
        self._reference_value = reference_value

    @property
    def id(self) -> "str":
        """Gets the id of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        str
            The id of this CommonSustainabilityProcessWithSustainability.
        """
        return self._id

    @id.setter
    def id(self, id: "str") -> None:
        """Sets the id of this CommonSustainabilityProcessWithSustainability.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: str
            The id of this CommonSustainabilityProcessWithSustainability.
        """
        self._id = id

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
        if issubclass(CommonSustainabilityProcessWithSustainability, dict):
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
        if not isinstance(other, CommonSustainabilityProcessWithSustainability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
