# -*- coding: utf-8 -*-
"""
URLs for Bank app
"""

from django.urls import re_path
from banks.views import IndexBanksView, UpdateBanksView, bank_attribute_save, bank_attribute_update, bank_attribute_delete

urlpatterns = [
    re_path(r'^create',
        IndexBanksView.as_view(),
        name='banks_create'),
    re_path(r'^update/bank/(?P<bank_id>[0-9\w\@\.\+-]+)/$',
        UpdateBanksView.as_view(),
        name='banks_update'),
    re_path(r'save/attribute', bank_attribute_save,
        name='bank_attribute_save'),
    re_path(r'updateattribute/attribute', bank_attribute_update,
        name='bank_attribute_update'),
    re_path(r'delete/attribute', bank_attribute_delete,
        name='bank_attribute_delete'),
]