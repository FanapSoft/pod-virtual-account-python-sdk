# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from pod_virtual_account import PodVirtualAccount
from examples.config import *

try:
    pod_virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)

    print(pod_virtual_account.get_link_issue_withdraw_rule_by_plan(business_id=BUSINESS_ID, plan_id=1141,
                                                                      redirect_uri="https://karthing.ir",
                                                                      call_uri="https://karthing.ir/test.php"))

    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/issueWithdrawRuleByPlan/?businessId=7867&planId=1141&redirectUri=https%3A%2F%2Fkarthing.ir&callUri=https%3A%2F%2Fkarthing.ir%2Ftest.php

    print(pod_virtual_account.get_link_issue_withdraw_rule_by_plan(business_id=BUSINESS_ID))
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/issueWithdrawRuleByPlan/?businessId=7867

    print(pod_virtual_account.get_link_issue_withdraw_rule_by_plan(business_id=BUSINESS_ID, plan_id=1141,
                                                                      redirect_uri="https://karthing.ir"))
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/issueWithdrawRuleByPlan/?planId=1141&redirectUri=https%3A%2F%2Fkarthing.ir&businessId=7867

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
