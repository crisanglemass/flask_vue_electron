# -- coding: utf-8 --
"""
 !/usr/bin/env python3
 -*- coding: utf-8 -*-
 @Time : 2023/5/18 10:29
 @Author : ZhangHui
 @Email : ujszhanghui@163.com
 @File : __init__.py.py
 @Software: PyCharm
"""
import logging
import os
from logging.handlers import RotatingFileHandler

import secrets
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

redis_conn = None


def setupLogging(level):
    logging.basicConfig(level=level)
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, "log")
    file_log_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 100, backupCount=10)

    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    file_log_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_log_handler)


def creat_app():
    app = Flask(__name__,
                static_folder='../static/static', template_folder='../templates')
    app.secret_key = secrets.token_urlsafe(32)

    setupLogging(logging.WARNING)
    CORS(app)

    app.config.from_object(config['development'])
    # mysql

    db.init_app(app)
    redis = app.config['REDIS_CLIENT']

    return app, redis
