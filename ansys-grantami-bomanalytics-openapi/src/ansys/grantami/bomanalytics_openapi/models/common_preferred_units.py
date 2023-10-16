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


class CommonPreferredUnits(ModelBase):
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
        "distance_unit": "str",
        "energy_unit": "str",
        "mass_unit": "str",
    }

    attribute_map = {
        "distance_unit": "DistanceUnit",
        "energy_unit": "EnergyUnit",
        "mass_unit": "MassUnit",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        distance_unit: "Optional[str]" = None,
        energy_unit: "Optional[str]" = None,
        mass_unit: "Optional[str]" = None,
    ) -> None:
        """CommonPreferredUnits - a model defined in Swagger

        Parameters
        ----------
            distance_unit: str, optional
            energy_unit: str, optional
            mass_unit: str, optional
        """
        self._mass_unit = None
        self._energy_unit = None
        self._distance_unit = None
        self.discriminator = None
        if mass_unit is not None:
            self.mass_unit = mass_unit
        if energy_unit is not None:
            self.energy_unit = energy_unit
        if distance_unit is not None:
            self.distance_unit = distance_unit

    @property
    def mass_unit(self) -> "str":
        """Gets the mass_unit of this CommonPreferredUnits.

        Returns
        -------
        str
            The mass_unit of this CommonPreferredUnits.
        """
        return self._mass_unit

    @mass_unit.setter
    def mass_unit(self, mass_unit: "str") -> None:
        """Sets the mass_unit of this CommonPreferredUnits.

        Parameters
        ----------
        mass_unit: str
            The mass_unit of this CommonPreferredUnits.
        """
        self._mass_unit = mass_unit

    @property
    def energy_unit(self) -> "str":
        """Gets the energy_unit of this CommonPreferredUnits.

        Returns
        -------
        str
            The energy_unit of this CommonPreferredUnits.
        """
        return self._energy_unit

    @energy_unit.setter
    def energy_unit(self, energy_unit: "str") -> None:
        """Sets the energy_unit of this CommonPreferredUnits.

        Parameters
        ----------
        energy_unit: str
            The energy_unit of this CommonPreferredUnits.
        """
        self._energy_unit = energy_unit

    @property
    def distance_unit(self) -> "str":
        """Gets the distance_unit of this CommonPreferredUnits.

        Returns
        -------
        str
            The distance_unit of this CommonPreferredUnits.
        """
        return self._distance_unit

    @distance_unit.setter
    def distance_unit(self, distance_unit: "str") -> None:
        """Sets the distance_unit of this CommonPreferredUnits.

        Parameters
        ----------
        distance_unit: str
            The distance_unit of this CommonPreferredUnits.
        """
        self._distance_unit = distance_unit

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
        if issubclass(CommonPreferredUnits, dict):
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
        if not isinstance(other, CommonPreferredUnits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
