"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.app_registration_api import AppRegistrationApi  # noqa: E501


class TestAppRegistrationApi(unittest.TestCase):
    """AppRegistrationApi unit test stubs"""

    def setUp(self):
        self.api = AppRegistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_app_registration_status(self):
        """Test case for get_app_registration_status

        Get App Registration Status  # noqa: E501
        """
        pass

    def test_migrate_institution_login_accounts(self):
        """Test case for migrate_institution_login_accounts

        Migrate Institution Login Accounts  # noqa: E501
        """
        pass

    def test_modify_app_registration(self):
        """Test case for modify_app_registration

        Modify App Registration  # noqa: E501
        """
        pass

    def test_register_app(self):
        """Test case for register_app

        Register App  # noqa: E501
        """
        pass

    def test_set_customer_app_id(self):
        """Test case for set_customer_app_id

        Set Customer App ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
