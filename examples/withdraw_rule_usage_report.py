# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from pod_virtual_account import PodVirtualAccount
from examples.config import *

try:
    pod_virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)
    result = pod_virtual_account.withdraw_rule_usage_report(rule_id=2715, access_token=ACCESS_TOKEN)
    print(result)

    # OUTPUT
    #  {
    #   "rule": {
    #     "id": 2715,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 395,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000000"
    #     },
    #     "creationDate": 1580046933722,
    #     "startDate": 1580046933722,
    #     "expireDate": 1587822933722,
    #     "maxAmount": 800000,
    #     "maxCount": 10,
    #     "typeCode": "WITHDRAW_RULE_TYPE_SUBSCRIPTION_AMOUNT",
    #     "usageCount": 0,
    #     "usageAmount": 0,
    #     "wallet": "PODLAND_WALLET",
    #     "expired": False
    #   },
    #   "validUntil": 1587822933722,
    #   "remainingAmount": 800000,
    #   "remainingCount": 10
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
