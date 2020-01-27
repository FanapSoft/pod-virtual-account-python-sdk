# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from examples.config import *
from pod_virtual_account import PodVirtualAccount

try:
    pod_virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)

    access_token = API_TOKEN
    # access_token = USER_ACCESS_TOKEN   # شما می توانید به جای توکن کسب و کار access token کاربر را نیز ارسال کنید

    result = pod_virtual_account.withdraw_rule_plan_list(business_id=BUSINESS_ID, access_token=access_token, page=1,
                                                         size=50)

    print(result)
    print("Total :", pod_virtual_account.total_items())
    # OUTPUT
    # [
    #   {
    #     "id": 1141,
    #     "creationDate": 1564342200000,
    #     "maxAmount": 800000,
    #     "maxCount": 10,
    #     "typeCode": "WITHDRAW_RULE_TYPE_SUBSCRIPTION_AMOUNT",
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
    #     "subscriptionDaysAmount": 90
    #   }
    #   , ...
    # ]

    # Total : 6

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
