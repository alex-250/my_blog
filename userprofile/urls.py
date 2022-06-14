#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 15:57
# @Author  : Synanceia horrida
# @File    : urls.py.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('delete/<int:id>/', views.user_delete, name='delete'),
    # 用户信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),
]