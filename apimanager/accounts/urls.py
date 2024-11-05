# -*- coding: utf-8 -*-
"""
URLs for Account app
"""

from django.urls import re_path
from .views import IndexAccountsView

urlpatterns = [
    re_path(r'^create',
        IndexAccountsView.as_view(),
        name='accounts-create'),

]
