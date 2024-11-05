# -*- coding: utf-8 -*-
"""
URLs for ATM list app
"""

from django.urls import re_path
from .views import AtmListView, ExportCsvView

urlpatterns = [
    re_path(r'^$',
        AtmListView.as_view(),
        name='atm-list'),
    re_path(r'^export_csv$',
            ExportCsvView.as_view(),
            name='export-csv')
]
