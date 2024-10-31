# -*- coding: utf-8 -*-
"""
URLs for config app
"""

from django.urls import re_path

from .views import IndexView, webui_save, webui_delete

urlpatterns = [
    re_path(r'^$',
        IndexView.as_view(),
        name='webui-index'),
    re_path(r'save/method', webui_save,
        name='methodrouting-save'),
    re_path(r'delete/method', webui_delete,
        name='methodrouting-delete')
]
