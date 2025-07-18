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
Granta.BomAnalyticsServices.V2

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


class CommonRequestConfig(ModelBase):
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
        "coatings_table_name": "str",
        "inhouse_materials_table_name": "str",
        "locations_table_name": "str",
        "material_universe_table_name": "str",
        "maximum_spec_chain_node_count": "int",
        "process_universe_table_name": "str",
        "products_and_parts_table_name": "str",
        "specifications_table_name": "str",
        "substances_table_name": "str",
        "transport_table_name": "str",
    }

    attribute_map: dict[str, str] = {
        "coatings_table_name": "CoatingsTableName",
        "inhouse_materials_table_name": "InhouseMaterialsTableName",
        "locations_table_name": "LocationsTableName",
        "material_universe_table_name": "MaterialUniverseTableName",
        "maximum_spec_chain_node_count": "MaximumSpecChainNodeCount",
        "process_universe_table_name": "ProcessUniverseTableName",
        "products_and_parts_table_name": "ProductsAndPartsTableName",
        "specifications_table_name": "SpecificationsTableName",
        "substances_table_name": "SubstancesTableName",
        "transport_table_name": "TransportTableName",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        coatings_table_name: "str | None | Unset_Type" = Unset,
        inhouse_materials_table_name: "str | None | Unset_Type" = Unset,
        locations_table_name: "str | None | Unset_Type" = Unset,
        material_universe_table_name: "str | None | Unset_Type" = Unset,
        maximum_spec_chain_node_count: "int | None | Unset_Type" = Unset,
        process_universe_table_name: "str | None | Unset_Type" = Unset,
        products_and_parts_table_name: "str | None | Unset_Type" = Unset,
        specifications_table_name: "str | None | Unset_Type" = Unset,
        substances_table_name: "str | None | Unset_Type" = Unset,
        transport_table_name: "str | None | Unset_Type" = Unset,
    ) -> None:
        """CommonRequestConfig - a model defined in Swagger

        Parameters
        ----------
        coatings_table_name: str | None, optional
        inhouse_materials_table_name: str | None, optional
        locations_table_name: str | None, optional
        material_universe_table_name: str | None, optional
        maximum_spec_chain_node_count: int | None, optional
        process_universe_table_name: str | None, optional
        products_and_parts_table_name: str | None, optional
        specifications_table_name: str | None, optional
        substances_table_name: str | None, optional
        transport_table_name: str | None, optional
        """
        self._material_universe_table_name: str | None | Unset_Type = Unset
        self._inhouse_materials_table_name: str | None | Unset_Type = Unset
        self._specifications_table_name: str | None | Unset_Type = Unset
        self._products_and_parts_table_name: str | None | Unset_Type = Unset
        self._substances_table_name: str | None | Unset_Type = Unset
        self._coatings_table_name: str | None | Unset_Type = Unset
        self._transport_table_name: str | None | Unset_Type = Unset
        self._process_universe_table_name: str | None | Unset_Type = Unset
        self._locations_table_name: str | None | Unset_Type = Unset
        self._maximum_spec_chain_node_count: int | None | Unset_Type = Unset

        if material_universe_table_name is not Unset:
            self.material_universe_table_name = material_universe_table_name
        if inhouse_materials_table_name is not Unset:
            self.inhouse_materials_table_name = inhouse_materials_table_name
        if specifications_table_name is not Unset:
            self.specifications_table_name = specifications_table_name
        if products_and_parts_table_name is not Unset:
            self.products_and_parts_table_name = products_and_parts_table_name
        if substances_table_name is not Unset:
            self.substances_table_name = substances_table_name
        if coatings_table_name is not Unset:
            self.coatings_table_name = coatings_table_name
        if transport_table_name is not Unset:
            self.transport_table_name = transport_table_name
        if process_universe_table_name is not Unset:
            self.process_universe_table_name = process_universe_table_name
        if locations_table_name is not Unset:
            self.locations_table_name = locations_table_name
        if maximum_spec_chain_node_count is not Unset:
            self.maximum_spec_chain_node_count = maximum_spec_chain_node_count

    @property
    def material_universe_table_name(self) -> "str | None | Unset_Type":
        """Gets the material_universe_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The material_universe_table_name of this CommonRequestConfig.
        """
        return self._material_universe_table_name

    @material_universe_table_name.setter
    def material_universe_table_name(
        self, material_universe_table_name: "str | None | Unset_Type"
    ) -> None:
        """Sets the material_universe_table_name of this CommonRequestConfig.

        Parameters
        ----------
        material_universe_table_name: str | None | Unset_Type
            The material_universe_table_name of this CommonRequestConfig.
        """
        self._material_universe_table_name = material_universe_table_name

    @property
    def inhouse_materials_table_name(self) -> "str | None | Unset_Type":
        """Gets the inhouse_materials_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The inhouse_materials_table_name of this CommonRequestConfig.
        """
        return self._inhouse_materials_table_name

    @inhouse_materials_table_name.setter
    def inhouse_materials_table_name(
        self, inhouse_materials_table_name: "str | None | Unset_Type"
    ) -> None:
        """Sets the inhouse_materials_table_name of this CommonRequestConfig.

        Parameters
        ----------
        inhouse_materials_table_name: str | None | Unset_Type
            The inhouse_materials_table_name of this CommonRequestConfig.
        """
        self._inhouse_materials_table_name = inhouse_materials_table_name

    @property
    def specifications_table_name(self) -> "str | None | Unset_Type":
        """Gets the specifications_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The specifications_table_name of this CommonRequestConfig.
        """
        return self._specifications_table_name

    @specifications_table_name.setter
    def specifications_table_name(
        self, specifications_table_name: "str | None | Unset_Type"
    ) -> None:
        """Sets the specifications_table_name of this CommonRequestConfig.

        Parameters
        ----------
        specifications_table_name: str | None | Unset_Type
            The specifications_table_name of this CommonRequestConfig.
        """
        self._specifications_table_name = specifications_table_name

    @property
    def products_and_parts_table_name(self) -> "str | None | Unset_Type":
        """Gets the products_and_parts_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The products_and_parts_table_name of this CommonRequestConfig.
        """
        return self._products_and_parts_table_name

    @products_and_parts_table_name.setter
    def products_and_parts_table_name(
        self, products_and_parts_table_name: "str | None | Unset_Type"
    ) -> None:
        """Sets the products_and_parts_table_name of this CommonRequestConfig.

        Parameters
        ----------
        products_and_parts_table_name: str | None | Unset_Type
            The products_and_parts_table_name of this CommonRequestConfig.
        """
        self._products_and_parts_table_name = products_and_parts_table_name

    @property
    def substances_table_name(self) -> "str | None | Unset_Type":
        """Gets the substances_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The substances_table_name of this CommonRequestConfig.
        """
        return self._substances_table_name

    @substances_table_name.setter
    def substances_table_name(self, substances_table_name: "str | None | Unset_Type") -> None:
        """Sets the substances_table_name of this CommonRequestConfig.

        Parameters
        ----------
        substances_table_name: str | None | Unset_Type
            The substances_table_name of this CommonRequestConfig.
        """
        self._substances_table_name = substances_table_name

    @property
    def coatings_table_name(self) -> "str | None | Unset_Type":
        """Gets the coatings_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The coatings_table_name of this CommonRequestConfig.
        """
        return self._coatings_table_name

    @coatings_table_name.setter
    def coatings_table_name(self, coatings_table_name: "str | None | Unset_Type") -> None:
        """Sets the coatings_table_name of this CommonRequestConfig.

        Parameters
        ----------
        coatings_table_name: str | None | Unset_Type
            The coatings_table_name of this CommonRequestConfig.
        """
        self._coatings_table_name = coatings_table_name

    @property
    def transport_table_name(self) -> "str | None | Unset_Type":
        """Gets the transport_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The transport_table_name of this CommonRequestConfig.
        """
        return self._transport_table_name

    @transport_table_name.setter
    def transport_table_name(self, transport_table_name: "str | None | Unset_Type") -> None:
        """Sets the transport_table_name of this CommonRequestConfig.

        Parameters
        ----------
        transport_table_name: str | None | Unset_Type
            The transport_table_name of this CommonRequestConfig.
        """
        self._transport_table_name = transport_table_name

    @property
    def process_universe_table_name(self) -> "str | None | Unset_Type":
        """Gets the process_universe_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The process_universe_table_name of this CommonRequestConfig.
        """
        return self._process_universe_table_name

    @process_universe_table_name.setter
    def process_universe_table_name(
        self, process_universe_table_name: "str | None | Unset_Type"
    ) -> None:
        """Sets the process_universe_table_name of this CommonRequestConfig.

        Parameters
        ----------
        process_universe_table_name: str | None | Unset_Type
            The process_universe_table_name of this CommonRequestConfig.
        """
        self._process_universe_table_name = process_universe_table_name

    @property
    def locations_table_name(self) -> "str | None | Unset_Type":
        """Gets the locations_table_name of this CommonRequestConfig.

        Returns
        -------
        str | None | Unset_Type
            The locations_table_name of this CommonRequestConfig.
        """
        return self._locations_table_name

    @locations_table_name.setter
    def locations_table_name(self, locations_table_name: "str | None | Unset_Type") -> None:
        """Sets the locations_table_name of this CommonRequestConfig.

        Parameters
        ----------
        locations_table_name: str | None | Unset_Type
            The locations_table_name of this CommonRequestConfig.
        """
        self._locations_table_name = locations_table_name

    @property
    def maximum_spec_chain_node_count(self) -> "int | None | Unset_Type":
        """Gets the maximum_spec_chain_node_count of this CommonRequestConfig.
        This value is the maximum number of nodes specification link chains should be expanded to contain. The default value of 0 represents the unlimited case.

        Returns
        -------
        int | None | Unset_Type
            The maximum_spec_chain_node_count of this CommonRequestConfig.
        """
        return self._maximum_spec_chain_node_count

    @maximum_spec_chain_node_count.setter
    def maximum_spec_chain_node_count(
        self, maximum_spec_chain_node_count: "int | None | Unset_Type"
    ) -> None:
        """Sets the maximum_spec_chain_node_count of this CommonRequestConfig.
        This value is the maximum number of nodes specification link chains should be expanded to contain. The default value of 0 represents the unlimited case.

        Parameters
        ----------
        maximum_spec_chain_node_count: int | None | Unset_Type
            The maximum_spec_chain_node_count of this CommonRequestConfig.
        """
        self._maximum_spec_chain_node_count = maximum_spec_chain_node_count

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
        if not isinstance(other, CommonRequestConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
