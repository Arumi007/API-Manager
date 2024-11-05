# -*- coding: utf-8 -*-
"""
URLs for Bank list app
"""

from django.urls import re_path
from .views import BankListView #, ExportCsvView

urlpatterns = [
    re_path(r'^$',
        BankListView.as_view(),
        name='bank-list'),

]
"""
url(r'^export_csv$',
            ExportCsvView.as_view(),
            name='export-bank-csv') """
