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


class ComplianceApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def post_compliance_bom1711(
        self, *, body: "GetComplianceForBom1711Request"
    ) -> "GetComplianceForBom1711Response":
        """Determine the compliance of a BoM in the context of specified indicators

        Compliance is determined first by identifying the substances contained within the parts defined in the BoM, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, specifications, and sub-parts, to determine the compliance of the parts included in the BoM. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex part hierarchies. References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 17/11 BoM schema for more details on how to construct a valid BoM.  Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator. The RoHS Indicator includes an additional parameter 'ignoreExemptions'. Setting this to true will result in the compliance analysis ignoring RoHS exemptions, forcing all parts that contain substances over the threshold to be reported as Non-Compliant. This setting defaults to false if not set, meaning exemptions will be applied and such a part would be reported as 'Compliant with Exemptions'. The parameter has no effect if used either on a non-part Compliance query (since only parts can have RoHS exemptions), or with a Watch List Indicator.  MI managed parts in the BoM will not be expanded to fetch linked parts, materials, substances or specifications from the database. To include these as part of the analysis, they must be explicitly defined within the input BoM.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetComplianceForBom1711Request

        Returns
        -------
        GetComplianceForBom1711Response
        """
        data = self._post_compliance_bom1711_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _post_compliance_bom1711_with_http_info(
        self, body: "GetComplianceForBom1711Request", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_compliance_bom1711"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_compliance_bom1711'"
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
            200: "GetComplianceForBom1711Response",
        }

        return self.api_client.call_api(
            "/compliance/bom1711",
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

    def post_compliance_bom2301(
        self, *, body: "GetComplianceForBom2301Request"
    ) -> "GetComplianceForBom2301Response":
        """Determine the compliance of a BoM in the context of specified indicators

        Compliance is determined first by identifying the substances contained within the parts defined in the BoM, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, specifications, and sub-parts, to determine the compliance of the parts included in the BoM. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex part hierarchies. References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 23/01 BoM schema for more details on how to construct a valid BoM.  Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator. The RoHS Indicator includes an additional parameter 'ignoreExemptions'. Setting this to true will result in the compliance analysis ignoring RoHS exemptions, forcing all parts that contain substances over the threshold to be reported as Non-Compliant. This setting defaults to false if not set, meaning exemptions will be applied and such a part would be reported as 'Compliant with Exemptions'. The parameter has no effect if used either on a non-part Compliance query (since only parts can have RoHS exemptions), or with a Watch List Indicator.  MI managed parts in the BoM will not be expanded to fetch linked parts, materials, substances or specifications from the database. To include these as part of the analysis, they must be explicitly defined within the input BoM.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetComplianceForBom2301Request

        Returns
        -------
        GetComplianceForBom2301Response
        """
        data = self._post_compliance_bom2301_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _post_compliance_bom2301_with_http_info(
        self, body: "GetComplianceForBom2301Request", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_compliance_bom2301"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_compliance_bom2301'"
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
            200: "GetComplianceForBom2301Response",
        }

        return self.api_client.call_api(
            "/compliance/bom2301",
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

    def post_compliance_materials(
        self, *, body: "GetComplianceForMaterialsRequest"
    ) -> "GetComplianceForMaterialsResponse":
        """Determine the compliance of one or more materials in the context of specified indicators

        Compliance is determined first by identifying the substances contained within the materials, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances to the parent materials to determine material compliance. This endpoint reports the compliance result for both the materials and substances. A material can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or material ID. The table that contains the material of interest is not required, materials will be discovered if they are present in either in the \"Materials in-house\" or \"MaterialUniverse\" tables. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetComplianceForMaterialsRequest

        Returns
        -------
        GetComplianceForMaterialsResponse
        """
        data = self._post_compliance_materials_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _post_compliance_materials_with_http_info(
        self, body: "GetComplianceForMaterialsRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_compliance_materials"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_compliance_materials'"
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
            200: "GetComplianceForMaterialsResponse",
        }

        return self.api_client.call_api(
            "/compliance/materials",
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

    def post_compliance_parts(
        self, *, body: "GetComplianceForPartsRequest"
    ) -> "GetComplianceForPartsResponse":
        """Determine the compliance of one or more parts in the context of specified indicators

        Compliance is determined first by identifying the substances contained within the parts, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, specifications, and sub-parts, to determine the compliance of the parts included in the request. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex part hierarchies. A part can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or part number. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator. The RoHS Indicator includes an additional parameter 'ignoreExemptions'. Setting this to true will result in the compliance analysis ignoring RoHS exemptions, forcing all parts that contain substances over the threshold to be reported as Non-Compliant. This setting defaults to false if not set, meaning exemptions will be applied and such a part would be reported as 'Compliant with Exemptions'. The parameter has no effect if used either on a non-part Compliance query (since only parts can have RoHS exemptions), or with a Watch List Indicator.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetComplianceForPartsRequest

        Returns
        -------
        GetComplianceForPartsResponse
        """
        data = self._post_compliance_parts_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _post_compliance_parts_with_http_info(
        self, body: "GetComplianceForPartsRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_compliance_parts"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_compliance_parts'"
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
            200: "GetComplianceForPartsResponse",
        }

        return self.api_client.call_api(
            "/compliance/parts",
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

    def post_compliance_specifications(
        self, *, body: "GetComplianceForSpecificationsRequest"
    ) -> "GetComplianceForSpecificationsResponse":
        """Determine the compliance of one or more specifications in the context of specified indicators

        Compliance is determined first by identifying the substances contained within the specifications, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, and specifications, to determine the compliance of the specifications included in the request. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex specification hierarchies. A specification can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or specification ID. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetComplianceForSpecificationsRequest

        Returns
        -------
        GetComplianceForSpecificationsResponse
        """
        data = self._post_compliance_specifications_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_compliance_specifications_with_http_info(
        self, body: "GetComplianceForSpecificationsRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_compliance_specifications"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_compliance_specifications'"
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
            200: "GetComplianceForSpecificationsResponse",
        }

        return self.api_client.call_api(
            "/compliance/specifications",
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

    def post_compliance_substances(
        self, *, body: "GetComplianceForSubstancesRequest"
    ) -> "GetComplianceForSubstancesResponse":
        """Determine the compliance of one or more substances in the context of specified indicators

        Compliance is determined by comparing the substance quantity against the threshold defined for that indicator. The response includes the compliance status for each substance for each indicator. A substance can be referenced by one of six different identifiers: record GUID, record history GUID, record history identity, CAS Number, EC Number, or Chemical Name. The amount of substance is also required, since generally a substance is only non-compliant over a certain threshold. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetComplianceForSubstancesRequest

        Returns
        -------
        GetComplianceForSubstancesResponse
        """
        data = self._post_compliance_substances_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _post_compliance_substances_with_http_info(
        self, body: "GetComplianceForSubstancesRequest", **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_compliance_substances"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_compliance_substances'"
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
            200: "GetComplianceForSubstancesResponse",
        }

        return self.api_client.call_api(
            "/compliance/substances",
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
