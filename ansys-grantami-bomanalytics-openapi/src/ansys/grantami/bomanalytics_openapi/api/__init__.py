# flake8: noqa

# import API ABC
from ansys.openapi.common import ApiBase

# import apis into api package
from .compliance_api import ComplianceApi
from .documentation_api import DocumentationApi
from .impacted_substances_api import ImpactedSubstancesApi
from .licenses_api import LicensesApi
from .sustainability_api import SustainabilityApi

__all__ = [
    "ApiBase",
    "ComplianceApi",
    "DocumentationApi",
    "ImpactedSubstancesApi",
    "LicensesApi",
    "SustainabilityApi",
]
