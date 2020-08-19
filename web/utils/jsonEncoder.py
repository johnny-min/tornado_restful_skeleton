# encoding: utf-8
'''
@author: cm
@file: jsonEncoder.py
@time: 2020/8/19 17:36
@desc:
'''
import json
import decimal

from datetime import date, datetime


class JsonEncoder(json.JSONEncoder):  # JSON序列化器
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        else:
            super(JsonEncoder, self).default(obj)
