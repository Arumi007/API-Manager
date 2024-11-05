# -*- coding: utf-8 -*-
"""
URLs for Account list app
"""

from django.urls import re_path
from .views import AccountListView, ExportCsvView

urlpatterns = [
    re_path(r'^$',
        AccountListView.as_view(),
        name='account-list'),
    re_path(r'^export_csv$',
        ExportCsvView.as_view(),
        name='export-csv-account')
]
