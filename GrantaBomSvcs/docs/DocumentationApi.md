# GrantaBomSvcs.DocumentationApi

All URIs are relative to *http://localhost/mi_servicelayer*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_miservicelayer_bom_analytics_v1svc_yaml**](DocumentationApi.md#get_miservicelayer_bom_analytics_v1svc_yaml) | **GET** /BomAnalytics/v1.svc/yaml | Provides the YAML specification for this service

# **get_miservicelayer_bom_analytics_v1svc_yaml**
> str get_miservicelayer_bom_analytics_v1svc_yaml()

Provides the YAML specification for this service

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
api_instance = GrantaBomSvcs.DocumentationApi(client)

try:
    # Provides the YAML specification for this service
    api_response = api_instance.get_miservicelayer_bom_analytics_v1svc_yaml()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentationApi->get_miservicelayer_bom_analytics_v1svc_yaml: %s\n" % e)
```

### Parameters
No parameters are required for this endpoint.

### Return type

**str**


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

