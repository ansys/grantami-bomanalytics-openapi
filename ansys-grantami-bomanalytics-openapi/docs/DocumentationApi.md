# ansys.grantami.bomanalytics_openapi.DocumentationApi

All URIs are relative to *http://localhost/mi_servicelayer/BomAnalytics/v1.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_yaml**](DocumentationApi.md#get_yaml) | **GET** /yaml | Provides the YAML specification for this service.

# **get_yaml**
> str get_yaml()

Provides the YAML specification for this service.

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
api_instance = ansys.grantami.bomanalytics_openapi.DocumentationApi(client)

try:
    # Provides the YAML specification for this service.
    api_response = api_instance.get_yaml()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentationApi->get_yaml: %s\n" % e)
```

### Parameters
No parameters are required for this endpoint.

### Return type

**str**


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

