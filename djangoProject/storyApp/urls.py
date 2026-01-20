#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 10:25:14 2026

@author: cod
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate/", views.generate, name="generate"),
    path("play/", views.play, name="play"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)