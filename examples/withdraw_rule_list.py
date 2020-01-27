# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from examples.config import *
from pod_virtual_account import PodVirtualAccount, WithdrawRuleType

try:
    pod_virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        # "userId": 12456,    # جستجو براساس یک شناسه کاربر
        "typeCode": WithdrawRuleType.SUBSCRIPTION_AMOUNT      # جستجو براساس نوع مجوز
    }

    result = pod_virtual_account.granted_withdraw_rule_list(page=1, size=50, **params)

    print(result)
    print("Total :", pod_virtual_account.total_items())
    # OUTPUT
    # [
    #   {
    #     "id": 2714,
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
    #     "creationDate": 1580041734589,
    #     "startDate": 1580041734589,
    #     "expireDate": 1587817734589,
    #     "maxAmount": 800000,
    #     "maxCount": 10,
    #     "typeCode": "WITHDRAW_RULE_TYPE_SUBSCRIPTION_AMOUNT",
    #     "usageCount": 0,
    #     "usageAmount": 0,
    #     "wallet": "PODLAND_WALLET",
    #     "expired": False,
    #     "user": {
    #       "id": 28590,
    #       "name": "سمیه بهدانی",
    #       "ssoId": "15778334",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     }
    #   },
    #   ...
    # ]

    # Total : 1

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
