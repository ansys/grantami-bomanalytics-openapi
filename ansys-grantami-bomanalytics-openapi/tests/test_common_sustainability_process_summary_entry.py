# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import (
    CommonSustainabilityProcessSummaryEntry,
)  # noqa: E501
from .mocked_tests import generate_model


@pytest.mark.xfail(reason="No example payload in API definition")
def test_CommonSustainabilityProcessSummaryEntry():
    """Test CommonSustainabilityProcessSummaryEntry"""

    model = generate_model(CommonSustainabilityProcessSummaryEntry)
    assert model