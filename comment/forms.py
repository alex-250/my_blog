#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 21:38
# @Author  : Synanceia horrida
# @File    : forms.py.py
# @Software: PyCharm

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']