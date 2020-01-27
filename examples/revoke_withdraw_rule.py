# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from pod_virtual_account import PodVirtualAccount
from examples.config import *

try:
    pod_virtual_account = PodVirtualAccount(api_token=API_TOKEN, server_type=SERVER_MODE)

    if pod_virtual_account.revoke_withdraw_rule(rule_id=2714):
        print("Revoked")

    # OUTPUT
    # Revoked

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
