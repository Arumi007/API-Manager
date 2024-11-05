# -*- coding: utf-8 -*-
"""
URLs for Product list app
"""

from django.urls import re_path
from .views import ProductListView, ExportCsvView

urlpatterns = [
    re_path(r'^$',
        ProductListView.as_view(),
        name='product-list'),
    re_path(r'^export_csv$',
        ExportCsvView.as_view(),
        name='export-csv-product'),

]
