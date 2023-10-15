"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.  # noqa: E501

    The version of the OpenAPI document: 1.13.7
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.base_report_ack_with_portfolio_id import BaseReportAckWithPortfolioId
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.pay_statement_report_all_of import PayStatementReportAllOf
from openapi_client.model.voie_pay_statement import VOIEPayStatement
globals()['BaseReportAckWithPortfolioId'] = BaseReportAckWithPortfolioId
globals()['ErrorMessage'] = ErrorMessage
globals()['PayStatementReportAllOf'] = PayStatementReportAllOf
globals()['VOIEPayStatement'] = VOIEPayStatement
from openapi_client.model.pay_statement_report import PayStatementReport


class TestPayStatementReport(unittest.TestCase):
    """PayStatementReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayStatementReport(self):
        """Test PayStatementReport"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PayStatementReport()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()