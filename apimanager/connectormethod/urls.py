# -*- coding: utf-8 -*-
"""
URLs for config app
"""

from django.urls import re_path

from connectormethod.views import IndexView, connectormethod_save, connectormethod_update

urlpatterns = [
    re_path(r'^$',
        IndexView.as_view(),
        name='connectormethod'),
    re_path(r'save/connectormethod', connectormethod_save,
        name='connectormethod-save'),
    re_path(r'^update/connectormethod', connectormethod_update,
        name='connectormethod-update')
]
