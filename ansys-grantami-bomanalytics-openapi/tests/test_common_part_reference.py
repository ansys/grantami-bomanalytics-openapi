# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import CommonPartReference  # noqa: E501
from .common import generate_model


@pytest.mark.xfail(reason="No example payload in API definition")
def test_CommonPartReference():
    """Test CommonPartReference"""

    model = generate_model(CommonPartReference)
    assert model

