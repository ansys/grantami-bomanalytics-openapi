# ansys.grantami.bomanalytics_openapi.ImpactedSubstancesApi

All URIs are relative to *http://localhost/mi_servicelayer/BomAnalytics/v1.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_impactedsubstances_bom1711**](ImpactedSubstancesApi.md#post_impactedsubstances_bom1711) | **POST** /impacted-substances/bom1711 | Get the impacted substances for a BoM
[**post_impactedsubstances_materials**](ImpactedSubstancesApi.md#post_impactedsubstances_materials) | **POST** /impacted-substances/materials | Get the impacted substances for materials
[**post_impactedsubstances_parts**](ImpactedSubstancesApi.md#post_impactedsubstances_parts) | **POST** /impacted-substances/parts | Get the impacted substances for parts
[**post_impactedsubstances_specifications**](ImpactedSubstancesApi.md#post_impactedsubstances_specifications) | **POST** /impacted-substances/specifications | Get the impacted substances for specifications

# **post_impactedsubstances_bom1711**
> GetImpactedSubstancesForBom1711Response post_impactedsubstances_bom1711(body)

Get the impacted substances for a BoM

Examines the substances contained in the provided 17/11 BoM and reports the ones impacted by one or more of the provided legislations. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked specification, the one with the higher percentage amount will be reported.

### Example
```python
import ansys.grantami.bomanalytics_openapi
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(ansys.grantami.bomanalytics_openapi.models)

# create an instance of the API class
api_instance = ansys.grantami.bomanalytics_openapi.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for a BoM
    api_response = api_instance.post_impactedsubstances_bom1711(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_impactedsubstances_bom1711: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetImpactedSubstancesForBom1711Request**](GetImpactedSubstancesForBom1711Request.md)|  | 

### Return type

[**GetImpactedSubstancesForBom1711Response**](GetImpactedSubstancesForBom1711Response.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_impactedsubstances_materials**
> GetImpactedSubstancesForMaterialsResponse post_impactedsubstances_materials(body)

Get the impacted substances for materials

Examines the substances contained in the provided materials and reports the ones impacted by each of the provided legislations. There are four different ways in which a material can be referenced in the request - record GUID, record history GUID, record history identity, and material ID. There is no need to specify the table in which the material is defined, i.e. it can be either in the \"Materials in-house\" or \"MaterialUniverse\" table.

### Example
```python
import ansys.grantami.bomanalytics_openapi
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(ansys.grantami.bomanalytics_openapi.models)

# create an instance of the API class
api_instance = ansys.grantami.bomanalytics_openapi.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for materials
    api_response = api_instance.post_impactedsubstances_materials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_impactedsubstances_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetImpactedSubstancesForMaterialsRequest**](GetImpactedSubstancesForMaterialsRequest.md)|  | 

### Return type

[**GetImpactedSubstancesForMaterialsResponse**](GetImpactedSubstancesForMaterialsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_impactedsubstances_parts**
> GetImpactedSubstancesForPartsResponse post_impactedsubstances_parts(body)

Get the impacted substances for parts

Examines the substances contained in the provided parts by following links to substances, materials, and other parts, and reports the ones impacted by one or more of the provided legislations. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked specification, the one with the higher percentage amount will be reported.

### Example
```python
import ansys.grantami.bomanalytics_openapi
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(ansys.grantami.bomanalytics_openapi.models)

# create an instance of the API class
api_instance = ansys.grantami.bomanalytics_openapi.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for parts
    api_response = api_instance.post_impactedsubstances_parts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_impactedsubstances_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetImpactedSubstancesForPartsRequest**](GetImpactedSubstancesForPartsRequest.md)|  | 

### Return type

[**GetImpactedSubstancesForPartsResponse**](GetImpactedSubstancesForPartsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_impactedsubstances_specifications**
> GetImpactedSubstancesForSpecificationsResponse post_impactedsubstances_specifications(body)

Get the impacted substances for specifications

Examines the substances contained in the provided specifications by following links to substances, materials, coatings and other specifications, and reports the ones impacted by one or more of the provided legislations. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.

### Example
```python
import ansys.grantami.bomanalytics_openapi
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(ansys.grantami.bomanalytics_openapi.models)

# create an instance of the API class
api_instance = ansys.grantami.bomanalytics_openapi.ImpactedSubstancesApi(client)

try:
    # Get the impacted substances for specifications
    api_response = api_instance.post_impactedsubstances_specifications(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpactedSubstancesApi->post_impactedsubstances_specifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetImpactedSubstancesForSpecificationsRequest**](GetImpactedSubstancesForSpecificationsRequest.md)|  | 

### Return type

[**GetImpactedSubstancesForSpecificationsResponse**](GetImpactedSubstancesForSpecificationsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

