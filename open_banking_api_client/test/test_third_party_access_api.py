"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.third_party_access_api import ThirdPartyAccessApi  # noqa: E501


class TestThirdPartyAccessApi(unittest.TestCase):
    """ThirdPartyAccessApi unit test stubs"""

    def setUp(self):
        self.api = ThirdPartyAccessApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_third_party_access_key(self):
        """Test case for generate_third_party_access_key

        Generate Third Party Access Key  # noqa: E501
        """
        pass

    def test_revoke_third_party_access_key(self):
        """Test case for revoke_third_party_access_key

        Revoke Third Party Access  # noqa: E501
        """
        pass

    def test_update_third_party_access_key(self):
        """Test case for update_third_party_access_key

        Update Third Party Access  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
