# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import (
    CommonIndicatorResult,
)  # noqa: E501
from .mocked_tests import generate_model


@pytest.mark.xfail(reason="No example payload in API definition")
def test_CommonIndicatorResult():
    """Test CommonIndicatorResult"""

    model = generate_model(CommonIndicatorResult)
    assert model
