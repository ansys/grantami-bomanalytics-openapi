# GrantaBomSvcs.ComplianceApi

All URIs are relative to *http://localhost/mi_servicelayer*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_miservicelayer_bom_analytics_v1svc_compliance_bom1711**](ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_bom1711) | **POST** /BomAnalytics/v1.svc/compliance/bom1711 | Get the compliance for a BoM
[**post_miservicelayer_bom_analytics_v1svc_compliance_materials**](ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_materials) | **POST** /BomAnalytics/v1.svc/compliance/materials | Get compliance for materials
[**post_miservicelayer_bom_analytics_v1svc_compliance_parts**](ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_parts) | **POST** /BomAnalytics/v1.svc/compliance/parts | Get compliance for parts
[**post_miservicelayer_bom_analytics_v1svc_compliance_specifications**](ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_specifications) | **POST** /BomAnalytics/v1.svc/compliance/specifications | Get compliance for specifications
[**post_miservicelayer_bom_analytics_v1svc_compliance_substances**](ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_substances) | **POST** /BomAnalytics/v1.svc/compliance/substances | Get compliance for substances

# **post_miservicelayer_bom_analytics_v1svc_compliance_bom1711**
> GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Response post_miservicelayer_bom_analytics_v1svc_compliance_bom1711(body)

Get the compliance for a BoM

Performs compliance analysis on the provided 17/11 BoM in the context of the specified indicator definitions.

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
api_instance = GrantaBomSvcs.ComplianceApi(client)

try:
    # Get the compliance for a BoM
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_compliance_bom1711(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_miservicelayer_bom_analytics_v1svc_compliance_bom1711: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Request**](GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Request.md)|  | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Response**](GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Response.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_compliance_materials**
> GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsResponse post_miservicelayer_bom_analytics_v1svc_compliance_materials(body)

Get compliance for materials

Performs compliance analysis on the provided materials in the context of the specified indicator definitions.

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
api_instance = GrantaBomSvcs.ComplianceApi(client)

try:
    # Get compliance for materials
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_compliance_materials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_miservicelayer_bom_analytics_v1svc_compliance_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest**](GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.md)| A set of materials references. The substance amounts in each material will be     compared to the legislation thresholds to determine whether the substance is below or above it. | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsResponse**](GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_compliance_parts**
> GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsResponse post_miservicelayer_bom_analytics_v1svc_compliance_parts(body)

Get compliance for parts

Performs compliance analysis on the provided parts in the context of the specified indicator definitions.

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
api_instance = GrantaBomSvcs.ComplianceApi(client)

try:
    # Get compliance for parts
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_compliance_parts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_miservicelayer_bom_analytics_v1svc_compliance_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsRequest**](GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsRequest.md)| A set of part references. | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsResponse**](GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_compliance_specifications**
> GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsResponse post_miservicelayer_bom_analytics_v1svc_compliance_specifications(body)

Get compliance for specifications

Performs compliance analysis on the provided specifications in the context of the specified indicator definitions.

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
api_instance = GrantaBomSvcs.ComplianceApi(client)

try:
    # Get compliance for specifications
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_compliance_specifications(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_miservicelayer_bom_analytics_v1svc_compliance_specifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsRequest**](GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsRequest.md)| A set of specification references. | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsResponse**](GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_miservicelayer_bom_analytics_v1svc_compliance_substances**
> GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesResponse post_miservicelayer_bom_analytics_v1svc_compliance_substances(body)

Get compliance for substances

Performs compliance analysis on the provided substances in the context of the specified indicator definitions.

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
api_instance = GrantaBomSvcs.ComplianceApi(client)

try:
    # Get compliance for substances
    api_response = api_instance.post_miservicelayer_bom_analytics_v1svc_compliance_substances(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_miservicelayer_bom_analytics_v1svc_compliance_substances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesRequest**](GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesRequest.md)| A set of substance references with their corresponding percentage amounts. The amounts will be     compared to the legislation thresholds to determine whether the substance is below or above it. | 

### Return type

[**GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesResponse**](GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

