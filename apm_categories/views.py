"""
ASHPense Categories View
"""

from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models.base import Model as Model
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod
)


# Create your views here.
class ASHPenserCategoryListView(LoginRequiredMixin, TemplateView):
    """
    Categories List View

    Description:
    Creates a view for the display of categories list
    """

    # model = ASHPenserCategories
    template_name = "apm_categories/apm_categories_panel.html"

    def get_context_data(self, **kwargs):
        """
        Get Context Data

        Descriptions:
        Loads data from three models
        """

        context = super().get_context_data(**kwargs)
        context["apm_categories"] = ASHPenserCategories.objects.all()
        context["apm_subcategories"] = ASHPenserSubCategories.objects.all()
        context["apm_paymethods"] = ASHPenserPaymentMethod.objects.all()

        return context


class ASHPenserCategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display Category Object Details

    Description:
    Displays the details of a selected category object
    """

    model = ASHPenserCategories
    template_name = "apm_categories/apm_category_detail.html"


class ASHPenserCategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Category Object Data

    Description
    Displays form to update data of a category's object
    """

    model = ASHPenserCategories
    fields = ["category_name", "category_type", "description"]
    template_name = "apm_categories/updates/apm_category_update.html"


class ASHPenserCategoryDeleteView(DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserCategories
    template_name = "apm_categories/delete/apm_category_delete.html"
    success_url = reverse_lazy("apm_categories:apm_categories_panel")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def delete(self, request, *args, **kwargs):
        info_msg = "Category data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)


class ASHPenserSubCategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display Sub-category Object Details

    Description:
    Displays the details of a selected sub-category object
    """

    model = ASHPenserSubCategories
    template_name = "apm_categories/apm_subcategory_detail.html"


class ASHPenserSubCategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Sub-category Object Data

    Description:
    Displays form to update data of subcategory's bject
    """

    model = ASHPenserSubCategories
    fields = ["subcategory_name", "subcategory_type", "category_data",  "description"]
    template_name = "apm_categories/updates/apm_subcategory_update.html"


class ASHPenserSubCategoryDeleteView(DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserSubCategories
    template_name = "apm_categories/delete/apm_subcategory_delete.html"
    success_url = reverse_lazy("apm_categories:apm_categories_panel")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def delete(self, request, *args, **kwargs):
        info_msg = "Sub-category data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)


class ASHPenserPaymentMethodDetailView(LoginRequiredMixin, DetailView):
    """
    Display Payment method Object Details

    Description:
    Displays the details of a selected sub-category object
    """

    model = ASHPenserPaymentMethod
    template_name = "apm_categories/apm_paymethod_detail.html"


class ASHPenserPaymentMethodUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Payment Method Object Data

    Description:
    Displays form to update data of payment method's object
    """

    model = ASHPenserPaymentMethod
    fields = ["paymethod_name", "description"]
    template_name = "apm_categories/updates/apm_paymethod_update.html"


class ASHPenserPaymentMethodDeleteView(DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserPaymentMethod
    template_name = "apm_categories/delete/apm_paymethod_delete.html"
    success_url = reverse_lazy("apm_categories:apm_categories_panel")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def delete(self, request, *args, **kwargs):
        info_msg = "Payment method data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)