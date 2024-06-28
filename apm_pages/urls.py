"""
Pages Routes

Description:
This specifies the paths for page switching
"""
from django.urls import path

from apm_pages.views import (
    ASHPenserDashboardView,
    ASHPenserIndexPageView
)


urlpatterns = [
    path("", ASHPenserIndexPageView.as_view(), name="index"),
    path("home/", ASHPenserDashboardView.as_view(), name="home"),
]
