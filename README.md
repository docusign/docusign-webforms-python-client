# docusign-webforms
The Web Forms API facilitates generating semantic HTML forms around everyday contracts. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developers.docusign.com/](https://developers.docusign.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import docusign_webforms 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import docusign_webforms
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import docusign_webforms
from docusign_webforms.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: docusignAccessCode
configuration = docusign_webforms.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = docusign_webforms.FormInstanceManagementApi(docusign_webforms.ApiClient(configuration))
account_id = 'account_id_example' # str | Account identifier in which the web form resides
form_id = 'form_id_example' # str | Unique identifier for a web form entity that is consistent for it's lifetime
create_instance_body = docusign_webforms.CreateInstanceRequestBody() # CreateInstanceRequestBody | Request body containing properties that will be used to create instance.

try:
    # Creates an instance of the web form
    api_response = api_instance.create_instance(account_id, form_id, create_instance_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormInstanceManagementApi->create_instance: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://www.docusign.net/webforms/v1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FormInstanceManagementApi* | [**create_instance**](docs/FormInstanceManagementApi.md#create_instance) | **POST** /accounts/{account_id}/forms/{form_id}/instances | Creates an instance of the web form
*FormInstanceManagementApi* | [**get_instance**](docs/FormInstanceManagementApi.md#get_instance) | **GET** /accounts/{account_id}/forms/{form_id}/instances/{instance_id} | Get form instance
*FormInstanceManagementApi* | [**list_instances**](docs/FormInstanceManagementApi.md#list_instances) | **GET** /accounts/{account_id}/forms/{form_id}/instances | List instances
*FormInstanceManagementApi* | [**refresh_token**](docs/FormInstanceManagementApi.md#refresh_token) | **POST** /accounts/{account_id}/forms/{form_id}/instances/{instance_id}/refresh | Refreshes the instance token
*FormManagementApi* | [**get_form**](docs/FormManagementApi.md#get_form) | **GET** /accounts/{account_id}/forms/{form_id} | Get Form
*FormManagementApi* | [**list_forms**](docs/FormManagementApi.md#list_forms) | **GET** /accounts/{account_id}/forms | List Forms


## Documentation For Models

 - [AuthenticationMethod](docs/AuthenticationMethod.md)
 - [CreateInstanceRequestBody](docs/CreateInstanceRequestBody.md)
 - [HttpError](docs/HttpError.md)
 - [HttpSuccess](docs/HttpSuccess.md)
 - [InstanceSource](docs/InstanceSource.md)
 - [InstanceStatus](docs/InstanceStatus.md)
 - [TemplateProperties](docs/TemplateProperties.md)
 - [WebForm](docs/WebForm.md)
 - [WebFormComponentType](docs/WebFormComponentType.md)
 - [WebFormContent](docs/WebFormContent.md)
 - [WebFormInstance](docs/WebFormInstance.md)
 - [WebFormInstanceEnvelopes](docs/WebFormInstanceEnvelopes.md)
 - [WebFormInstanceList](docs/WebFormInstanceList.md)
 - [WebFormInstanceMetadata](docs/WebFormInstanceMetadata.md)
 - [WebFormMetadata](docs/WebFormMetadata.md)
 - [WebFormProperties](docs/WebFormProperties.md)
 - [WebFormSource](docs/WebFormSource.md)
 - [WebFormState](docs/WebFormState.md)
 - [WebFormSummary](docs/WebFormSummary.md)
 - [WebFormSummaryList](docs/WebFormSummaryList.md)
 - [WebFormUserInfo](docs/WebFormUserInfo.md)
 - [WebFormValues](docs/WebFormValues.md)


## Documentation For Authorization


## docusignAccessCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://account.docusign.com/oauth/auth
- **Scopes**: N/A


## Author

devcenter@docusign.com

