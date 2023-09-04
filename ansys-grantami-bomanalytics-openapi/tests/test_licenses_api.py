# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
import requests_mock

from ansys.grantami.bomanalytics_openapi.api.licenses_api import (
    LicensesApi,
)  # noqa: E501
from ansys.grantami.bomanalytics_openapi.models.get_available_licenses_response import (
    GetAvailableLicensesResponse,
)
from .mocked_tests import generate_model, get_example, mock_method


class TestLicensesApi:
    """LicensesApi unit test stubs"""

    def test_get_licenses(self, api_client):
        """Test case for get_licenses
        Determine if Restricted Substances and Sustainability licenses are available  # noqa: E501
        """
        client = LicensesApi(api_client)
        with requests_mock.Mocker() as m:
            mock_method(
                m,
                "GET",
                "http://localhost/mi_servicelayer/BomAnalytics/v1.svc/licenses",
                get_example(GetAvailableLicensesResponse),
            )
            result = client.get_licenses()
        assert isinstance(result, GetAvailableLicensesResponse)
