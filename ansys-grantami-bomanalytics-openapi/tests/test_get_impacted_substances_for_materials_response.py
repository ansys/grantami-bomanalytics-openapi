# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import GetImpactedSubstancesForMaterialsResponse  # noqa: E501
from .mocked_tests import generate_model



def test_GetImpactedSubstancesForMaterialsResponse():
    """Test GetImpactedSubstancesForMaterialsResponse"""

    model = generate_model(GetImpactedSubstancesForMaterialsResponse)
    assert model

