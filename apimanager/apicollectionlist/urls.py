# -*- coding: utf-8 -*-
"""
URLs for Api Collection list app
"""

from django.urls import re_path
from .views import ApiCollectionListView, ExportCsvView

urlpatterns = [
    re_path(r'^$',
        ApiCollectionListView.as_view(),
        name='apicollection-list'),
    re_path(r'^export_csv$',
        ExportCsvView.as_view(),
        name='export-csv-apicollection')
]
