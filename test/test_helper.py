import os
import base64
import unittest
import functools

import docusign_webforms as docusign
from docusign_webforms import ApiException


class TestHelper(object):
    def __init__(self):

        self.user_name = None
        self.user_id = None

        self.client_secret = None
        self.integrator_key = None
        self.private_key_bytes = None
        self.expires_in = 3600
        self.scopes = None

        self.user_info = None
        self.account_id = None

        self.published_webform_id = None

        self.initialize_config()

    def initialize_config(self, user_name=None, client_secret =None, user_id=None, integrator_key=None):
        self.user_name = user_name if user_name else os.environ.get("USER_NAME")
        self.client_secret = client_secret if client_secret else os.environ.get("CLIENT_SECRET")

        self.integrator_key = integrator_key if integrator_key else os.environ.get("INTEGRATOR_KEY_JWT")
        self.user_id = user_id if user_id else os.environ.get("USER_ID")

        self.private_key_bytes = base64.b64decode(os.environ.get("PRIVATE_KEY"))
        self.expires_in = 3600
        self.scopes = ["signature", 'webforms_read', 'webforms_write', 'webforms_instance_read', 'webforms_instance_write']

        # Note: This value is being hardcoded so that the form values can be sent accordingly in the test.
        self.published_webform_id = 'ae0dbfc4-67c9-4dd2-863b-2823cadde398'

    def get_api_client(self):
        api_client = docusign.ApiClient()
        docusign.configuration.api_client = api_client
        return api_client

    def get_authenticated_api_client(self):
        try:
            api_client = self.get_api_client()
            token = (api_client.request_jwt_user_token(client_id=self.integrator_key,
                                                            user_id=self.user_id,
                                                            oauth_host_name=api_client.oauth_host_name,
                                                            private_key_bytes=self.private_key_bytes,
                                                            expires_in=3600,
                                                            scopes=self.scopes))

            self.user_info = api_client.get_user_info(token.access_token)
            if self.user_info.accounts and len(self.user_info.accounts) > 0:
                self.account_id = self.user_info.accounts[0].account_id

        except ApiException as e:
            print("\nApiException when setting up DocuSign Api Client: %s" % e)
            raise Exception("An unexpected error occurred. Test case should not fail here.")
        except Exception as e:
            print("\nException when calling DocuSign Api Client: %s" % e)
            raise Exception("An unexpected error occurred. Test case should not fail here.")

        return api_client

    @staticmethod
    def handle_exceptions(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ApiException as e:
                print("An ApiException occurred:", e)
                unittest.TestCase().fail("An unexpected error occurred. Test case should not fail here.")
            except Exception as e:
                print("An Exception occurred:", e)
                unittest.TestCase().fail("An unexpected error occurred. Test case should not fail here.")
        return wrapper
