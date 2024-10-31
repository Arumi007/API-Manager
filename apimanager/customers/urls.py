# -*- coding: utf-8 -*-
"""
URLs for customers app
"""

from django.urls import re_path
from .views import CreateView

urlpatterns = [
    re_path(r'^$',
        CreateView.as_view(),
        name='customers-create'),
]
