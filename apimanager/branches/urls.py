# -*- coding: utf-8 -*-
"""
URLs for metrics app
"""

from django.urls import re_path

from .views import IndexBranchesView, UpdateBranchesView

urlpatterns = [
    re_path(r'^$',
        IndexBranchesView.as_view(),
        name='branches_list'),
    re_path(r'^update/(?P<branch_id>[0-9\w\@\.\+-]+)/bank/(?P<bank_id>[0-9\w\@\.\+-]+)/$',
        UpdateBranchesView.as_view(),
        name='branches_update')
]
