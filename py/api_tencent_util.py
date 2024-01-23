from tencentcloud.common import credential
from qcloud_cos import CosConfig, CosS3Client

import base64
import time
from config import tencent_acc_config as config

def bytes2Base64(data):
    return base64.b64encode(data).decode("utf-8")

def getCredential():
    cred = credential.Credential(
        config["secret_id"], config["secret_key"]
    )
    return cred

def getCosClient():
    cos_config = CosConfig(
        Region=config["region"], 
        SecretId=config["secret_id"], 
        SecretKey=config["secret_key"],
        Token=None,     # tmp secret need
        Scheme='https'  # http or https, default https
    )
    return CosS3Client(cos_config)

def makeDateStr():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

def makeFilePath(prefix, file_name):
    return prefix + makeDateStr() + "-" + file_name

def getTmpSecret():
    pass