"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.transactions_api import TransactionsApi  # noqa: E501


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_transactions_report(self):
        """Test case for generate_transactions_report

        Generate Transactions Report  # noqa: E501
        """
        pass

    def test_get_all_customer_transactions(self):
        """Test case for get_all_customer_transactions

        Get All Customer Transactions  # noqa: E501
        """
        pass

    def test_get_customer_account_transactions(self):
        """Test case for get_customer_account_transactions

        Get Customer Account Transactions  # noqa: E501
        """
        pass

    def test_get_customer_transaction(self):
        """Test case for get_customer_transaction

        Get Customer Transaction by ID  # noqa: E501
        """
        pass

    def test_load_historic_transactions_for_customer_account(self):
        """Test case for load_historic_transactions_for_customer_account

        Load Historic Transactions for Customer Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
