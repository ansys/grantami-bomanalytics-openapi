# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import (
    GetComplianceForBom1711Request,
)  # noqa: E501
from .mocked_tests import generate_model


def test_GetComplianceForBom1711Request():
    """Test GetComplianceForBom1711Request"""

    model = generate_model(GetComplianceForBom1711Request)
    assert model
