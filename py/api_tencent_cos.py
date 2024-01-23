from qcloud_cos.cos_exception import CosClientError, CosServiceError

import api_tencent_util as util
from config import tencent_cos_config

client = util.getCosClient()

def getBucketObjects(prefix=tencent_cos_config["prefix"]):
    res = client.list_objects(
        Bucket=tencent_cos_config["bucket"],
        Prefix=prefix
    )
    if 'Contents' in res:
        # Key / LastModified / ETag / Size / Owner / StorageClass
        obj_lists = [
            {
                'key':i['Key'], 
                'LastModified':i['LastModified']
            } for i in res['Contents']]
        return obj_lists
    else:
        return None
    
def putObject(
        file_name, 
        bytes,
        prefix=tencent_cos_config["prefix"]):
    # concat path like test/2024-1-24-11-22-33-file.jpg
    path = util.makeFilePath(prefix, file_name)
    res = client.put_object(
        Bucket=tencent_cos_config["bucket"],
        Body=bytes,
        Key=path
    )
    return res

    
def uploadObjectLocal(
        file_name, 
        local_file_url, 
        prefix=tencent_cos_config["prefix"]):
    path = util.makeFilePath(prefix, file_name)
    res = client.upload_file(
        Bucket=tencent_cos_config["bucket"],
        Key=path,
        LocalFilePath=local_file_url,
        EnableMD5=False,
        progress_callback=None
    )
    return res


if __name__ == '__main__':
    # print(a)
    # with open("../tmp", "rb") as f:
    #     a = f.read()
    # r = putObject("tmp.txt", a)
    # r = uploadObjectLocal("test_upload.txt","../tmp")
    # print(r)
    pass
