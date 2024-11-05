# -*- coding: utf-8 -*-
"""
URLs for OBP app
"""

from django.urls import re_path

from .views import (
    OAuthInitiateView, OAuthAuthorizeView,
    DirectLoginView,
    GatewayLoginView,
    LogoutView,
)


urlpatterns = [
    re_path(r'^oauth/initiate$',
        OAuthInitiateView.as_view(), name='oauth-initiate'),
    re_path(r'^oauth/authorize$',
        OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    re_path(r'^directlogin$',
        DirectLoginView.as_view(), name='directlogin'),
    re_path(r'^gatewaylogin$',
        GatewayLoginView.as_view(), name='gatewaylogin'),
    re_path(r'^logout$',
        LogoutView.as_view(), name='oauth-logout'),
]
