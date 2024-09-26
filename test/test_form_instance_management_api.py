from __future__ import absolute_import, print_function

import unittest

import docusign_webforms as docusign
from docusign_webforms import ApiException, FormManagementApi, FormInstanceManagementApi
from docusign_webforms.models import WebFormValues, CreateInstanceRequestBody
from docusign_webforms.models.authentication_method import AuthenticationMethod
from test.test_helper import TestHelper


class FormInstanceManagementAPIUnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._testConfig = TestHelper()
        cls._api_client = cls._testConfig.get_authenticated_api_client()

        cls._form_management_api = FormManagementApi(cls._api_client)
        cls._form_instance_management_api = FormInstanceManagementApi(cls._api_client)
        cls._published_form_id = None
        cls._web_form_instance = None
        cls._web_form_instance_id = None
        cls._fill_dependencies()

    @classmethod
    def _fill_dependencies(cls):

        try:
            if cls._testConfig.published_webform_id is None:
                webforms_list_data = cls._form_management_api.list_forms(cls._testConfig.account_id, is_published=True)
                published_web_forms = [x for x in webforms_list_data.items if x.is_published]
                if published_web_forms:
                    cls._published_form_id = published_web_forms[0].id
            else:
                cls._published_form_id = cls._testConfig.published_webform_id

            # Get Instance ID
            cls._web_form_instance = cls._create_webform_instance()
            cls._web_form_instance_id = cls._web_form_instance.id
        except ApiException as e:
            print("\nApiException when setting up Dependencies Info: %s" % e)
            raise Exception("An unexpected error occurred. Test case should not fail here.")
        except Exception as e:
            print("\nException when setting up Dependencies Info: %s" % e)
            raise Exception("An unexpected error occurred. Test case should not fail here.")

    @classmethod
    def _get_webform_instance_create_request_body(cls):
        values = ({
            "Signer_name": "SDK Python Client - " + docusign.configuration.user_agent,
            "Signer_email": "customer@domain.com",
            "T1": "Customer"
        })

        requestBody = CreateInstanceRequestBody(
            form_values=values,
            client_user_id="customer_id@domain.com",
            authentication_instant="02/02/2023",
            authentication_method=AuthenticationMethod.BIOMETRIC,
            assertion_id="client-1",
            security_domain="domain.com",
            return_url="http://www.google.com",
            expiration_offset=120,
            tags=["loan_application", "finance_dept"]
        )

        return requestBody

    @classmethod
    def _create_webform_instance(cls):
        try:
            accountId = cls._testConfig.account_id
            formId = cls._published_form_id
            requestBody = cls._get_webform_instance_create_request_body()

            webFormInstance = cls._form_instance_management_api.create_instance(accountId, formId, requestBody)
            return webFormInstance
        except ApiException as e:
            print("\nApiException: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException: %s" % e)
            assert e is None  # make the test case fail in case of an exception

    def tearDown(self):
        self._api_client.rest_client.pool_manager.clear()

    @TestHelper.handle_exceptions
    def test_list_instances_with_http_info_withValidParams_shouldReturnFormInstances(self):
        account_id = self._testConfig.account_id
        form_id = self._published_form_id

        api_response = self._form_instance_management_api.list_instances_with_http_info(account_id, form_id)

        self.assertIsNotNone(api_response[0], "The webFormInstances should not be null.")
        self.assertTrue(len(api_response[0].items) > 0, "The list of instances should not be empty.")

    @TestHelper.handle_exceptions
    def test_get_form_instance_with_http_info_withValidParams_shouldReturnFormInstance(self):
        account_id = self._testConfig.account_id
        form_id = self._published_form_id
        instance_id = self._web_form_instance_id

        api_response = self._form_instance_management_api.get_instance_with_http_info(account_id, form_id, instance_id)

        self.assertIsNotNone(api_response[0], "The webFormInstance should not be null.")
        self.assertEqual(form_id, api_response[0].form_id, "WebformId in request and response should match")
        self.assertEqual(account_id, api_response[0].account_id, "AccountId in request and response should match")
        self.assertEqual(instance_id, api_response[0].id, "InstanceId in request and response should match")

    @TestHelper.handle_exceptions
    def test_get_form_instance_with_http_info_withInvalidAccountId_shouldReturnApiException(self):
        account_id = self._testConfig.user_id
        form_id = self._published_form_id
        instance_id = self._web_form_instance_id

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.get_instance_with_http_info(account_id, form_id, instance_id)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_get_form_instance_with_http_info_withInvalidFormId_shouldReturnApiException(self):
        account_id = self._testConfig.account_id
        form_id = self._testConfig.user_id
        instance_id = self._web_form_instance_id

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.get_instance_with_http_info(account_id, form_id, instance_id)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_get_form_instance_with_http_info_withInvalidInstanceId_shouldReturnApiException(self):
        account_id = self._testConfig.account_id
        form_id = self._published_form_id
        instance_id = self._testConfig.user_id

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.get_instance_with_http_info(account_id, form_id, instance_id)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_create_instance_with_http_info_withValidParams_shouldReturnCreatedFormInstance(self):
        accountId = self._testConfig.account_id
        formId = self._published_form_id
        requestBody = self._get_webform_instance_create_request_body()

        apiResponse = self._form_instance_management_api.create_instance_with_http_info(accountId, formId, requestBody)

        self.assertIsNotNone(apiResponse[0])
        self.assertEqual(requestBody.client_user_id, apiResponse[0].client_user_id, "ClientUserId in request and response should match")
        self.assertEqual(len(requestBody.tags), len(apiResponse[0].tags), "Tags length in request and response should match")

    @TestHelper.handle_exceptions
    def test_create_instance_with_http_info_withInvalidFormId_shouldReturnApiException(self):
        accountId = self._testConfig.account_id
        formId = self._testConfig.user_id
        requestBody = self._get_webform_instance_create_request_body()

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.create_instance_with_http_info(accountId, formId, requestBody)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_create_instance_with_http_info_withInvalidAccountId_shouldReturnApiException(self):
        accountId = self._testConfig.user_id
        formId = self._published_form_id
        requestBody = self._get_webform_instance_create_request_body()

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.create_instance_with_http_info(accountId, formId, requestBody)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_create_instance_with_http_info_withInvalidRequestObject_shouldReturnApiException(self):
        accountId = self._testConfig.account_id
        formId = self._published_form_id

        requestBody = CreateInstanceRequestBody()

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.create_instance_with_http_info(accountId, formId, requestBody)
        self.assertEqual(400, context.exception.status)

    @TestHelper.handle_exceptions
    def test_refresh_token_with_http_info_withValidRequestParams_shouldReturnWebFormInstanceWithNewToken(self):
        accountId = self._testConfig.account_id
        formId = self._published_form_id
        existingWebFormInstance = self._web_form_instance
        instanceId = self._web_form_instance_id

        apiResponse = self._form_instance_management_api.refresh_token_with_http_info(accountId, formId, instanceId)

        self.assertIsNotNone(apiResponse[0].instance_token, "InstanceToken in response should not be None")
        self.assertNotEqual(existingWebFormInstance.instance_token, apiResponse[0].instance_token, "InstanceToken in request and response should not match")

    @TestHelper.handle_exceptions
    def test_refresh_token_with_http_info_withInvalidAccountId_shouldReturnApiException(self):
        accountId = self._testConfig.user_id
        formId = self._published_form_id
        instanceId = self._web_form_instance_id

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.refresh_token_with_http_info(accountId, formId, instanceId)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_refresh_token_with_http_info_withInvalidFormId_shouldReturnApiException(self):
        accountId = self._testConfig.account_id
        formId = self._testConfig.user_id
        instanceId = self._web_form_instance_id

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.refresh_token_with_http_info(accountId, formId, instanceId)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_refresh_token_with_http_info_withInvalidInstanceIdAsNull_shouldReturnApiException(self):
        accountId = self._testConfig.account_id
        formId = self._published_form_id
        instanceId = self._testConfig.user_id

        with self.assertRaises(ApiException) as context:
            self._form_instance_management_api.refresh_token_with_http_info(accountId, formId, instanceId)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

        
if __name__ == '__main__':
    unittest.main()
