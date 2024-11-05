# -*- coding: utf-8 -*-
"""
URLs for config app
"""

from django.urls import re_path

from methodrouting.views import IndexView, methodrouting_save, methodrouting_delete

urlpatterns = [
    re_path(r'^$',
        IndexView.as_view(),
        name='methodrouting-index'),
    re_path(r'save/method', methodrouting_save,
        name='methodrouting-save'),
    re_path(r'delete/method', methodrouting_delete,
        name='methodrouting-delete'),
]
