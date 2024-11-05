# -*- coding: utf-8 -*-
"""
URLs for metrics app
"""

from django.urls import re_path

from .views import IndexProductView, UpdateProductView, create_list

urlpatterns = [
    re_path(r'^create',
        IndexProductView.as_view(),
        name='products-create'),
    re_path(r'^update/(?P<product_code>[0-9\w\@\.\+-]+)/bank/(?P<bank_id>[0-9\w\@\.\+-]+)/$',
               UpdateProductView.as_view(),
               name='products_update'),
    re_path(r'^createProductList',
       create_list,
       name = 'create-product-list'),
]
