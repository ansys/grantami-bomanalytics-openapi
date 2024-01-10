"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "impacted_substances": "list[CommonImpactedSubstance]",
        "legislation_id": "str",
    }

    attribute_map = {
        "impacted_substances": "ImpactedSubstances",
        "legislation_id": "LegislationId",
    }

    subtype_mapping = {
        "ImpactedSubstances": "CommonImpactedSubstance",
    }

    discriminator = None

    def __init__(
        self,
        *,
        impacted_substances: "Optional[List[CommonImpactedSubstance]]" = None,
        legislation_id: "Optional[str]" = None,
    ) -> None:
        """CommonLegislationWithImpactedSubstances - a model defined in Swagger

        Parameters
        ----------
            impacted_substances: List[CommonImpactedSubstance], optional
            legislation_id: str, optional
        """
        self._legislation_id = None
        self._impacted_substances = None

        if legislation_id is not None:
            self.legislation_id = legislation_id
        if impacted_substances is not None:
            self.impacted_substances = impacted_substances

    @property
    def legislation_id(self) -> "str":
        """Gets the legislation_id of this CommonLegislationWithImpactedSubstances.

        Returns
        -------
        str
            The legislation_id of this CommonLegislationWithImpactedSubstances.
        """
        return self._legislation_id

    @legislation_id.setter
    def legislation_id(self, legislation_id: "str") -> None:
        """Sets the legislation_id of this CommonLegislationWithImpactedSubstances.

        Parameters
        ----------
        legislation_id: str
            The legislation_id of this CommonLegislationWithImpactedSubstances.
        """
        self._legislation_id = legislation_id

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
