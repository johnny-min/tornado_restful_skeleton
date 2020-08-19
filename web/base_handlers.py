# encoding: utf-8
'''
@author: cm
@file: base_handlers.py
@time: 2020/8/19 17:35
@desc:
'''
import logging

import json

from tornado.web import RequestHandler

from web.utils.jsonEncoder import JsonEncoder


class BaseHandler(RequestHandler):
    """
       控制器基类
       """

    def prepare(self):  # 请求之前记录log
        logging.info(self.request)

    # 解决跨域问题
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Access-Control-Max-Age", 1000)
        self.set_header("Content-type", "application/json")

    # vue一般需要访问options方法， 如果报错则很难继续，所以只要通过就行了，当然需要其他逻辑就自己控制。
    def options(self):
        # 返回方法1
        self.set_status(204)
        self.finish()
        # 返回方法2
        self.write('{"errorCode":"00","errorMessage","success"}')

    def get_current_user(self):  # 当前用户
        return self.get_secure_cookie('auth-user').decode('utf-8') if self.get_secure_cookie('auth-user') else ''

    def render(self, template_name, err='', message='', data=None, **kwargs):  # 重写渲染方法
        data = data if isinstance(data, dict) else {}
        data.update({'username': self.current_user})
        err = err or self.get_argument('e', '')
        message = message or self.get_argument('m', '')
        data.update({'err': err})
        data.update({'message': message})
        super(BaseHandler, self).render(template_name, **data)

    def json_response(self, status, message, data=None):  # 重写渲染json方法
        data = data if isinstance(data, dict) else {}
        json_response = {
            'status': status,
            'message': message,
            'data': data
        }
        print(json_response)
        self.write(json.dumps(json_response, cls=JsonEncoder))

