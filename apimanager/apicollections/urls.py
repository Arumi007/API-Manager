# -*- coding: utf-8 -*-
"""
URLs for config app
"""

from django.urls import re_path

from apicollections.views import IndexView, apicollections_save, \
    apicollections_delete, DetailView, DeleteCollectionEndpointView, apicollections_update

urlpatterns = [
    re_path(r'^$',
        IndexView.as_view(),
        name='apicollections-index'),
    re_path(r'save/apicollection', apicollections_save,
        name='apicollection-save'),
    re_path(r'update/apicollection', apicollections_update,
        name='apicollection-update'),
    re_path(r'delete/apicollection', apicollections_delete,
        name='apicollection-delete'),
    re_path(r'^my-api-collection-ids/(?P<api_collection_id>[\w\@\.\+-]+)$',
        DetailView.as_view(),
        name='my-api-collection-detail'),
    re_path(r'^delete/api-collections/(?P<api_collection_id>[\w-]+)/api-collection-endpoint/(?P<operation_id>[\w\@\.\+-]+)$',
        DeleteCollectionEndpointView.as_view(),
        name='delete-api-collection-endpoint'),
]
