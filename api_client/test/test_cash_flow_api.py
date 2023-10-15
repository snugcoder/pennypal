"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.cash_flow_api import CashFlowApi  # noqa: E501


class TestCashFlowApi(unittest.TestCase):
    """CashFlowApi unit test stubs"""

    def setUp(self):
        self.api = CashFlowApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_cash_flow_business_report(self):
        """Test case for generate_cash_flow_business_report

        Generate Cash Flow Report - Business  # noqa: E501
        """
        pass

    def test_generate_cash_flow_personal_report(self):
        """Test case for generate_cash_flow_personal_report

        Generate Cash Flow Report - Personal  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()