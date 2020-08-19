# encoding: utf-8
'''
@author: cm
@file: __init__.py
@time: 2020/8/19 17:28
@desc:
'''
from web.file.handles import FileHandler

ROUTER = [
    (r'/file', FileHandler),
]