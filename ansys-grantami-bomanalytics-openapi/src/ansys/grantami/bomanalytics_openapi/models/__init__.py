# coding: utf-8

# flake8: noqa
"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

# import Model ABC
from ansys.openapi.common import ModelBase

# import models into model package
from .common_coating_with_compliance import CommonCoatingWithCompliance
from .common_impacted_substance import CommonImpactedSubstance
from .common_indicator_definition import CommonIndicatorDefinition
from .common_indicator_result import CommonIndicatorResult
from .common_legislation_with_impacted_substances import (
    CommonLegislationWithImpactedSubstances,
)
from .common_log_entry import CommonLogEntry
from .common_material_reference import CommonMaterialReference
from .common_material_with_compliance import CommonMaterialWithCompliance
from .common_part_reference import CommonPartReference
from .common_part_with_compliance import CommonPartWithCompliance
from .common_request_config import CommonRequestConfig
from .common_specification_reference import CommonSpecificationReference
from .common_specification_with_compliance import CommonSpecificationWithCompliance
from .common_substance_with_compliance import CommonSubstanceWithCompliance
from .get_compliance_for_bom1711_request import GetComplianceForBom1711Request
from .get_compliance_for_bom1711_response import GetComplianceForBom1711Response
from .get_compliance_for_materials_request import GetComplianceForMaterialsRequest
from .get_compliance_for_materials_response import GetComplianceForMaterialsResponse
from .get_compliance_for_parts_request import GetComplianceForPartsRequest
from .get_compliance_for_parts_response import GetComplianceForPartsResponse
from .get_compliance_for_specifications_request import (
    GetComplianceForSpecificationsRequest,
)
from .get_compliance_for_specifications_response import (
    GetComplianceForSpecificationsResponse,
)
from .get_compliance_for_substances_request import GetComplianceForSubstancesRequest
from .get_compliance_for_substances_response import GetComplianceForSubstancesResponse
from .get_compliance_for_substances_substance_with_amount import (
    GetComplianceForSubstancesSubstanceWithAmount,
)
from .get_impacted_substances_for_bom1711_request import (
    GetImpactedSubstancesForBom1711Request,
)
from .get_impacted_substances_for_bom1711_response import (
    GetImpactedSubstancesForBom1711Response,
)
from .get_impacted_substances_for_materials_material import (
    GetImpactedSubstancesForMaterialsMaterial,
)
from .get_impacted_substances_for_materials_request import (
    GetImpactedSubstancesForMaterialsRequest,
)
from .get_impacted_substances_for_materials_response import (
    GetImpactedSubstancesForMaterialsResponse,
)
from .get_impacted_substances_for_parts_part import GetImpactedSubstancesForPartsPart
from .get_impacted_substances_for_parts_request import (
    GetImpactedSubstancesForPartsRequest,
)
from .get_impacted_substances_for_parts_response import (
    GetImpactedSubstancesForPartsResponse,
)
from .get_impacted_substances_for_specifications_request import (
    GetImpactedSubstancesForSpecificationsRequest,
)
from .get_impacted_substances_for_specifications_response import (
    GetImpactedSubstancesForSpecificationsResponse,
)
from .get_impacted_substances_for_specifications_specification import (
    GetImpactedSubstancesForSpecificationsSpecification,
)
