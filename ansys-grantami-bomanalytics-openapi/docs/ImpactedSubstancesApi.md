# ansys.grantami.bomanalytics_openapi.ImpactedSubstancesApi

All URIs are relative to *http://localhost/mi_servicelayer/BomAnalytics/v1.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_impactedsubstances_bom1711**](ImpactedSubstancesApi.md#post_impactedsubstances_bom1711) | **POST** /impacted-substances/bom1711 | Get the impacted substances for a Bill of Materials
[**post_impactedsubstances_materials**](ImpactedSubstancesApi.md#post_impactedsubstances_materials) | **POST** /impacted-substances/materials | Get the impacted substances for materials
[**post_impactedsubstances_parts**](ImpactedSubstancesApi.md#post_impactedsubstances_parts) | **POST** /impacted-substances/parts | Get the impacted substances for parts
[**post_impactedsubstances_specifications**](ImpactedSubstancesApi.md#post_impactedsubstances_specifications) | **POST** /impacted-substances/specifications | Get the impacted substances for specifications

# **post_impactedsubstances_bom1711**
> GetImpactedSubstancesForBom1711Response post_impactedsubstances_bom1711(body)

Get the impacted substances for a Bill of Materials

Examines the substances contained within a 17/11 Bill of Materials (BoM) by following links to substances, materials, specifications, and parts, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null.  If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.  References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 17/11 BoM schema for more details on how to construct a valid BoM. Legislations are specified by the legislation 'Short title' attribute.

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
    # Get the impacted substances for a Bill of Materials
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

Examines the substances contained within one or more materials and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the material and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null. A material can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or material ID. The table that contains the material of interest is not required, materials will be discovered if they are present in either in the \"Materials in-house\" or \"MaterialUniverse\" tables. Legislations are specified by the legislation 'Short title' attribute.

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

Examines the substances contained within one or more parts by following links to substances, materials, specifications and other parts, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null.  If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported.  A part can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or part number. Legislations are specified by the legislation 'Short title' attribute.

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

Examines the substances contained within one or more specifications by following links to substances, materials, coatings and other specifications, and reports those that are impacted by the specified legislations. Each substance includes the quantity of that substance in the parent and the quantity threshold imposed on that substance by the relevant legislation. Both the quantity and threshold are only reported if present in Granta MI, otherwise they are null. If the same substance is impacted in more than one place, e.g. once in a linked material and once in a linked coating, the one with the higher percentage amount will be reported. A specification can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or specification ID. Legislations are specified by the legislation 'Short title' attribute.

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

