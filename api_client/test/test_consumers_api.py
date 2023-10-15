"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.consumers_api import ConsumersApi  # noqa: E501


class TestConsumersApi(unittest.TestCase):
    """ConsumersApi unit test stubs"""

    def setUp(self):
        self.api = ConsumersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_consumer(self):
        """Test case for create_consumer

        Create Consumer  # noqa: E501
        """
        pass

    def test_get_consumer(self):
        """Test case for get_consumer

        Get Consumer by ID  # noqa: E501
        """
        pass

    def test_get_consumer_for_customer(self):
        """Test case for get_consumer_for_customer

        Get Consumer For Customer  # noqa: E501
        """
        pass

    def test_modify_consumer(self):
        """Test case for modify_consumer

        Modify Consumer by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()