# -*- coding: utf-8 -*-
"""
URLs for entitlement requests app
"""

from django.urls import re_path

from .views import IndexView, RejectEntitlementRequest, AcceptEntitlementRequest

urlpatterns = [
    re_path(r'^$',
        IndexView.as_view(),
        name='entitlementrequests-index'),
    re_path(r'^entitlement-requests/entitlement_request_id/(?P<entitlement_request_id>[\w\@\.\+-]+)$',
        RejectEntitlementRequest.as_view(),
        name='entitlement-request-delete'),
    re_path(r'^entitlement-requests/user_id/(?P<user_id>[\w\@\.\+-]+)$',
        AcceptEntitlementRequest.as_view(),
        name='entitlement-request-accept'),
]
