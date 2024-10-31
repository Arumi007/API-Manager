# -*- coding: utf-8 -*-
"""
URLs for metrics app
"""

from django.urls import re_path

from .views import (
    APIMetricsView,
    APISummaryPartialFunctionView,
    ConnectorMetricsView,
    MonthlyMetricsSummaryView,
    YearlySummaryView,
    QuarterlySummaryView,
    WeeklySummaryView,
    DailySummaryView,
    HourlySummaryView,
    CustomSummaryView,
    get_metric_last_endpoint
)

urlpatterns = [
    re_path(r'^api/$',
        APIMetricsView.as_view(),
        name='api-metrics'),
    re_path(r'^api/last-endpoint/$',
        get_metric_last_endpoint,
        name='api-metrics-last-endpoint'),
    re_path(r'^api/summary-partial-function$',
        APISummaryPartialFunctionView.as_view(),
        name='api-metrics-summary-partial-function'),
    re_path(r'^connector/$',
        ConnectorMetricsView.as_view(),
        name='connector-metrics'),
    re_path(r'^monthly-summary/$',
        MonthlyMetricsSummaryView.as_view(),
        name='metrics-summary'),
    re_path(r'^yearly-summary/$',
        YearlySummaryView.as_view(),
        name='yearly-summary'),
    re_path(r'^quarterly-summary/$',
        QuarterlySummaryView.as_view(),
        name='quarterly-summary'),
    re_path(r'^weekly-summary/$',
        WeeklySummaryView.as_view(),
        name='weekly-summary'),
    re_path(r'^daily-summary/$',
        DailySummaryView.as_view(),
        name='daily-summary'),
    re_path(r'^hourly-summary/$',
        HourlySummaryView.as_view(),
        name='hourly-summary'),
    re_path(r'^custom-summary/$',
        CustomSummaryView.as_view(),
        name='custom-summary'),
]
