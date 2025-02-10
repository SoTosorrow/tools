from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

import json
import time

import api_tencent_util as util
# https://github.com/TencentCloud/tencentcloud-sdk-python/blob/master/tencentcloud/asr/v20190614/asr_client.py

def createAsrBaseInfo(data_src, data_type="16k_zh", api_type=""):
    data_format = data_src.split(".")[-1]
    if(data_src.startswith("http")):    # 使用url音频
        params_data = { "SourceType": 0, "Url": data_src }
    else:   # 使用本地音频，即SourceType 为1 时， 需要设置Data，将音频数据base64编码（最大5MB）
        with open(data_src, "rb") as f:
            data = f.read()
        data = util.bytes2Base64(data)
        params_data = { "SourceType": 1, "Data": data }
    
    params = {
        "EngSerViceType": data_type,  # 一句话识别需要
        "VoiceFormat": data_format,   # 一句话识别需要
        "ChannelNum": 1,              # CreateRecTask录音文件识别需要,识别声道数 1单声道，2双声道
        "EngineModelType": data_type, # CreateRecTask录音文件识别需要
        "ResTextFormat": 1,           # CreateRecTask录音文件识别需要 识别结果返回样式
    }
    params.update(params_data)
    return json.dumps(params)


# 5000/month max-60s/3MB 一句话识别
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
    try:
        cred = util.getCredential()
        # client of request target service
        client = asr_client.AsrClient(cred, "")

        asr_params_json_string = createAsrBaseInfo(data_src, data_type)
        req = models.SentenceRecognitionRequest()
        req.from_json_string(asr_params_json_string)
        resp = client.SentenceRecognition(req)
        
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)

def invokeASR(data_src, data_type="16k_zh"):
    try:
        cred = util.getCredential()
        # client of request target service
        client = asr_client.AsrClient(cred, "")

        asr_params_json_string = createAsrBaseInfo(data_src, data_type)
        req = models.CreateRecTaskRequest()
        req.from_json_string(asr_params_json_string)
        resp = client.CreateRecTask(req)    # 返回 {"TaskId": 11529095690}
        
        # 轮询识别结果查询
        taskid = resp.Data.TaskId
        print("任务id", taskid)
        req = models.DescribeTaskStatusRequest()
        params = { "TaskId": taskid }
        req.from_json_string(json.dumps(params))
        result = ""
        while True:
            resp = client.DescribeTaskStatus(req)
            resp_json = resp.to_json_string()
            resp_obj = json.loads(resp_json)
            if resp_obj["Data"]["StatusStr"] == "success":
                result = resp_obj["Data"]["ResultDetail"]
                break
            if resp_obj["Data"]["Status"] == 3:
                return False, ""
            time.sleep(1)
        return result

    except TencentCloudSDKException as err:
        print(err)

if __name__ == '__main__':
    t1 = time.time()
    r1 = invokeASR("./test.m4a")
    # print(r1, time.time() - t1)
    print(r1[0]["FinalSentence"], time.time() - t1)
    # pass