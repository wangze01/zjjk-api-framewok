"""
# -*- coding: utf-8 -*-
# @Time    : 2021-04-12 17:21:41
# @Author  : Tibbers
# @File    :


#执行user功能sheet页面的测试用例
"""

import pytest
import os
import sys
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log
from Common.plugs.get_db import MysqlConnect


BASE_DIR = os.path.dirname((os.path.dirname(__file__)))

if sys.platform == "win32":
    conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
else:
    conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini')

log_path = r_config(conf_path, "log", "log_path")
database_info = r_config(conf_path, 'DB', 'database')


logger = Log(log_path)

mc = MysqlConnect(eval(database_info)['host'],
                  eval(database_info)['port'],
                  eval(database_info)['user'],
                  eval(database_info)['password'],
                  eval(database_info)['db'])

headers = { 'Content-Type': 'application/json;charset=UTF-8',
            'App-code':'ZJ-PUB-D-AN',
            }


@pytest.fixture(scope='session')
def project_module_start():
    logger.info("==========开始 XX模块 执行测试===========")
    yield (headers, mc)
    mc.close_db()
    logger.info("==========结束 XX模块 测试===========")


def pytest_configure(config):
    # 标签名集合
    marker_list = ['p1', 'p2', 'p3', 'p11']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)

