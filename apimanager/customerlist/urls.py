# -*- coding: utf-8 -*-
"""
URLs for customer list app
"""

from django.urls import re_path
from .views import CustomerListView, ExportCsvView

urlpatterns = [
    re_path(r'^$',
        CustomerListView.as_view(),
        name='customer-list'),
    re_path(r'^export_csv$',
            ExportCsvView.as_view(),
            name='export-csv-customer')
]
