from __future__ import absolute_import, print_function

import unittest

from docusign_webforms import ApiException, FormManagementApi, FormInstanceManagementApi
from test.test_helper import TestHelper


class FormManagementApiTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._testConfig = TestHelper()
        cls._api_client = cls._testConfig.get_authenticated_api_client()

        cls._form_management_api = FormManagementApi(cls._api_client)
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

        except ApiException as e:
            print("\nApiException when setting up Dependencies Info: %s" % e)
            raise Exception("An unexpected error occurred. Test case should not fail here.")
        except Exception as e:
            print("\nException when setting up Dependencies Info: %s" % e)
            raise Exception("An unexpected error occurred. Test case should not fail here.")

    def tearDown(self):
        self._api_client.rest_client.pool_manager.clear()

    @TestHelper.handle_exceptions
    def test_list_forms_with_http_info_withValidAccountId_shouldReturnForms(self):
        account_id = self._testConfig.account_id

        api_response = self._form_management_api.list_forms_with_http_info(account_id)

        self.assertIsNotNone(api_response[0], "The list of forms should not be null.")
        self.assertIsNotNone(api_response[0].items, "The list of forms should not be null.")
        self.assertTrue(len(api_response[0].items) > 0, "The list of forms should not be empty.")

    @TestHelper.handle_exceptions
    def test_list_forms_with_http_info_withInvalidAccountId_shouldReturnApiException(self):
        account_id = self._testConfig.user_id

        with self.assertRaises(ApiException) as context:
            self._form_management_api.list_forms_with_http_info(account_id)
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_get_form_with_http_info_WithValidParams_shouldReturnForm(self):
        account_id = self._testConfig.account_id
        form_id = self._published_form_id

        api_response = self._form_management_api.get_form_with_http_info(account_id, form_id, state="active")

        self.assertIsNotNone(api_response[0], "Form Object cannot be null")
        self.assertEqual(form_id, api_response[0].id, "WebformId in request and response should match")

    @TestHelper.handle_exceptions
    def test_get_form_with_http_info_withInvalidFormId_shouldReturnApiException(self):
        account_id = self._testConfig.account_id
        form_id = self._testConfig.account_id

        with self.assertRaises(ApiException) as context:
            self._form_management_api.get_form_with_http_info(account_id, form_id, state="active")
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

    @TestHelper.handle_exceptions
    def test_get_form_with_http_info_withInvalidAccountId_shouldReturnApiException(self):
        account_id = self._testConfig.user_id
        form_id = self._published_form_id

        with self.assertRaises(ApiException) as context:
            self._form_management_api.get_form_with_http_info(account_id, form_id, state="active")
        self.assertEqual(context.exception.status, 404, "Expected ApiException status code to be 404, indicating that the resource was not found.")

        
if __name__ == '__main__':
    unittest.main()        
