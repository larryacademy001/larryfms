"""
ASHPense Front-end Routes

Description:
This module specifies the paths to the various static files for
the front-end elements
"""

from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from apm_accounts.views import (
    ASHPenserSignupView,
    ASHPenseLogoutView,
    ASHPenserLoginView,
    ASHPenserPassChangeView,
)


urlpatterns = [
    path("signup/", ASHPenserSignupView.as_view(), name="signup"),
    path("apm_accounts/login/", ASHPenserLoginView.as_view(), name="login"),
    path("apm_accounts/logout/", ASHPenseLogoutView.as_view(), name="logout"),
    path("apm_accounts/pass_change/", ASHPenserPassChangeView.as_view(), name="pass_change"),
    path("apm_accounts/pass_change_done/", TemplateView.as_view(template_name="registration/pass_change_done.html"), name="pass_change_done"),
]
