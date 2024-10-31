# -*- coding: utf-8 -*-
"""
URLs for config app
"""

from django.urls import re_path

from dynamicendpoints.views import IndexView, dynamicendpoints_save,dynamicendpoints_delete

urlpatterns = [
    re_path(r'^$',
        IndexView.as_view(),
        name='dynamicendpoints-index'),
    re_path(r'save/dynamicendpoint', dynamicendpoints_save,
        name='dynamicendpoint-save'),
    re_path(r'delete/dynamicendpoint', dynamicendpoints_delete,
        name='dynamicendpoint-delete')
]
