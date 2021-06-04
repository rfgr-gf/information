# from flask import Flask
# from flask import session
# from flask_script import Manager
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.wtf import CSRFProtect
# from redis import StrictRedis
# from flask_session import Session
# from flask_migrate import  Migrate,MigrateCommand
#
#
# class Config():
#     # 项目的配置
#     DEBUG = True
#
#     SERCET_KEY = 'EFWSEGFWEGWEG'
#
#     # 数据库的配置
#     SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information14"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # Redis 的配置
#     REDIS_HOST = '127.0.0.1'
#     REDIS_PORT = 6379
#
#
#     # session 的配置
#     SESSION_TYPE = 'redis'
#
#     # 开启session签名
#     SESSION_USE_SIGNER = True
#
#     SESIION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
#
#     # 设置位 过期
#     SESSION_PERMANENT = False
#
#     PERMANENT_SESSION_LIFETIOME = 86400 * 2
#
# app = Flask(__name__)
#
#
#
#
#
#
# app.config.from_object(Config)
#
# # 初始化数据库
# db = SQLAlchemy(app)
#
# # 初始化 redis  存储对象
# redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
#
# # 开启当前项目 CSRF  保护
# CSRFProtect(app)
#
# Session(app)
#
# manager = Manager(app)
#
# # 将app 与 db关联
# Migrate(app,db)
#
# # 将迁移命令 添加到manager
# manager.add_command('db',MigrateCommand)
#
#
# @app.route('/')
# def index():
#     session['name'] = 'zhwy'
#     return 'hello 3333'
#
#
# if __name__ == '__main__':
#     manager.run()


from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
# 可以用来指定 session 保存的位置
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import  Config



app = Flask(__name__)
# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化 redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index33333'


if __name__ == '__main__':
    manager.run()