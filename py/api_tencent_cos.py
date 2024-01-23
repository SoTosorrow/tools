from qcloud_cos.cos_exception import CosClientError, CosServiceError

import api_tencent_util as util
from config import tencent_cos_config

client = util.getCosClient()

# @checked
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
    
# with open("../tmp", "rb") as f:
#     a = f.read()
# r = putObject("tmp.txt", a)
# @checked
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

# TODO multiPut
# TODO multiDownload
# TODO multiDelete

# uploadObjectLocal("test_upload.txt","../tmp")    
# @checked
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
    # { Content-Length:0, Connection..., ETag, ...}
    return res

# downloadObject("2024-01-23-14-33-02tmp.txt","test.tt","")
# @checked
def downloadObject(
        file_name, 
        download_name, 
        prefix=tencent_cos_config["prefix"]):
    path = prefix + file_name
    res = client.download_file(
        Bucket=tencent_cos_config["bucket"],
        Key=path,
        DestFilePath=download_name
    )
    # TODO Seemd return None
    return res

# TODO consider other handle for object stream
# r = getObjectBytes("2024-01-23-14-57-27-test_upload.txt")
# print(r.decode("utf-8"))
def getObjectBytes(file_name, prefix=tencent_cos_config["prefix"]):
    path = prefix + file_name
    res = client.get_object(
        Bucket=tencent_cos_config["bucket"],
        Key=path
    )
    if 'Body' in res:
        bytes = res['Body'].get_raw_stream().data
        return bytes 
    else:
        return None


# @checked
def deleteObject(
        file_name, 
        prefix=tencent_cos_config["prefix"]):
    path = prefix + file_name
    res = client.delete_object(
        Bucket=tencent_cos_config["bucket"],
        Key=path
    )
    # return {Connection, Date, Server, x-cos-request-id}
    return res


if __name__ == '__main__':
    # print(a)
    pass
