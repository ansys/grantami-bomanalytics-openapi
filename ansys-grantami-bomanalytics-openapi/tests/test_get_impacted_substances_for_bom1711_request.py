# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import GetImpactedSubstancesForBom1711Request  # noqa: E501
from .mocked_tests import generate_model



def test_GetImpactedSubstancesForBom1711Request():
    """Test GetImpactedSubstancesForBom1711Request"""

    model = generate_model(GetImpactedSubstancesForBom1711Request)
    assert model

