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


class CommonLegislationWithImpactedSubstances(ModelBase):
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
        "legislation_name": "str",
        "impacted_substances": "list[CommonImpactedSubstance]",
    }

    attribute_map = {
        "legislation_name": "LegislationName",
        "impacted_substances": "ImpactedSubstances",
    }

    subtype_mapping = {
        "ImpactedSubstances": "CommonImpactedSubstance",
    }

    def __init__(
        self,
        *,
        impacted_substances: "Optional[List[CommonImpactedSubstance]]" = None,
        legislation_name: "Optional[str]" = None,
    ) -> None:
        """CommonLegislationWithImpactedSubstances - a model defined in Swagger

        Parameters
        ----------
            impacted_substances: List[CommonImpactedSubstance], optional
            legislation_name: str, optional
        """
        self._legislation_name = None
        self._impacted_substances = None
        self.discriminator = None
        if legislation_name is not None:
            self.legislation_name = legislation_name
        if impacted_substances is not None:
            self.impacted_substances = impacted_substances

    @property
    def legislation_name(self) -> "str":
        """Gets the legislation_name of this CommonLegislationWithImpactedSubstances.

        Returns
        -------
        str
            The legislation_name of this CommonLegislationWithImpactedSubstances.
        """
        return self._legislation_name

    @legislation_name.setter
    def legislation_name(self, legislation_name: "str") -> None:
        """Sets the legislation_name of this CommonLegislationWithImpactedSubstances.

        Parameters
        ----------
        legislation_name: str
            The legislation_name of this CommonLegislationWithImpactedSubstances.
        """
        self._legislation_name = legislation_name

    @property
    def impacted_substances(self) -> "list[CommonImpactedSubstance]":
        """Gets the impacted_substances of this CommonLegislationWithImpactedSubstances.

        Returns
        -------
        list[CommonImpactedSubstance]
            The impacted_substances of this CommonLegislationWithImpactedSubstances.
        """
        return self._impacted_substances

    @impacted_substances.setter
    def impacted_substances(
        self, impacted_substances: "list[CommonImpactedSubstance]"
    ) -> None:
        """Sets the impacted_substances of this CommonLegislationWithImpactedSubstances.

        Parameters
        ----------
        impacted_substances: list[CommonImpactedSubstance]
            The impacted_substances of this CommonLegislationWithImpactedSubstances.
        """
        self._impacted_substances = impacted_substances

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
        if issubclass(CommonLegislationWithImpactedSubstances, dict):
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
        if not isinstance(other, CommonLegislationWithImpactedSubstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
