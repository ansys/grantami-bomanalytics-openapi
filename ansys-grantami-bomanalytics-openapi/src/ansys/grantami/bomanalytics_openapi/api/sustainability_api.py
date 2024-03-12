"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    BinaryIO,
    List,
    Optional,
    Union,
)  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class SustainabilityApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def post_sustainability_bom2301(
        self, *, body: "GetSustainabilityForBom2301Request"
    ) -> "GetSustainabilityForBom2301Response":
        """Provides sustainability analysis for a BoM, including embodied energy and climate change (CO2-eq) values.

        This endpoint reports sustainability results for each applicable level, and as a result the response can be very large for complex part hierarchies. References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 23/01 BoM schema for more details on how to construct a valid BoM. Embodied Energy and Climate Change (CO2-eq) are rolled-up at a part level. The associated energy and climate change values with a process are the costs of applying that process to the parent material or part. The associated energy and climate change values with a material are the production costs of the material and do not include the costs of any processes applied to it. However the associated values with a part are the sum of any contained materials and parts, the processes applied to those materials as well as any processes applied directly to the part itself.  MI managed parts in the BoM will not be expanded to fetch linked parts or materials from the database. To include these as part of the analysis, they must be explicitly defined within the input BoM.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetSustainabilityForBom2301Request

        Returns
        -------
        GetSustainabilityForBom2301Response
        """
        data = self._post_sustainability_bom2301_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_sustainability_bom2301_with_http_info(
        self, body: "GetSustainabilityForBom2301Request", **kwargs: Any
    ) -> Any:
        all_params = [
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_sustainability_bom2301"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_sustainability_bom2301'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GetSustainabilityForBom2301Response",
        }

        return self.api_client.call_api(
            "/sustainability/bom2301",
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

    def post_sustainabilitysummary_bom2301(
        self, *, body: "GetSustainabilitySummaryForBom2301Request"
    ) -> "GetSustainabilitySummaryForBom2301Response":
        """Summarises the sustainability analysis for a BoM, highlighting the most significant contributors to the environmental impact.

        This endpoint summarises sustainability results for the material, transport and process phases. For BoMs containing many materials and processes, this can result in the response being very large. References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 23/01 BoM schema for more details on how to construct a valid BoM. The PhaseSummary property for each phase reports the percentage impact relative to the entire BoM energy/climate change. Individual materials and transport entries give their percentage impact relative to the phase, whilst individual process entries give their percentage relative to the process type. A primary process entry with a embodied energy contribution of 50% would be 50% of the total embodied energy of primary processes in the BoM, whereas a transport entry with the same contribution would be 50% of all transport energy in the BoM.  MI managed parts in the BoM will not be expanded to fetch linked parts or materials from the database. To include these as part of the analysis, they must be explicitly defined within the input BoM.
        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GetSustainabilitySummaryForBom2301Request

        Returns
        -------
        GetSustainabilitySummaryForBom2301Response
        """
        data = self._post_sustainabilitysummary_bom2301_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _post_sustainabilitysummary_bom2301_with_http_info(
        self, body: "GetSustainabilitySummaryForBom2301Request", **kwargs: Any
    ) -> Any:
        all_params = [
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method post_sustainabilitysummary_bom2301"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "body" is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter 'body' when calling 'post_sustainabilitysummary_bom2301'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GetSustainabilitySummaryForBom2301Response",
        }

        return self.api_client.call_api(
            "/sustainability-summary/bom2301",
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
