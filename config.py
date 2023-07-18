# -- coding: utf-8 --
"""
 !/usr/bin/env python3
 -*- coding: utf-8 -*-
 @Time : 2023/4/27 17:14
 @Author : ZhangHui
 @Email : ujszhanghui@163.com
 @File : config.py.py
 @Software: PyCharm
"""
import logging
from redis import StrictRedis


class BaseConfig:
    # mysql database
    HOSTNAME = "sh-cynosdbmysql-grp-3g5ojk8k.sql.tencentcdb.com"
    PORT = 20687
    USERNAME = "root"
    PASSWORD = "102173122Zh"
    DATABASE = "crisangle_website"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    # redis database
    REDIS_HOST = "124.223.211.19"
    REDIS_PORT = 6379
    REDIS_DB = '0'
    REDIS_PASSWORD = "102173122Zh@"
    REDIS_CLIENT = StrictRedis(host=REDIS_HOST,
                               port=REDIS_PORT,
                               db=REDIS_DB,
                               password=REDIS_PASSWORD)




class DevelopmentConfig(BaseConfig):
    LOGGING_LEVEL = logging.WARNING
    DEBUG = False


class TestingConfig(BaseConfig):
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
