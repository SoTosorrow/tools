from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

import json
import time

import api_tencent_util as util

# 5000/month
# params: 
#       EngSerViceType  : 16k_zh, 16k_en
#       SourceType      : url=0 postData=1
#       VoiceFormat     : wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac、amr
# test code:
#       t1 = time.time()
#       r1 = invokeSingleASR("https://cm.xyskyz.xyz/test.mp3")
#       print(r1, time.time() - t1)
#       t2 = time.time()
#       r2 = invokeSingleASR("./test.mp3")
#       print(r2, time.time() - t2)
def invokeSingleASR(data_src, data_type="16k_zh"):
    # define file format e.g. mp3
    data_format = data_src.split(".")[-1]

    # define params body of audio
    if(data_src.startswith("http")):
        params_data = { "SourceType": 0, "Url": data_src }
    else:
        with open(data_src, "rb") as f:
            data = f.read()
        data = util.bytes2Base64(data)
        params_data = { "SourceType": 1, "Data": data }

    try:
        cred = util.getCredential()
        # client of request target service
        client = asr_client.AsrClient(cred, "")
        req = models.SentenceRecognitionRequest()
        
        params = {
            "EngSerViceType": data_type,
            "VoiceFormat": data_format, 
        }
        params.update(params_data)
        
        req.from_json_string(json.dumps(params))
        resp = client.SentenceRecognition(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)

if __name__ == '__main__':
    # t1 = time.time()
    # r1 = invokeSingleASR("./test2.mp3")
    # print(r1, time.time() - t1)
    pass