# -*- coding: utf-8 -*-
"""
URLs for System View app
"""

from django.urls import re_path
from .views import SystemView

urlpatterns = [
    re_path(r'^$',
        SystemView.as_view(),
        name='system_view'),
]
