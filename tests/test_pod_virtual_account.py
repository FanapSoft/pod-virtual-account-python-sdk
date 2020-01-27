# coding=utf-8
from __future__ import unicode_literals

import unittest

try:
    from urlparse import urlparse
    from urlparse import parse_qs
except ImportError:
    from urllib.parse import urlparse
    from urllib.parse import parse_qs

from pod_base import InvalidDataException, APIException

from pod_virtual_account import PodVirtualAccount, WithdrawRuleType
from tests.config import *


class TestPodVirtualAccount(unittest.TestCase):
    __slots__ = "__virtual_account"

    def setUp(self):
        self.__virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_add_withdraw_rule_plan(self):
        result = self.__virtual_account.add_withdraw_rule_plan(subscription_days=2, max_amount=1000, max_count=5,
                                                               type_code=WithdrawRuleType.SUBSCRIPTION_AMOUNT)

        self.assertIsInstance(result, dict, msg="add withdraw rule plan : check instance")
        self.assertEqual(result["subscriptionDaysAmount"], 2, msg="add withdraw rule plan : check subscription days")
        self.assertEqual(result["maxAmount"], 1000, msg="add withdraw rule plan : check max amount")
        self.assertEqual(result["maxCount"], 5, msg="add withdraw rule plan : check max count")
        self.assertEqual(result["typeCode"], WithdrawRuleType.SUBSCRIPTION_AMOUNT,
                         msg="add withdraw rule plan : check type code")

    def test_01_add_withdraw_rule_plan_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="add withdraw rule plan : validation error"):
            self.__virtual_account.add_withdraw_rule_plan(subscription_days="2", max_amount="1000", max_count="5",
                                                          type_code="ABCD")

    def test_01_add_withdraw_rule_plan_required_params(self):
        with self.assertRaises(TypeError, msg="add withdraw rule plan : required param"):
            self.__virtual_account.add_withdraw_rule_plan()

    def test_02_withdraw_rule_plan_list(self):
        result = self.__virtual_account.withdraw_rule_plan_list(business_id=BUSINESS_ID)

        self.assertIsInstance(result, list, msg="withdraw rule plan list : check instance")

    def test_02_withdraw_rule_plan_list_all_params(self):
        result = self.__virtual_account.withdraw_rule_plan_list(business_id=BUSINESS_ID)

        self.assertIsInstance(result, list, msg="withdraw rule plan list (all params): check instance")

    def test_02_withdraw_rule_plan_list_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="withdraw rule plan list : validation error"):
            self.__virtual_account.withdraw_rule_plan_list(business_id=str(BUSINESS_ID))

    def test_02_withdraw_rule_plan_list_required_param(self):
        with self.assertRaises(TypeError, msg="withdraw rule plan list : required param"):
            self.__virtual_account.withdraw_rule_plan_list()

    def test_03_get_link_issue_withdraw_rule_by_plan(self):
        link = self.__virtual_account.get_link_issue_withdraw_rule_by_plan(business_id=BUSINESS_ID)
        parsed = urlparse(link)
        parsed_qs = parse_qs(parsed.query)

        self.assertIsInstance(link, str, msg="get link issue : check instance")
        self.assertEqual(parsed_qs["businessId"][0], str(BUSINESS_ID), msg="get link issue : business id")

    def test_03_get_link_issue_withdraw_rule_by_plan_all_params(self):
        call_uri = "http://google.com"
        redirect_url = "http://yahoo.com"
        plan_id = 123
        link = self.__virtual_account.get_link_issue_withdraw_rule_by_plan(business_id=BUSINESS_ID, call_uri=call_uri,
                                                                           redirect_uri=redirect_url, plan_id=plan_id)
        parsed = urlparse(link)
        parsed_qs = parse_qs(parsed.query)

        self.assertIsInstance(link, str, msg="get link issue : check instance")
        self.assertEqual(parsed_qs["businessId"][0], str(BUSINESS_ID), msg="get link issue : business id")
        self.assertEqual(parsed_qs["planId"][0], str(plan_id), msg="get link issue : plan id")
        self.assertEqual(parsed_qs["callUri"][0], call_uri, msg="get link issue : call uri")
        self.assertEqual(parsed_qs["redirectUri"][0], redirect_url, msg="get link issue : redirect uri")

    def test_03_get_link_issue_withdraw_rule_by_plan_validation_error(self):
        call_uri = "ABCD"
        redirect_url = "DEFH"
        plan_id = "123"
        with self.assertRaises(InvalidDataException, msg="get link issue : validation error"):
            self.__virtual_account.get_link_issue_withdraw_rule_by_plan(business_id=BUSINESS_ID, call_uri=call_uri,
                                                                        redirect_uri=redirect_url, plan_id=plan_id)

    def test_03_get_link_issue_withdraw_rule_by_plan_required_param(self):
        with self.assertRaises(TypeError, msg="get link issue : required param"):
            self.__virtual_account.get_link_issue_withdraw_rule_by_plan()

    def test_04_granted_withdraw_rule_list(self):
        result = self.__virtual_account.granted_withdraw_rule_list()
        self.assertIsInstance(result, list, msg="granted withdraw rule list : check instance")

    def test_04_granted_withdraw_rule_list_all_params(self):
        params = {
            "userId": USER_ID,
            "typeCode": WithdrawRuleType.SUBSCRIPTION_AMOUNT
        }
        result = self.__virtual_account.granted_withdraw_rule_list(page=1, size=50, **params)
        self.assertIsInstance(result, list, msg="granted withdraw rule list (all params) : check instance")

    def test_04_granted_withdraw_rule_list_validation_error(self):
        params = {
            "userId": "123456",
            "typeCode": "ABCD"
        }
        with self.assertRaises(InvalidDataException, msg="granted withdraw rule list : validation error"):
            self.__virtual_account.granted_withdraw_rule_list(page=1, size=50, **params)

    def test_05_revoke_withdraw_rule_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="withdraw rule list : validation error"):
            self.__virtual_account.revoke_withdraw_rule(rule_id="123456")

    def test_05_revoke_withdraw_rule_required_param(self):
        with self.assertRaises(TypeError, msg="withdraw rule list : required param"):
            self.__virtual_account.revoke_withdraw_rule()

    def test_05_revoke_withdraw_rule_invalid_rule_id(self):
        with self.assertRaises(APIException, msg="withdraw rule list : invalid rule id"):
            self.__virtual_account.revoke_withdraw_rule(rule_id=1)

    def test_06_withdraw_rule_usage_report_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="withdraw rule usage report : validation error"):
            self.__virtual_account.withdraw_rule_usage_report(rule_id="123456", access_token=123456)

    def test_06_withdraw_rule_usage_report_required_param(self):
        with self.assertRaises(TypeError, msg="withdraw rule usage report : required param"):
            self.__virtual_account.withdraw_rule_usage_report()

    def test_06_withdraw_rule_usage_report_invalid_rule_id(self):
        with self.assertRaises(APIException, msg="withdraw rule usage report : invalid rule id"):
            self.__virtual_account.withdraw_rule_usage_report(rule_id=1, access_token=ACCESS_TOKEN)
