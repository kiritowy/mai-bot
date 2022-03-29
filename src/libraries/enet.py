 # 列举文件
from asyncio.log import logger
import asyncio
from fileinput import filename
from sqlite3 import Timestamp
from unittest import result
import oss2
import time
from itertools import islice
 
AccessKeyId = ""
AccessKeySecret = ""
oss_url="oss-cn-guangzhou.aliyuncs.com"
BuckerName="mai2photo"
 
auth = oss2.Auth(AccessKeyId,AccessKeySecret)
bucket = oss2.Bucket(auth,oss_url,BuckerName)
folder=""

def allphoto(userid:str): 
    photolist = []
    # print(f"{userid}=============")
    #列举所有文件
    for obj in oss2.ObjectIterator(bucket, prefix=folder,):

        filen=str(obj.key)

        print('file: ' + obj.key)
        namecut = filen.split('-')
        print('=====')
        print(namecut[0])
        print(type(namecut[0]))
        print(type(userid))
        if namecut[0] == str(userid):
            print('进来了')
            orgtime = namecut[1].split('.')
            timestamp = int(orgtime[0])
            timeArray = time.localtime(timestamp)
            otherStyleTime = time.strftime("%Y%m%d%H%M%S", timeArray)
            photolist.append(otherStyleTime)
            print(photolist)
                # print(otherStyleTime)
                # print('-------')
    
    print(f"{photolist}============")
    return photolist
  




# allphoto(userid='45601466')
def downloadPhoto(userid:str,photo:str):
    print(userid)
    print(photo)
    # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录RAM控制台创建RAM账号。
    timeArray = time.strptime(str(photo), "%Y%m%d%H%M%S")
    timeStamp = int(time.mktime(timeArray))
    auth = oss2.Auth(AccessKeyId, AccessKeySecret)
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    # 填写Bucket名称，例如examplebucket。
    bucket = oss2.Bucket(auth, oss_url, BuckerName)
    photoname = f"{str(userid)}-{str(timeStamp)}.jpg"
    # 填写Object完整路径，完整路径中不包含Bucket名称，例如testfolder/exampleobject.txt。
    # 下载Object到本地文件，并保存到指定的本地路径D:\\localpath\\examplefile.txt。如果指定的本地文件存在会覆盖，不存在则新建。
    bucket.get_object_to_file(photoname, f"/home/pi/mai-bot/src/static/{photoname}")
    return photoname        