"""
Static Pages View

Description:
Manages the page switching for static pages
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ASHPenserDashboardView(LoginRequiredMixin, TemplateView):
    """
    Template for the dashboard page
    """
    
    template_name = "home.html"
    login_url = "login"

    @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True))
    def dispatch(self, *args, **kwargs):
        """
        Diasble Cache

        Description:
        Disables the caching of the dashboard by overrding the dispatch
        method. This enforces users to login before accessing the dashboard
        """
        return super().dispatch(*args, **kwargs)


class ASHPenserIndexPageView(TemplateView):
    """
    Template for index/landing page
    """

    template_name = "index.html"