# -- coding: utf-8 --
"""
 !/usr/bin/env python3
 -*- coding: utf-8 -*-
 @Time : 2023/5/18 10:42
 @Author : ZhangHui
 @Email : ujszhanghui@163.com
 @File : models.py
 @Software: PyCharm
"""
from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    isVip = db.Column(db.String(255))

    def __init__(self, name, email, password, isVip):
        self.name = name
        self.email = email
        self.password = password
        self.isVip = isVip

    def check_password(self, password):
        return password == self.password


