# ansys.grantami.bomanalytics_openapi.ComplianceApi

All URIs are relative to *http://localhost/mi_servicelayer/BomAnalytics/v1.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_compliance_bom1711**](ComplianceApi.md#post_compliance_bom1711) | **POST** /compliance/bom1711 | Determine the compliance of a BoM in the context of specified indicators
[**post_compliance_materials**](ComplianceApi.md#post_compliance_materials) | **POST** /compliance/materials | Determine the compliance of one or more materials in the context of specified indicators
[**post_compliance_parts**](ComplianceApi.md#post_compliance_parts) | **POST** /compliance/parts | Determine the compliance of one or more parts in the context of specified indicators
[**post_compliance_specifications**](ComplianceApi.md#post_compliance_specifications) | **POST** /compliance/specifications | Determine the compliance of one or more specifications in the context of specified indicators
[**post_compliance_substances**](ComplianceApi.md#post_compliance_substances) | **POST** /compliance/substances | Determine the compliance of one or more substances in the context of specified indicators

# **post_compliance_bom1711**
> GetComplianceForBom1711Response post_compliance_bom1711(body)

Determine the compliance of a BoM in the context of specified indicators

Compliance is determined first by identifying the substances contained within the parts defined in the BoM, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, specifications, and sub-parts, to determine the compliance of the parts included in the BoM. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex part hierarchies. References to Granta MI records are constructed as 'GrantaBaseType' RecordReferences; see the 17/11 BoM schema for more details on how to construct a valid BoM.  Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator. The RoHS Indicator includes an additional parameter 'ignoreExemptions'. Setting this to true will result in the compliance analysis ignoring RoHS exemptions, forcing all parts that contain substances over the threshold to be reported as Non-Compliant. This setting defaults to false if not set, meaning exemptions will be applied and such a part would be reported as 'Compliant with Exemptions'. The parameter has no effect if used either on a non-part Compliance query (since only parts can have RoHS exemptions), or with a Watch List Indicator.

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
api_instance = ansys.grantami.bomanalytics_openapi.ComplianceApi(client)

try:
    # Determine the compliance of a BoM in the context of specified indicators
    api_response = api_instance.post_compliance_bom1711(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_compliance_bom1711: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetComplianceForBom1711Request**](GetComplianceForBom1711Request.md)|  | 

### Return type

[**GetComplianceForBom1711Response**](GetComplianceForBom1711Response.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_compliance_materials**
> GetComplianceForMaterialsResponse post_compliance_materials(body)

Determine the compliance of one or more materials in the context of specified indicators

Compliance is determined first by identifying the substances contained within the materials, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances to the parent materials to determine material compliance. This endpoint reports the compliance result for both the materials and substances. A material can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or material ID. The table that contains the material of interest is not required, materials will be discovered if they are present in either in the \"Materials in-house\" or \"MaterialUniverse\" tables. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator.

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
api_instance = ansys.grantami.bomanalytics_openapi.ComplianceApi(client)

try:
    # Determine the compliance of one or more materials in the context of specified indicators
    api_response = api_instance.post_compliance_materials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_compliance_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetComplianceForMaterialsRequest**](GetComplianceForMaterialsRequest.md)|  | 

### Return type

[**GetComplianceForMaterialsResponse**](GetComplianceForMaterialsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_compliance_parts**
> GetComplianceForPartsResponse post_compliance_parts(body)

Determine the compliance of one or more parts in the context of specified indicators

Compliance is determined first by identifying the substances contained within the parts, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, specifications, and sub-parts, to determine the compliance of the parts included in the request. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex part hierarchies. A part can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or part number. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator. The RoHS Indicator includes an additional parameter 'ignoreExemptions'. Setting this to true will result in the compliance analysis ignoring RoHS exemptions, forcing all parts that contain substances over the threshold to be reported as Non-Compliant. This setting defaults to false if not set, meaning exemptions will be applied and such a part would be reported as 'Compliant with Exemptions'. The parameter has no effect if used either on a non-part Compliance query (since only parts can have RoHS exemptions), or with a Watch List Indicator.

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
api_instance = ansys.grantami.bomanalytics_openapi.ComplianceApi(client)

try:
    # Determine the compliance of one or more parts in the context of specified indicators
    api_response = api_instance.post_compliance_parts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_compliance_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetComplianceForPartsRequest**](GetComplianceForPartsRequest.md)|  | 

### Return type

[**GetComplianceForPartsResponse**](GetComplianceForPartsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_compliance_specifications**
> GetComplianceForSpecificationsResponse post_compliance_specifications(body)

Determine the compliance of one or more specifications in the context of specified indicators

Compliance is determined first by identifying the substances contained within the specifications, either directly or indirectly, and then calculating the compliance status of those substances against the specified indicators. The worst compliance results are then rolled-up from the substances, through any intermediate coatings, materials, and specifications, to determine the compliance of the specifications included in the request. This endpoint reports the compliance result at every level, and as a result the response can be very large for complex specification hierarchies. A specification can be referenced by one of four different identifiers: record GUID, record history GUID, record history identity, or specification ID. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold. The Watch List Indicator includes an additional parameter 'ignoreProcessChemicals'. Setting this to true will ignore any chemicals that have been set as process chemicals in Granta MI, indicating that they are not present in the finished article. This setting defaults to false if not set, meaning process chemicals are included in the compliance analysis. The parameter has no effect if used on a Substance Compliance query, and has no effect if used with a RoHS Indicator.

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
api_instance = ansys.grantami.bomanalytics_openapi.ComplianceApi(client)

try:
    # Determine the compliance of one or more specifications in the context of specified indicators
    api_response = api_instance.post_compliance_specifications(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_compliance_specifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetComplianceForSpecificationsRequest**](GetComplianceForSpecificationsRequest.md)|  | 

### Return type

[**GetComplianceForSpecificationsResponse**](GetComplianceForSpecificationsResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_compliance_substances**
> GetComplianceForSubstancesResponse post_compliance_substances(body)

Determine the compliance of one or more substances in the context of specified indicators

Compliance is determined by comparing the substance quantity against the threshold defined for that indicator. The response includes the compliance status for each substance for each indicator. A substance can be referenced by one of six different identifiers: record GUID, record history GUID, record history identity, CAS Number, EC Number, or Chemical Name. The amount of substance is also required, since generally a substance is only non-compliant over a certain threshold. Two indicator types are currently implemented, a RoHS Indicator and a Watch List Indicator. These indicators are intended to be used with RoHS-type legislations and REACH-type legislations respectively, but this is not enforced in the API. Both indicator types are defined in terms of one or more legislations against which compliance will be determined, and an optional default substance threshold.

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
api_instance = ansys.grantami.bomanalytics_openapi.ComplianceApi(client)

try:
    # Determine the compliance of one or more substances in the context of specified indicators
    api_response = api_instance.post_compliance_substances(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->post_compliance_substances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetComplianceForSubstancesRequest**](GetComplianceForSubstancesRequest.md)|  | 

### Return type

[**GetComplianceForSubstancesResponse**](GetComplianceForSubstancesResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

