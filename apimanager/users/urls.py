# -*- coding: utf-8 -*-
"""
URLs for users app
"""

from django.urls import re_path
from django.urls import path

from .views import IndexView, DetailView, MyDetailView, DeleteEntitlementView, InvitationView, UserStatusUpdateView, \
    ExportCsvView, AutocompleteFieldView, DeleteAttributeView

urlpatterns = [
    re_path(r'^all$',
        IndexView.as_view(),
        name='users-index'),
    re_path(r'^all/user_id/(?P<user_id>[\w\@\.\+-]+)$',
        DetailView.as_view(),
        name='users-detail'),
    re_path(r'^myuser$',
        MyDetailView.as_view(),
        name='my-user-detail'),
    re_path(r'^myuser/invitation$',
        InvitationView.as_view(),
        name='my-user-invitation'),
    re_path(r'^(?P<user_id>[\w-]+)/entitlement/delete/(?P<entitlement_id>[\w-]+)$',
        DeleteEntitlementView.as_view(),
        name='users-delete-entitlement'),
    re_path(r'^(?P<user_id>[\w-]+)/atribute/delete/(?P<user_attribute_id>[\w-]+)$',
        DeleteAttributeView.as_view(),
        name='users-delete-attribute'),
    re_path(r'^(?P<user_id>[\w-]+)/userStatusUpdateView/(?P<username>[\w\@\.\+-]+)$',
        UserStatusUpdateView.as_view(),
        name='user-status-update'),
    re_path(r'^export_csv$',
        ExportCsvView.as_view(),
        name='export-csv-users'),
]
