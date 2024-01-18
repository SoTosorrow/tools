from tencentcloud.common import credential

import base64
from config import tencent_sub_config as config

def bytes2Base64(data):
    return base64.b64encode(data).decode("utf-8")

def getCredential():
    cred = credential.Credential(
        config["secret_id"], config["secret_key"]
    )
    return cred

def getTmpSecret():
    pass