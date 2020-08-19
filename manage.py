# encoding: utf-8
'''
@author: cm
@file: manage.py
@time: 2020/8/19 17:01
@desc: 主入口
'''
import os
import sys
import tornado
import platform


from tornado import web, ioloop, httpserver
from web.router import *
from config.config import *


def make_app():
    print(SETTINGS)
    return tornado.web.Application(ROUTERS, **SETTINGS)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        import asyncio

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    args = sys.argv[1:]
    if args[0] == 'run':
        app = make_app()
        print('Starting server on port 5000...')
        # sockets = netutil.bind_sockets(9000, '127.0.0.1', socket.AF_UNSPEC)
        # process.fork_processes(5)
        server = httpserver.HTTPServer(app)
        server.listen(5000)  # 端口
        # server.start(num_processes=4)  # 进程数
        server.start()  # 进程数
        # server.add_sockets(sockets)
        ioloop.IOLoop.instance().start()  # 启动实例

    elif args[0] == 'dbshell':
        config = DATABASE.get('default', {})
        os.system('mysql -u{user} -p{password} -D{database} -A'.format(
            user=config.get('user', 'root'),
            password=config.get('password', ''),
            database=config.get('database', 'blog')
        ))

    elif args[0] == 'migrate':
        config = DATABASE.get('default', {})
        init_sql = 'mysql -u{user} -p{password} -D{database} -A < database/migration.sql'.format(
            user=config.get('user', 'root'),
            password=config.get('password', '184346'),
            database=config.get('database', 'blog')
        )
        print('Initializing tables to database {}...'.format(config.get('database')))
        data = os.system(init_sql)
        if data == 256:
            log.info(
                'Seems like you havent\'t create the database, try:\n \'create database tequila default character set utf8;\'')
            print(
                'Seems like you havent\'t create the database, try:\n \'create database tequila default character set utf8;\'')
        print('Completed.')

    elif args[0] == 'shell':
        a = os.system('pip3 list | grep -w"ipython " 1>/dev/null')
        if a:
            print('Installing ipython')
            os.system('pip3 install ipython')
        os.system('ipython')

    elif args[0] == 'help':
        print(""" following arguments available:
        <migrate> for migrating tables to your database,
        <shell> for using ipython shell,
        <dbshell> connect current database,
        <run> run a tornado web server.""")
