#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 21:38
# @Author  : Synanceia horrida
# @File    : urls.py.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]