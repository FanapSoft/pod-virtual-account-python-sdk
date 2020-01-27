# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from pod_virtual_account import PodVirtualAccount, WithdrawRuleType
from examples.config import *

try:
    pod_virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)

    result = pod_virtual_account.add_withdraw_rule_plan(subscription_days=5, max_amount=1000, max_count=5,
                                                        type_code=WithdrawRuleType.AMOUNT_COUNT)

    print(result)
    # OUTPUT
    # {
    #   "id": 4076,
    #   "creationDate": 1579984200000,
    #   "maxAmount": 1000,
    #   "maxCount": 5,
    #   "typeCode": "WITHDRAW_RULE_TYPE_AMOUNT_COUNT",
    #   "business": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 395,
    #     "rate": {
    #       "rate": 8,
    #       "rateCount": 1
    #     },
    #     "sheba": "640170000000000000000000"
    #   },
    #   "subscriptionDaysAmount": 5
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
