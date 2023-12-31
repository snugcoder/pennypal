"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.tx_push_api import TxPushApi  # noqa: E501


class TestTxPushApi(unittest.TestCase):
    """TxPushApi unit test stubs"""

    def setUp(self):
        self.api = TxPushApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tx_push_test_transaction(self):
        """Test case for create_tx_push_test_transaction

        Create TxPush Test Transaction  # noqa: E501
        """
        pass

    def test_delete_tx_push_subscription(self):
        """Test case for delete_tx_push_subscription

        Delete TxPush Subscription  # noqa: E501
        """
        pass

    def test_disable_tx_push_notifications(self):
        """Test case for disable_tx_push_notifications

        Disable TxPush Notifications  # noqa: E501
        """
        pass

    def test_subscribe_to_tx_push_notifications(self):
        """Test case for subscribe_to_tx_push_notifications

        Subscribe to TxPush Notifications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
