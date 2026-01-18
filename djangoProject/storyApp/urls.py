#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 10:25:14 2026

@author: cod
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]