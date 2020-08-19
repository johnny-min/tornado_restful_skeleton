# encoding: utf-8
'''
@author: cm
@file: router.py
@time: 2020/8/19 17:06
@desc: 路由配置
'''
import importlib

from config import config

# index
ROUTERS = []
for _ in config.registered_app:
    # 动态导入importlib.import_module
    module = importlib.import_module(_)
    ROUTERS += module.ROUTER
