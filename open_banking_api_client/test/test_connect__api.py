"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.connect__api import ConnectApi  # noqa: E501


class TestConnectApi(unittest.TestCase):
    """ConnectApi unit test stubs"""

    def setUp(self):
        self.api = ConnectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_connect_url(self):
        """Test case for generate_connect_url

        Generate Connect URL  # noqa: E501
        """
        pass

    def test_generate_fix_connect_url(self):
        """Test case for generate_fix_connect_url

        Generate Fix Connect URL  # noqa: E501
        """
        pass

    def test_generate_joint_borrower_connect_url(self):
        """Test case for generate_joint_borrower_connect_url

        Generate Connect URL - Joint Borrower  # noqa: E501
        """
        pass

    def test_generate_lite_connect_url(self):
        """Test case for generate_lite_connect_url

        Generate Lite Connect URL  # noqa: E501
        """
        pass

    def test_send_connect_email(self):
        """Test case for send_connect_email

        Send Connect Email  # noqa: E501
        """
        pass

    def test_send_joint_borrower_connect_email(self):
        """Test case for send_joint_borrower_connect_email

        Send Connect Email - Joint Borrower  # noqa: E501
        """
        pass

    def test_verify_micro_entry_microdeposit(self):
        """Test case for verify_micro_entry_microdeposit

        Account Validation Assistant User verification of microdeposits  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
