# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import (
    CommonPartWithCompliance,
)  # noqa: E501
from .mocked_tests import generate_model


@pytest.mark.xfail(reason="No example payload in API definition")
def test_CommonPartWithCompliance():
    """Test CommonPartWithCompliance"""

    model = generate_model(CommonPartWithCompliance)
    assert model
