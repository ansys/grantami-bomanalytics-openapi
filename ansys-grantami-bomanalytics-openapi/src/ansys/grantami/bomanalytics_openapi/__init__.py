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

# flake8: noqa

"""
Granta.BomAnalyticsServices.V1

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: V1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

# import apis into sdk package
from .api.compliance_api import ComplianceApi
from .api.documentation_api import DocumentationApi
from .api.impacted_substances_api import ImpactedSubstancesApi
from .api.licenses_api import LicensesApi
from .api.sustainability_api import SustainabilityApi

# import models into sdk package
from .models.common_coating_with_compliance import CommonCoatingWithCompliance
from .models.common_impacted_substance import CommonImpactedSubstance
from .models.common_indicator_definition import CommonIndicatorDefinition
from .models.common_indicator_result import CommonIndicatorResult
from .models.common_legislation_with_impacted_substances import (
    CommonLegislationWithImpactedSubstances,
)
from .models.common_log_entry import CommonLogEntry
from .models.common_material_reference import CommonMaterialReference
from .models.common_material_with_compliance import CommonMaterialWithCompliance
from .models.common_part_reference import CommonPartReference
from .models.common_part_with_compliance import CommonPartWithCompliance
from .models.common_preferred_units import CommonPreferredUnits
from .models.common_process_reference import CommonProcessReference
from .models.common_request_config import CommonRequestConfig
from .models.common_specification_reference import CommonSpecificationReference
from .models.common_specification_with_compliance import CommonSpecificationWithCompliance
from .models.common_substance_with_compliance import CommonSubstanceWithCompliance
from .models.common_sustainability_material_contributing_component import (
    CommonSustainabilityMaterialContributingComponent,
)
from .models.common_sustainability_material_summary import CommonSustainabilityMaterialSummary
from .models.common_sustainability_material_summary_entry import (
    CommonSustainabilityMaterialSummaryEntry,
)
from .models.common_sustainability_material_with_sustainability import (
    CommonSustainabilityMaterialWithSustainability,
)
from .models.common_sustainability_part_with_sustainability import (
    CommonSustainabilityPartWithSustainability,
)
from .models.common_sustainability_phase_summary import CommonSustainabilityPhaseSummary
from .models.common_sustainability_process_summary import CommonSustainabilityProcessSummary
from .models.common_sustainability_process_summary_entry import (
    CommonSustainabilityProcessSummaryEntry,
)
from .models.common_sustainability_process_with_sustainability import (
    CommonSustainabilityProcessWithSustainability,
)
from .models.common_sustainability_transport_by_category_summary_entry import (
    CommonSustainabilityTransportByCategorySummaryEntry,
)
from .models.common_sustainability_transport_by_part_summary_entry import (
    CommonSustainabilityTransportByPartSummaryEntry,
)
from .models.common_sustainability_transport_summary import CommonSustainabilityTransportSummary
from .models.common_sustainability_transport_summary_entry import (
    CommonSustainabilityTransportSummaryEntry,
)
from .models.common_sustainability_transport_with_sustainability import (
    CommonSustainabilityTransportWithSustainability,
)
from .models.common_transport_reference import CommonTransportReference
from .models.common_value_with_unit import CommonValueWithUnit
from .models.get_available_licenses_response import GetAvailableLicensesResponse
from .models.get_compliance_for_bom1711_request import GetComplianceForBom1711Request
from .models.get_compliance_for_bom1711_response import GetComplianceForBom1711Response
from .models.get_compliance_for_bom2301_request import GetComplianceForBom2301Request
from .models.get_compliance_for_bom2301_response import GetComplianceForBom2301Response
from .models.get_compliance_for_materials_request import GetComplianceForMaterialsRequest
from .models.get_compliance_for_materials_response import GetComplianceForMaterialsResponse
from .models.get_compliance_for_parts_request import GetComplianceForPartsRequest
from .models.get_compliance_for_parts_response import GetComplianceForPartsResponse
from .models.get_compliance_for_specifications_request import GetComplianceForSpecificationsRequest
from .models.get_compliance_for_specifications_response import (
    GetComplianceForSpecificationsResponse,
)
from .models.get_compliance_for_substances_request import GetComplianceForSubstancesRequest
from .models.get_compliance_for_substances_response import GetComplianceForSubstancesResponse
from .models.get_compliance_for_substances_substance_with_amount import (
    GetComplianceForSubstancesSubstanceWithAmount,
)
from .models.get_impacted_substances_for_bom1711_request import (
    GetImpactedSubstancesForBom1711Request,
)
from .models.get_impacted_substances_for_bom1711_response import (
    GetImpactedSubstancesForBom1711Response,
)
from .models.get_impacted_substances_for_bom2301_request import (
    GetImpactedSubstancesForBom2301Request,
)
from .models.get_impacted_substances_for_bom2301_response import (
    GetImpactedSubstancesForBom2301Response,
)
from .models.get_impacted_substances_for_materials_material import (
    GetImpactedSubstancesForMaterialsMaterial,
)
from .models.get_impacted_substances_for_materials_request import (
    GetImpactedSubstancesForMaterialsRequest,
)
from .models.get_impacted_substances_for_materials_response import (
    GetImpactedSubstancesForMaterialsResponse,
)
from .models.get_impacted_substances_for_parts_part import GetImpactedSubstancesForPartsPart
from .models.get_impacted_substances_for_parts_request import GetImpactedSubstancesForPartsRequest
from .models.get_impacted_substances_for_parts_response import GetImpactedSubstancesForPartsResponse
from .models.get_impacted_substances_for_specifications_request import (
    GetImpactedSubstancesForSpecificationsRequest,
)
from .models.get_impacted_substances_for_specifications_response import (
    GetImpactedSubstancesForSpecificationsResponse,
)
from .models.get_impacted_substances_for_specifications_specification import (
    GetImpactedSubstancesForSpecificationsSpecification,
)
from .models.get_sustainability_for_bom2301_request import GetSustainabilityForBom2301Request
from .models.get_sustainability_for_bom2301_response import GetSustainabilityForBom2301Response
from .models.get_sustainability_summary_for_bom2301_request import (
    GetSustainabilitySummaryForBom2301Request,
)
from .models.get_sustainability_summary_for_bom2301_response import (
    GetSustainabilitySummaryForBom2301Response,
)

__all__ = [
    "ComplianceApi",
    "DocumentationApi",
    "ImpactedSubstancesApi",
    "LicensesApi",
    "SustainabilityApi",
    "CommonCoatingWithCompliance",
    "CommonImpactedSubstance",
    "CommonIndicatorDefinition",
    "CommonIndicatorResult",
    "CommonLegislationWithImpactedSubstances",
    "CommonLogEntry",
    "CommonMaterialReference",
    "CommonMaterialWithCompliance",
    "CommonPartReference",
    "CommonPartWithCompliance",
    "CommonPreferredUnits",
    "CommonProcessReference",
    "CommonRequestConfig",
    "CommonSpecificationReference",
    "CommonSpecificationWithCompliance",
    "CommonSubstanceWithCompliance",
    "CommonSustainabilityMaterialContributingComponent",
    "CommonSustainabilityMaterialSummary",
    "CommonSustainabilityMaterialSummaryEntry",
    "CommonSustainabilityMaterialWithSustainability",
    "CommonSustainabilityPartWithSustainability",
    "CommonSustainabilityPhaseSummary",
    "CommonSustainabilityProcessSummary",
    "CommonSustainabilityProcessSummaryEntry",
    "CommonSustainabilityProcessWithSustainability",
    "CommonSustainabilityTransportByCategorySummaryEntry",
    "CommonSustainabilityTransportByPartSummaryEntry",
    "CommonSustainabilityTransportSummary",
    "CommonSustainabilityTransportSummaryEntry",
    "CommonSustainabilityTransportWithSustainability",
    "CommonTransportReference",
    "CommonValueWithUnit",
    "GetAvailableLicensesResponse",
    "GetComplianceForBom1711Request",
    "GetComplianceForBom1711Response",
    "GetComplianceForBom2301Request",
    "GetComplianceForBom2301Response",
    "GetComplianceForMaterialsRequest",
    "GetComplianceForMaterialsResponse",
    "GetComplianceForPartsRequest",
    "GetComplianceForPartsResponse",
    "GetComplianceForSpecificationsRequest",
    "GetComplianceForSpecificationsResponse",
    "GetComplianceForSubstancesRequest",
    "GetComplianceForSubstancesResponse",
    "GetComplianceForSubstancesSubstanceWithAmount",
    "GetImpactedSubstancesForBom1711Request",
    "GetImpactedSubstancesForBom1711Response",
    "GetImpactedSubstancesForBom2301Request",
    "GetImpactedSubstancesForBom2301Response",
    "GetImpactedSubstancesForMaterialsMaterial",
    "GetImpactedSubstancesForMaterialsRequest",
    "GetImpactedSubstancesForMaterialsResponse",
    "GetImpactedSubstancesForPartsPart",
    "GetImpactedSubstancesForPartsRequest",
    "GetImpactedSubstancesForPartsResponse",
    "GetImpactedSubstancesForSpecificationsRequest",
    "GetImpactedSubstancesForSpecificationsResponse",
    "GetImpactedSubstancesForSpecificationsSpecification",
    "GetSustainabilityForBom2301Request",
    "GetSustainabilityForBom2301Response",
    "GetSustainabilitySummaryForBom2301Request",
    "GetSustainabilitySummaryForBom2301Response",
]
