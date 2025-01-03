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

# import Model ABC
from ansys.openapi.common import ModelBase, Unset, Unset_Type

# import models into model package
from .common_coating_with_compliance import CommonCoatingWithCompliance
from .common_impacted_substance import CommonImpactedSubstance
from .common_indicator_definition import CommonIndicatorDefinition
from .common_indicator_result import CommonIndicatorResult
from .common_legislation_with_impacted_substances import CommonLegislationWithImpactedSubstances
from .common_log_entry import CommonLogEntry
from .common_material_reference import CommonMaterialReference
from .common_material_with_compliance import CommonMaterialWithCompliance
from .common_part_reference import CommonPartReference
from .common_part_with_compliance import CommonPartWithCompliance
from .common_preferred_units import CommonPreferredUnits
from .common_process_reference import CommonProcessReference
from .common_request_config import CommonRequestConfig
from .common_specification_reference import CommonSpecificationReference
from .common_specification_with_compliance import CommonSpecificationWithCompliance
from .common_substance_with_compliance import CommonSubstanceWithCompliance
from .common_sustainability_material_contributing_component import (
    CommonSustainabilityMaterialContributingComponent,
)
from .common_sustainability_material_summary import CommonSustainabilityMaterialSummary
from .common_sustainability_material_summary_entry import CommonSustainabilityMaterialSummaryEntry
from .common_sustainability_material_with_sustainability import (
    CommonSustainabilityMaterialWithSustainability,
)
from .common_sustainability_part_with_sustainability import (
    CommonSustainabilityPartWithSustainability,
)
from .common_sustainability_phase_summary import CommonSustainabilityPhaseSummary
from .common_sustainability_process_summary import CommonSustainabilityProcessSummary
from .common_sustainability_process_summary_entry import CommonSustainabilityProcessSummaryEntry
from .common_sustainability_process_with_sustainability import (
    CommonSustainabilityProcessWithSustainability,
)
from .common_sustainability_transport_summary import CommonSustainabilityTransportSummary
from .common_sustainability_transport_summary_entry import CommonSustainabilityTransportSummaryEntry
from .common_sustainability_transport_with_sustainability import (
    CommonSustainabilityTransportWithSustainability,
)
from .common_transport_reference import CommonTransportReference
from .common_value_with_unit import CommonValueWithUnit
from .get_available_licenses_response import GetAvailableLicensesResponse
from .get_compliance_for_bom1711_request import GetComplianceForBom1711Request
from .get_compliance_for_bom1711_response import GetComplianceForBom1711Response
from .get_compliance_for_bom2301_request import GetComplianceForBom2301Request
from .get_compliance_for_bom2301_response import GetComplianceForBom2301Response
from .get_compliance_for_materials_request import GetComplianceForMaterialsRequest
from .get_compliance_for_materials_response import GetComplianceForMaterialsResponse
from .get_compliance_for_parts_request import GetComplianceForPartsRequest
from .get_compliance_for_parts_response import GetComplianceForPartsResponse
from .get_compliance_for_specifications_request import GetComplianceForSpecificationsRequest
from .get_compliance_for_specifications_response import GetComplianceForSpecificationsResponse
from .get_compliance_for_substances_request import GetComplianceForSubstancesRequest
from .get_compliance_for_substances_response import GetComplianceForSubstancesResponse
from .get_compliance_for_substances_substance_with_amount import (
    GetComplianceForSubstancesSubstanceWithAmount,
)
from .get_impacted_substances_for_bom1711_request import GetImpactedSubstancesForBom1711Request
from .get_impacted_substances_for_bom1711_response import GetImpactedSubstancesForBom1711Response
from .get_impacted_substances_for_bom2301_request import GetImpactedSubstancesForBom2301Request
from .get_impacted_substances_for_bom2301_response import GetImpactedSubstancesForBom2301Response
from .get_impacted_substances_for_materials_material import (
    GetImpactedSubstancesForMaterialsMaterial,
)
from .get_impacted_substances_for_materials_request import GetImpactedSubstancesForMaterialsRequest
from .get_impacted_substances_for_materials_response import (
    GetImpactedSubstancesForMaterialsResponse,
)
from .get_impacted_substances_for_parts_part import GetImpactedSubstancesForPartsPart
from .get_impacted_substances_for_parts_request import GetImpactedSubstancesForPartsRequest
from .get_impacted_substances_for_parts_response import GetImpactedSubstancesForPartsResponse
from .get_impacted_substances_for_specifications_request import (
    GetImpactedSubstancesForSpecificationsRequest,
)
from .get_impacted_substances_for_specifications_response import (
    GetImpactedSubstancesForSpecificationsResponse,
)
from .get_impacted_substances_for_specifications_specification import (
    GetImpactedSubstancesForSpecificationsSpecification,
)
from .get_sustainability_for_bom2301_request import GetSustainabilityForBom2301Request
from .get_sustainability_for_bom2301_response import GetSustainabilityForBom2301Response
from .get_sustainability_summary_for_bom2301_request import (
    GetSustainabilitySummaryForBom2301Request,
)
from .get_sustainability_summary_for_bom2301_response import (
    GetSustainabilitySummaryForBom2301Response,
)

__all__ = [
    "ModelBase",
    "Unset",
    "Unset_Type",
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
