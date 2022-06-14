#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/30 14:32
# @Author  : Synanceia horrida
# @File    : urls.py.py
# @Software: PyCharm

from django.contrib import admin
from django.urls import path
from webapp import views

from django.conf.urls import include

app_name = 'webapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', views.article_list,name='article_list'),
    path('article-detail/<int:id>', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # # 删除文章
    # path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    # path('article-delete/<int:id>/',include('views.article_delete',namespace='webapp')),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]
