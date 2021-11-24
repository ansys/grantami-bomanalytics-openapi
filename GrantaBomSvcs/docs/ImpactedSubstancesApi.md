# GrantaBomSvcs.ImpactedSubstancesApi

All URIs are relative to *http://localhost/mi_servicelayer*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711**](ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711) | **POST** /BomAnalytics/v1.svc/impacted-substances/bom1711 | Get the impacted substances for a BoM
[**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials**](ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials) | **POST** /BomAnalytics/v1.svc/impacted-substances/materials | Get the impacted substances for materials.
[**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts**](ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts) | **POST** /BomAnalytics/v1.svc/impacted-substances/parts | Get the impacted substances for parts
[**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications**](ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications) | **POST** /BomAnalytics/v1.svc/impacted-substances/specifications | Get the impacted substances for specifications

# **post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711**
> GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Response post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711(body)

Get the impacted substances for a BoM

Examines the substances contained in the provided 17/11 BoM and reports the ones impacted by one or more of the provided legislations. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked specification, the one with the higher percentage amount will be reported.

### Example
```python
import GrantaBomSvcs
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(GrantaBomSvcs.models)

# create an instance of the API class
api_instance = GrantaBomSvcs.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for a BoM
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request.md)|  | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Response**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Response.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials**
> GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials(body)

Get the impacted substances for materials.

Examines the substances contained in the provided materials and reports the ones impacted by each of the provided legislations. There are four different ways in which a material can be referenced in the request - record GUID, record history GUID, record history identity, and material ID. There is no need to specify the table in which the material is defined, i.e. it can be either in the \"Materials in-house\" or \"MaterialUniverse\" table.

### Example
```python
import GrantaBomSvcs
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(GrantaBomSvcs.models)

# create an instance of the API class
api_instance = GrantaBomSvcs.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for materials.
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsRequest**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsRequest.md)|  | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts**
> GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsResponse post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts(body)

Get the impacted substances for parts

Examines the substances contained in the provided parts by following links to substances, materials, and other parts, and reports the ones impacted by one or more of the provided legislations. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked specification, the one with the higher percentage amount will be reported.

### Example
```python
import GrantaBomSvcs
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(GrantaBomSvcs.models)

# create an instance of the API class
api_instance = GrantaBomSvcs.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for parts
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsRequest**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsRequest.md)|  | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsResponse**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications**
> GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications(body)

Get the impacted substances for specifications

Examines the substances contained in the provided specifications by following links to substances, materials, coatings and other specifications, and reports the ones impacted by one or more of the provided legislations. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.

### Example
```python
import GrantaBomSvcs
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(GrantaBomSvcs.models)

# create an instance of the API class
api_instance = GrantaBomSvcs.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for specifications
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsRequest**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsRequest.md)|  | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse**](GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

