
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

import json
import time

import api_tencent_util as util

# 500w/month
# params:
#       SourceText: (utf-8) less than 6k
#       Source    : auto, zh, en, ja
#       Target    : ...
#       ProjectId : 0 
# https://console.cloud.tencent.com/api/explorer?Product=tmt&Version=2018-03-21&Action=TextTranslate
tmt_region = 'ap-shanghai'

def invokeTranslateText(text:str, target="en", source="auto"):
    try:
        cred = util.getCredential()
        
        client = tmt_client.TmtClient(cred, tmt_region)
        req = models.TextTranslateRequest()
        params = {
            "SourceText": text,
            "Source": source,
            "Target": target,
            "ProjectId": 0
        }
        req.from_json_string(json.dumps(params))
        resp = client.TextTranslate(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)

# @todo
# def invokeTranslateSpeech(src, target="en", source="zh"):
#     data_format = src.split(".")[-1]
#     if(data_format == "mp3"):
#         audio_format = "83886080"

#     try:
#         cred = getCredential()
        
#         client = tmt_client.TmtClient(cred, tmt_region)
#         req = models.SpeechTranslateRequest()
#         params = {
#             "Seq": 0,
#             "AudioFormat": audio_format,
#             "Source": source,
#             "Target": target,
#             "Data": "",
#         }
#         req.from_json_string(json.dumps(params))
#         resp = client.SpeechTranslate(req)
#         return resp.to_json_string()

#     except TencentCloudSDKException as err:
#         print(err)

if __name__ == '__main__':
    # t1 = time.time()
    # r1 = invokeTranslateText("温哥华的大将军刘能抵达了枫丹白露宫")
    # print(r1, time.time() - t1)
    pass