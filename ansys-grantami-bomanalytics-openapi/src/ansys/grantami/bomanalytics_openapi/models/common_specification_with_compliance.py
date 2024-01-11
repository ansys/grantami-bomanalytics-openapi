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


class CommonSpecificationWithCompliance(ModelBase):
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
        "coatings": "list[CommonCoatingWithCompliance]",
        "external_identity": "str",
        "id": "str",
        "indicators": "list[CommonIndicatorResult]",
        "materials": "list[CommonMaterialWithCompliance]",
        "name": "str",
        "reference_type": "str",
        "reference_value": "str",
        "specifications": "list[CommonSpecificationWithCompliance]",
        "substances": "list[CommonSubstanceWithCompliance]",
    }

    attribute_map = {
        "coatings": "Coatings",
        "external_identity": "ExternalIdentity",
        "id": "Id",
        "indicators": "Indicators",
        "materials": "Materials",
        "name": "Name",
        "reference_type": "ReferenceType",
        "reference_value": "ReferenceValue",
        "specifications": "Specifications",
        "substances": "Substances",
    }

    subtype_mapping = {
        "Indicators": "CommonIndicatorResult",
        "Specifications": "CommonSpecificationWithCompliance",
        "Coatings": "CommonCoatingWithCompliance",
        "Materials": "CommonMaterialWithCompliance",
        "Substances": "CommonSubstanceWithCompliance",
    }

    discriminator = None

    def __init__(
        self,
        *,
        coatings: "Optional[List[CommonCoatingWithCompliance]]" = None,
        external_identity: "Optional[str]" = None,
        id: "Optional[str]" = None,
        indicators: "Optional[List[CommonIndicatorResult]]" = None,
        materials: "Optional[List[CommonMaterialWithCompliance]]" = None,
        name: "Optional[str]" = None,
        reference_type: "Optional[str]" = None,
        reference_value: "Optional[str]" = None,
        specifications: "Optional[List[CommonSpecificationWithCompliance]]" = None,
        substances: "Optional[List[CommonSubstanceWithCompliance]]" = None,
    ) -> None:
        """CommonSpecificationWithCompliance - a model defined in Swagger

        Parameters
        ----------
            coatings: List[CommonCoatingWithCompliance], optional
            external_identity: str, optional
            id: str, optional
            indicators: List[CommonIndicatorResult], optional
            materials: List[CommonMaterialWithCompliance], optional
            name: str, optional
            reference_type: str, optional
            reference_value: str, optional
            specifications: List[CommonSpecificationWithCompliance], optional
            substances: List[CommonSubstanceWithCompliance], optional
        """
        self._indicators = None
        self._specifications = None
        self._coatings = None
        self._materials = None
        self._substances = None
        self._external_identity = None
        self._name = None
        self._reference_type = None
        self._reference_value = None
        self._id = None

        if indicators is not None:
            self.indicators = indicators
        if specifications is not None:
            self.specifications = specifications
        if coatings is not None:
            self.coatings = coatings
        if materials is not None:
            self.materials = materials
        if substances is not None:
            self.substances = substances
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
    def indicators(self) -> "list[CommonIndicatorResult]":
        """Gets the indicators of this CommonSpecificationWithCompliance.

        Returns
        -------
        list[CommonIndicatorResult]
            The indicators of this CommonSpecificationWithCompliance.
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators: "list[CommonIndicatorResult]") -> None:
        """Sets the indicators of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        indicators: list[CommonIndicatorResult]
            The indicators of this CommonSpecificationWithCompliance.
        """
        self._indicators = indicators

    @property
    def specifications(self) -> "list[CommonSpecificationWithCompliance]":
        """Gets the specifications of this CommonSpecificationWithCompliance.

        Returns
        -------
        list[CommonSpecificationWithCompliance]
            The specifications of this CommonSpecificationWithCompliance.
        """
        return self._specifications

    @specifications.setter
    def specifications(
        self, specifications: "list[CommonSpecificationWithCompliance]"
    ) -> None:
        """Sets the specifications of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        specifications: list[CommonSpecificationWithCompliance]
            The specifications of this CommonSpecificationWithCompliance.
        """
        self._specifications = specifications

    @property
    def coatings(self) -> "list[CommonCoatingWithCompliance]":
        """Gets the coatings of this CommonSpecificationWithCompliance.

        Returns
        -------
        list[CommonCoatingWithCompliance]
            The coatings of this CommonSpecificationWithCompliance.
        """
        return self._coatings

    @coatings.setter
    def coatings(self, coatings: "list[CommonCoatingWithCompliance]") -> None:
        """Sets the coatings of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        coatings: list[CommonCoatingWithCompliance]
            The coatings of this CommonSpecificationWithCompliance.
        """
        self._coatings = coatings

    @property
    def materials(self) -> "list[CommonMaterialWithCompliance]":
        """Gets the materials of this CommonSpecificationWithCompliance.

        Returns
        -------
        list[CommonMaterialWithCompliance]
            The materials of this CommonSpecificationWithCompliance.
        """
        return self._materials

    @materials.setter
    def materials(self, materials: "list[CommonMaterialWithCompliance]") -> None:
        """Sets the materials of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        materials: list[CommonMaterialWithCompliance]
            The materials of this CommonSpecificationWithCompliance.
        """
        self._materials = materials

    @property
    def substances(self) -> "list[CommonSubstanceWithCompliance]":
        """Gets the substances of this CommonSpecificationWithCompliance.

        Returns
        -------
        list[CommonSubstanceWithCompliance]
            The substances of this CommonSpecificationWithCompliance.
        """
        return self._substances

    @substances.setter
    def substances(self, substances: "list[CommonSubstanceWithCompliance]") -> None:
        """Sets the substances of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        substances: list[CommonSubstanceWithCompliance]
            The substances of this CommonSpecificationWithCompliance.
        """
        self._substances = substances

    @property
    def external_identity(self) -> "str":
        """Gets the external_identity of this CommonSpecificationWithCompliance.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Returns
        -------
        str
            The external_identity of this CommonSpecificationWithCompliance.
        """
        return self._external_identity

    @external_identity.setter
    def external_identity(self, external_identity: "str") -> None:
        """Sets the external_identity of this CommonSpecificationWithCompliance.
        In the input BoM, the ExternalIdentity is intended to be used as a temporary reference populated and used by applications to refer to the item within the BoM. If a value was specified in the input BoM, it will be returned back to the client in this property. If the ExternalIdentity was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        external_identity: str
            The external_identity of this CommonSpecificationWithCompliance.
        """
        self._external_identity = external_identity

    @property
    def name(self) -> "str":
        """Gets the name of this CommonSpecificationWithCompliance.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Returns
        -------
        str
            The name of this CommonSpecificationWithCompliance.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this CommonSpecificationWithCompliance.
        Many elements in the input BoM schema allow for the display name to be set in a 'Name' element. If this was set in the input BoM, its value is returned in this property. If the Name was not present in the input BoM, this property is omitted.

        Parameters
        ----------
        name: str
            The name of this CommonSpecificationWithCompliance.
        """
        self._name = name

    @property
    def reference_type(self) -> "str":
        """Gets the reference_type of this CommonSpecificationWithCompliance.

        Returns
        -------
        str
            The reference_type of this CommonSpecificationWithCompliance.
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type: "str") -> None:
        """Sets the reference_type of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        reference_type: str
            The reference_type of this CommonSpecificationWithCompliance.
        """
        self._reference_type = reference_type

    @property
    def reference_value(self) -> "str":
        """Gets the reference_value of this CommonSpecificationWithCompliance.

        Returns
        -------
        str
            The reference_value of this CommonSpecificationWithCompliance.
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value: "str") -> None:
        """Sets the reference_value of this CommonSpecificationWithCompliance.

        Parameters
        ----------
        reference_value: str
            The reference_value of this CommonSpecificationWithCompliance.
        """
        self._reference_value = reference_value

    @property
    def id(self) -> "str":
        """Gets the id of this CommonSpecificationWithCompliance.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Returns
        -------
        str
            The id of this CommonSpecificationWithCompliance.
        """
        return self._id

    @id.setter
    def id(self, id: "str") -> None:
        """Sets the id of this CommonSpecificationWithCompliance.
        Many elements in the input BoM schema allow for an XML ID attribute (called 'id') to be set. If this was set in the input BoM, its value is returned in this property. If no value was set in the input BoM an arbitrary, a unique value will be assigned.

        Parameters
        ----------
        id: str
            The id of this CommonSpecificationWithCompliance.
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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, CommonSpecificationWithCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
