"""
# -*- coding: utf-8 -*-
# @Time    : 2021-04-12 17:21:41
# @Author  : Tibbers
# @File    :


#封装requests方法，对请求内容进行封装，支持post/get/DELETE方式
"""


import json
import os
import sys

import requests

from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

# 获取配置文件的完整路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)

if sys.platform == "win32":
    conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
else:
    conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini')

log_path = r_config(conf_path, "log", "log_path")

logger = Log(log_path)


class BaseRequest:

    # 初始化requests的请求内容进行封装
    def __init__(self, method, url, data=None, cookies=None, headers=None):
        logger.info("准备发送 {0} 请求".format(method.upper()))
        logger.info("请求头: {0}".format(headers))
        logger.info("接口地址: {0}".format(url))
        logger.info("接口类型: {0}".format(method.upper()))
        logger.info("接口数据: {0}".format(data))
        try:
            if method.upper() == 'GET':
                self.response = requests.get(url=url, params=data, cookies=cookies, headers=headers)
                logger.info("完成 GET 请求")
            elif method.upper() == 'POST':
                self.response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
                logger.info("完成 POST 请求")
            elif method.upper() == 'DELETE':
                self.response = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
                logger.info("完成 DELETE 请求")
        except Exception as e:
            logger.error("请求报错：{0}".format(str(e)))
            raise e

    # 声明一个方法,获得响应状态code
    def get_status_code(self):
        logger.info("响应结果状态码:{0}".format(self.response.json()))
        return self.response.status_code

    # 声明一个方法,获得响应状态text
    def get_text(self):
        logger.info("响应结text:{0}".format(self.response.json()))
        return self.response.text

    # 声明一个方法,获得响应状态json数据
    def get_json(self):
        logger.info("响应结果json:{0}".format(self.response.json()))
        json = self.response.json()
        return json

    # 声明一个方法,获得响应状态cookies
    def get_cookies(self):
        logger.info("响应结果cookie:{0}".format(self.response.json()))
        return self.response.cookies

    # 声明一个方法,获得响应状态headers
    def get_headers(self):
        logger.info("响应结果headers:{0}".format(self.response.json()))
        return self.response.headers


if __name__ == '__main__':
    headers = { 'Content-Type': 'application/json;charset=UTF-8',
                }
    url = 'http:////api/api/user/auth/login'
    url1 = 'http:///api/api/patient/case/getPatientHealthPortrait'
    data = { 'loginName': '',
             'pwd': '', }
    data1 = { 'archiveId': '612295079331102720' }

    data = json.dumps(data)
    data1 = json.dumps(data1)
    print(type(data))

    ret = BaseRequest('post', url=url, data=data, headers=headers)
    a = ret.get_json()
    print(a)

    headers['token'] = ret.get_json()['data']['token']
    ret1 = BaseRequest('post', url=url1, data=data1, headers=headers)
    print(ret1.get_headers())
    print(ret1.get_status_code())
    print(ret1.get_json())
    #print(headers)


    pass
