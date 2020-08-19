# encoding: utf-8
'''
@author: cm
@file: handles.py
@time: 2020/8/19 17:29
@desc:
'''
import logging
import os

from tornado import gen

from config.config import DEFAULT_UPLOAD_PATH
from web.base_handlers import BaseHandler

from werkzeug.datastructures import FileStorage


class FileHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        self.json_response(200, 'OK')

    @gen.coroutine
    def post(self):
        files = self.request.files['file']
        file_name = self.get_argument('file_name')
        # file = args['file']
        print(type(files))
        for file in files:
            with open(os.path.join(DEFAULT_UPLOAD_PATH, file_name), 'wb') as f:
                f.write(file['body'])
        self.json_response(200, 'OK')
