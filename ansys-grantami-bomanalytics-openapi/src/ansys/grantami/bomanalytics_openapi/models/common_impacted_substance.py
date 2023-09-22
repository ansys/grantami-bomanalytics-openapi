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


class CommonImpactedSubstance(ModelBase):
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
        "substance_name": "str",
        "cas_number": "str",
        "ec_number": "str",
        "max_percentage_amount_in_material": "float",
        "legislation_threshold": "float",
    }

    attribute_map = {
        "substance_name": "SubstanceName",
        "cas_number": "CasNumber",
        "ec_number": "EcNumber",
        "max_percentage_amount_in_material": "MaxPercentageAmountInMaterial",
        "legislation_threshold": "LegislationThreshold",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        cas_number: "Optional[str]" = None,
        ec_number: "Optional[str]" = None,
        legislation_threshold: "Optional[float]" = None,
        max_percentage_amount_in_material: "Optional[float]" = None,
        substance_name: "Optional[str]" = None
    ) -> None:
        """CommonImpactedSubstance - a model defined in Swagger

        Parameters
        ----------
            cas_number: str, optional
            ec_number: str, optional
            legislation_threshold: float, optional
            max_percentage_amount_in_material: float, optional
            substance_name: str, optional
        """
        self._substance_name = None
        self._cas_number = None
        self._ec_number = None
        self._max_percentage_amount_in_material = None
        self._legislation_threshold = None
        self.discriminator = None
        if substance_name is not None:
            self.substance_name = substance_name
        if cas_number is not None:
            self.cas_number = cas_number
        if ec_number is not None:
            self.ec_number = ec_number
        if max_percentage_amount_in_material is not None:
            self.max_percentage_amount_in_material = max_percentage_amount_in_material
        if legislation_threshold is not None:
            self.legislation_threshold = legislation_threshold

    @property
    def substance_name(self) -> "str":
        """Gets the substance_name of this CommonImpactedSubstance.

        Returns
        -------
        str
            The substance_name of this CommonImpactedSubstance.
        """
        return self._substance_name

    @substance_name.setter
    def substance_name(self, substance_name: "str") -> None:
        """Sets the substance_name of this CommonImpactedSubstance.

        Parameters
        ----------
        substance_name: str
            The substance_name of this CommonImpactedSubstance.
        """
        self._substance_name = substance_name

    @property
    def cas_number(self) -> "str":
        """Gets the cas_number of this CommonImpactedSubstance.

        Returns
        -------
        str
            The cas_number of this CommonImpactedSubstance.
        """
        return self._cas_number

    @cas_number.setter
    def cas_number(self, cas_number: "str") -> None:
        """Sets the cas_number of this CommonImpactedSubstance.

        Parameters
        ----------
        cas_number: str
            The cas_number of this CommonImpactedSubstance.
        """
        self._cas_number = cas_number

    @property
    def ec_number(self) -> "str":
        """Gets the ec_number of this CommonImpactedSubstance.

        Returns
        -------
        str
            The ec_number of this CommonImpactedSubstance.
        """
        return self._ec_number

    @ec_number.setter
    def ec_number(self, ec_number: "str") -> None:
        """Sets the ec_number of this CommonImpactedSubstance.

        Parameters
        ----------
        ec_number: str
            The ec_number of this CommonImpactedSubstance.
        """
        self._ec_number = ec_number

    @property
    def max_percentage_amount_in_material(self) -> "float":
        """Gets the max_percentage_amount_in_material of this CommonImpactedSubstance.

        Returns
        -------
        float
            The max_percentage_amount_in_material of this CommonImpactedSubstance.
        """
        return self._max_percentage_amount_in_material

    @max_percentage_amount_in_material.setter
    def max_percentage_amount_in_material(
        self, max_percentage_amount_in_material: "float"
    ) -> None:
        """Sets the max_percentage_amount_in_material of this CommonImpactedSubstance.

        Parameters
        ----------
        max_percentage_amount_in_material: float
            The max_percentage_amount_in_material of this CommonImpactedSubstance.
        """
        self._max_percentage_amount_in_material = max_percentage_amount_in_material

    @property
    def legislation_threshold(self) -> "float":
        """Gets the legislation_threshold of this CommonImpactedSubstance.

        Returns
        -------
        float
            The legislation_threshold of this CommonImpactedSubstance.
        """
        return self._legislation_threshold

    @legislation_threshold.setter
    def legislation_threshold(self, legislation_threshold: "float") -> None:
        """Sets the legislation_threshold of this CommonImpactedSubstance.

        Parameters
        ----------
        legislation_threshold: float
            The legislation_threshold of this CommonImpactedSubstance.
        """
        self._legislation_threshold = legislation_threshold

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
        if issubclass(CommonImpactedSubstance, dict):
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
        if not isinstance(other, CommonImpactedSubstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
