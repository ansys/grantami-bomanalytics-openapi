# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import CommonSubstanceWithCompliance  # noqa: E501
from .common import generate_model


@pytest.mark.xfail(reason="No example payload in API definition")
def test_CommonSubstanceWithCompliance():
    """Test CommonSubstanceWithCompliance"""

    model = generate_model(CommonSubstanceWithCompliance)
    assert model

