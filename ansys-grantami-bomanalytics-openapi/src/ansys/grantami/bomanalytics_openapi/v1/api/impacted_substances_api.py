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
Granta.BomAnalyticsServices.V1

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: V1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ApiBase

if TYPE_CHECKING:
    import pathlib

    from ..models import *


class ImpactedSubstancesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def post_impactedsubstances_bom1711(
        self, *, body: "GetImpactedSubstancesForBom1711Request"
    ) -> "GetImpactedSubstancesForBom1711Response":
        """Get the impacted substances for a Bill of Materials

        Examines the substances contained within a 17/11 Bill of Materials (BoM) by following links to substances, materials, specifications, and parts, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null.  If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.  References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 17/11 BoM schema for more details on how to construct a valid BoM. Legislations are specified by the Legislation Id attribute.  MI managed parts in the BoM will not be expanded to fetch linked parts, materials, substances or specifications from the database. To include these as part of the analysis, they must be explicitly defined within the input BoM.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetImpactedSubstancesForBom1711Request

        Returns
        -------
        GetImpactedSubstancesForBom1711Response
        """
        data = self._post_impactedsubstances_bom1711_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_impactedsubstances_bom1711_with_http_info(
        self, body: "GetImpactedSubstancesForBom1711Request", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_impactedsubstances_bom1711"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_impactedsubstances_bom1711'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GetImpactedSubstancesForBom1711Response",
        }

        return self.api_client.call_api(
            "/impacted-substances/bom1711",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def post_impactedsubstances_bom2301(
        self, *, body: "GetImpactedSubstancesForBom2301Request"
    ) -> "GetImpactedSubstancesForBom2301Response":
        """Get the impacted substances for a Bill of Materials

        Examines the substances contained within a 23/01 Bill of Materials (BoM) by following links to substances, materials, specifications, and parts, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null.  If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.  References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 23/01 BoM schema for more details on how to construct a valid BoM. Legislations are specified by the Legislation Id attribute.  MI managed parts in the BoM will not be expanded to fetch linked parts, materials, substances or specifications from the database. To include these as part of the analysis, they must be explicitly defined within the input BoM.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetImpactedSubstancesForBom2301Request

        Returns
        -------
        GetImpactedSubstancesForBom2301Response
        """
        data = self._post_impactedsubstances_bom2301_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_impactedsubstances_bom2301_with_http_info(
        self, body: "GetImpactedSubstancesForBom2301Request", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_impactedsubstances_bom2301"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_impactedsubstances_bom2301'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GetImpactedSubstancesForBom2301Response",
        }

        return self.api_client.call_api(
            "/impacted-substances/bom2301",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def post_impactedsubstances_materials(
        self, *, body: "GetImpactedSubstancesForMaterialsRequest"
    ) -> "GetImpactedSubstancesForMaterialsResponse":
        """Get the impacted substances for materials

        Examines the substances contained within one or more materials and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the material and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null. A material can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or material ID. The table that contains the material of interest is not required, materials will be discovered if they are present in either in the \"Materials in-house\" or \"MaterialUniverse\" tables. Legislations are specified by the Legislation Id attribute.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetImpactedSubstancesForMaterialsRequest

        Returns
        -------
        GetImpactedSubstancesForMaterialsResponse
        """
        data = self._post_impactedsubstances_materials_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_impactedsubstances_materials_with_http_info(
        self, body: "GetImpactedSubstancesForMaterialsRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_impactedsubstances_materials"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_impactedsubstances_materials'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GetImpactedSubstancesForMaterialsResponse",
        }

        return self.api_client.call_api(
            "/impacted-substances/materials",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def post_impactedsubstances_parts(
        self, *, body: "GetImpactedSubstancesForPartsRequest"
    ) -> "GetImpactedSubstancesForPartsResponse":
        """Get the impacted substances for parts

        Examines the substances contained within one or more parts by following links to substances, materials, specifications and other parts, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null.  If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.  A part can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or part number. Legislations are specified by the Legislation Id attribute.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetImpactedSubstancesForPartsRequest

        Returns
        -------
        GetImpactedSubstancesForPartsResponse
        """
        data = self._post_impactedsubstances_parts_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _post_impactedsubstances_parts_with_http_info(
        self, body: "GetImpactedSubstancesForPartsRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_impactedsubstances_parts"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_impactedsubstances_parts'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GetImpactedSubstancesForPartsResponse",
        }

        return self.api_client.call_api(
            "/impacted-substances/parts",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def post_impactedsubstances_specifications(
        self, *, body: "GetImpactedSubstancesForSpecificationsRequest"
    ) -> "GetImpactedSubstancesForSpecificationsResponse":
        """Get the impacted substances for specifications

        Examines the substances contained within one or more specifications by following links to substances, materials, coatings and other specifications, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported. A specification can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or specification ID. Legislations are specified by the Legislation Id attribute.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetImpactedSubstancesForSpecificationsRequest

        Returns
        -------
        GetImpactedSubstancesForSpecificationsResponse
        """
        data = self._post_impactedsubstances_specifications_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_impactedsubstances_specifications_with_http_info(
        self, body: "GetImpactedSubstancesForSpecificationsRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_impactedsubstances_specifications"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_impactedsubstances_specifications'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GetImpactedSubstancesForSpecificationsResponse",
        }

        return self.api_client.call_api(
            "/impacted-substances/specifications",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )
