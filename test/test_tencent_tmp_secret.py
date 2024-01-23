from config import tencent_acc_config as config

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sts.v20180813 import sts_client, models

import json
# https://cloud.tencent.com/document/product/1278/85305
try:
    cred = credential.Credential(
        config["secret_id"], config["secret_key"]
    )
    client = sts_client.StsClient(cred, "ap-nanjing")
    req = models.GetFederationTokenRequest()
    params = {
        "Name":"tmp_secret",
        "Policy":{
            "version":"2.0",
            "statement":[
            ]
        }
    }
    req.from_json_string(json.dumps(params))
    resp = client.GetFederationToken(req)
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)