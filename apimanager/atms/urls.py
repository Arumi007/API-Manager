# -*- coding: utf-8 -*-
"""
URLs for metrics app
"""

from django.urls import re_path
from atms.views import IndexAtmsView, UpdateAtmsView, atm_attribute_save, atm_attribute_delete, atm_attribute_update

urlpatterns = [
    re_path(r'^create',
        IndexAtmsView.as_view(),
        name='atms_create'),
    re_path(r'^update/(?P<atm_id>[ 0-9\w|\W\@\.\+-]+)/bank/(?P<bank_id>[0-9\w\@\.\+-]+)/$',
        UpdateAtmsView.as_view(),
        name='atms_update'),
    re_path(r'save/attribute', atm_attribute_save,
        name='atm_attribute_save'),
    re_path(r'delete/attribute', atm_attribute_delete,
        name='atm_attribute_delete'),
    re_path(r'updateattribute/attribute', atm_attribute_update,
        name='atm_attribute_update'),
]
