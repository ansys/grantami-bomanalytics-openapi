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


class CommonRequestConfig(ModelBase):
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
        "coatings_table_name": "str",
        "inhouse_materials_table_name": "str",
        "locations_table_name": "str",
        "material_universe_table_name": "str",
        "maximum_spec_to_spec_link_depth": "int",
        "process_universe_table_name": "str",
        "products_and_parts_table_name": "str",
        "specifications_table_name": "str",
        "substances_table_name": "str",
        "transport_table_name": "str",
    }

    attribute_map = {
        "coatings_table_name": "CoatingsTableName",
        "inhouse_materials_table_name": "InhouseMaterialsTableName",
        "locations_table_name": "LocationsTableName",
        "material_universe_table_name": "MaterialUniverseTableName",
        "maximum_spec_to_spec_link_depth": "MaximumSpecToSpecLinkDepth",
        "process_universe_table_name": "ProcessUniverseTableName",
        "products_and_parts_table_name": "ProductsAndPartsTableName",
        "specifications_table_name": "SpecificationsTableName",
        "substances_table_name": "SubstancesTableName",
        "transport_table_name": "TransportTableName",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        coatings_table_name: "Optional[str]" = None,
        inhouse_materials_table_name: "Optional[str]" = None,
        locations_table_name: "Optional[str]" = None,
        material_universe_table_name: "Optional[str]" = None,
        maximum_spec_to_spec_link_depth: "Optional[int]" = None,
        process_universe_table_name: "Optional[str]" = None,
        products_and_parts_table_name: "Optional[str]" = None,
        specifications_table_name: "Optional[str]" = None,
        substances_table_name: "Optional[str]" = None,
        transport_table_name: "Optional[str]" = None,
    ) -> None:
        """CommonRequestConfig - a model defined in Swagger

        Parameters
        ----------
            coatings_table_name: str, optional
            inhouse_materials_table_name: str, optional
            locations_table_name: str, optional
            material_universe_table_name: str, optional
            maximum_spec_to_spec_link_depth: int, optional
            process_universe_table_name: str, optional
            products_and_parts_table_name: str, optional
            specifications_table_name: str, optional
            substances_table_name: str, optional
            transport_table_name: str, optional
        """
        self._material_universe_table_name = None
        self._inhouse_materials_table_name = None
        self._specifications_table_name = None
        self._products_and_parts_table_name = None
        self._substances_table_name = None
        self._coatings_table_name = None
        self._transport_table_name = None
        self._process_universe_table_name = None
        self._locations_table_name = None
        self._maximum_spec_to_spec_link_depth = None
        self.discriminator = None
        if material_universe_table_name is not None:
            self.material_universe_table_name = material_universe_table_name
        if inhouse_materials_table_name is not None:
            self.inhouse_materials_table_name = inhouse_materials_table_name
        if specifications_table_name is not None:
            self.specifications_table_name = specifications_table_name
        if products_and_parts_table_name is not None:
            self.products_and_parts_table_name = products_and_parts_table_name
        if substances_table_name is not None:
            self.substances_table_name = substances_table_name
        if coatings_table_name is not None:
            self.coatings_table_name = coatings_table_name
        if transport_table_name is not None:
            self.transport_table_name = transport_table_name
        if process_universe_table_name is not None:
            self.process_universe_table_name = process_universe_table_name
        if locations_table_name is not None:
            self.locations_table_name = locations_table_name
        if maximum_spec_to_spec_link_depth is not None:
            self.maximum_spec_to_spec_link_depth = maximum_spec_to_spec_link_depth

    @property
    def material_universe_table_name(self) -> "str":
        """Gets the material_universe_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The material_universe_table_name of this CommonRequestConfig.
        """
        return self._material_universe_table_name

    @material_universe_table_name.setter
    def material_universe_table_name(self, material_universe_table_name: "str") -> None:
        """Sets the material_universe_table_name of this CommonRequestConfig.

        Parameters
        ----------
        material_universe_table_name: str
            The material_universe_table_name of this CommonRequestConfig.
        """
        self._material_universe_table_name = material_universe_table_name

    @property
    def inhouse_materials_table_name(self) -> "str":
        """Gets the inhouse_materials_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The inhouse_materials_table_name of this CommonRequestConfig.
        """
        return self._inhouse_materials_table_name

    @inhouse_materials_table_name.setter
    def inhouse_materials_table_name(self, inhouse_materials_table_name: "str") -> None:
        """Sets the inhouse_materials_table_name of this CommonRequestConfig.

        Parameters
        ----------
        inhouse_materials_table_name: str
            The inhouse_materials_table_name of this CommonRequestConfig.
        """
        self._inhouse_materials_table_name = inhouse_materials_table_name

    @property
    def specifications_table_name(self) -> "str":
        """Gets the specifications_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The specifications_table_name of this CommonRequestConfig.
        """
        return self._specifications_table_name

    @specifications_table_name.setter
    def specifications_table_name(self, specifications_table_name: "str") -> None:
        """Sets the specifications_table_name of this CommonRequestConfig.

        Parameters
        ----------
        specifications_table_name: str
            The specifications_table_name of this CommonRequestConfig.
        """
        self._specifications_table_name = specifications_table_name

    @property
    def products_and_parts_table_name(self) -> "str":
        """Gets the products_and_parts_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The products_and_parts_table_name of this CommonRequestConfig.
        """
        return self._products_and_parts_table_name

    @products_and_parts_table_name.setter
    def products_and_parts_table_name(
        self, products_and_parts_table_name: "str"
    ) -> None:
        """Sets the products_and_parts_table_name of this CommonRequestConfig.

        Parameters
        ----------
        products_and_parts_table_name: str
            The products_and_parts_table_name of this CommonRequestConfig.
        """
        self._products_and_parts_table_name = products_and_parts_table_name

    @property
    def substances_table_name(self) -> "str":
        """Gets the substances_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The substances_table_name of this CommonRequestConfig.
        """
        return self._substances_table_name

    @substances_table_name.setter
    def substances_table_name(self, substances_table_name: "str") -> None:
        """Sets the substances_table_name of this CommonRequestConfig.

        Parameters
        ----------
        substances_table_name: str
            The substances_table_name of this CommonRequestConfig.
        """
        self._substances_table_name = substances_table_name

    @property
    def coatings_table_name(self) -> "str":
        """Gets the coatings_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The coatings_table_name of this CommonRequestConfig.
        """
        return self._coatings_table_name

    @coatings_table_name.setter
    def coatings_table_name(self, coatings_table_name: "str") -> None:
        """Sets the coatings_table_name of this CommonRequestConfig.

        Parameters
        ----------
        coatings_table_name: str
            The coatings_table_name of this CommonRequestConfig.
        """
        self._coatings_table_name = coatings_table_name

    @property
    def transport_table_name(self) -> "str":
        """Gets the transport_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The transport_table_name of this CommonRequestConfig.
        """
        return self._transport_table_name

    @transport_table_name.setter
    def transport_table_name(self, transport_table_name: "str") -> None:
        """Sets the transport_table_name of this CommonRequestConfig.

        Parameters
        ----------
        transport_table_name: str
            The transport_table_name of this CommonRequestConfig.
        """
        self._transport_table_name = transport_table_name

    @property
    def process_universe_table_name(self) -> "str":
        """Gets the process_universe_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The process_universe_table_name of this CommonRequestConfig.
        """
        return self._process_universe_table_name

    @process_universe_table_name.setter
    def process_universe_table_name(self, process_universe_table_name: "str") -> None:
        """Sets the process_universe_table_name of this CommonRequestConfig.

        Parameters
        ----------
        process_universe_table_name: str
            The process_universe_table_name of this CommonRequestConfig.
        """
        self._process_universe_table_name = process_universe_table_name

    @property
    def locations_table_name(self) -> "str":
        """Gets the locations_table_name of this CommonRequestConfig.

        Returns
        -------
        str
            The locations_table_name of this CommonRequestConfig.
        """
        return self._locations_table_name

    @locations_table_name.setter
    def locations_table_name(self, locations_table_name: "str") -> None:
        """Sets the locations_table_name of this CommonRequestConfig.

        Parameters
        ----------
        locations_table_name: str
            The locations_table_name of this CommonRequestConfig.
        """
        self._locations_table_name = locations_table_name

    @property
    def maximum_spec_to_spec_link_depth(self) -> "int":
        """Gets the maximum_spec_to_spec_link_depth of this CommonRequestConfig.

        Returns
        -------
        int
            The maximum_spec_to_spec_link_depth of this CommonRequestConfig.
        """
        return self._maximum_spec_to_spec_link_depth

    @maximum_spec_to_spec_link_depth.setter
    def maximum_spec_to_spec_link_depth(
        self, maximum_spec_to_spec_link_depth: "int"
    ) -> None:
        """Sets the maximum_spec_to_spec_link_depth of this CommonRequestConfig.

        Parameters
        ----------
        maximum_spec_to_spec_link_depth: int
            The maximum_spec_to_spec_link_depth of this CommonRequestConfig.
        """
        self._maximum_spec_to_spec_link_depth = maximum_spec_to_spec_link_depth

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
        if issubclass(CommonRequestConfig, dict):
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
        if not isinstance(other, CommonRequestConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
