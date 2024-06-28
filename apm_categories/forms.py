"""
Forms Module

Description:
Create forms for categories, sub-categories and
payment methods
"""

from django import forms

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod
)


class ASHPenserCategoriesForm(forms.ModelForm):
    """
    Categories Form

    Description:
    Creates a form for adding and editing categories
    """

    class Meta:
        model = ASHPenserCategories
        fields = ["category_name", "category_type", "description"]


class ASHPenserSubCategoriesForm(forms.ModelForm):
    """
    Subcategories Form

    Description:
    Creates a form for adding and editing subcategories
    """
    
    class Meta:
        model = ASHPenserSubCategories
        fields = ["subcategory_name", "subcategory_type", "category_data", "description"]


class ASHPenserPaymentMethodForm(forms.ModelForm):
    """
    Payment Method Form

    Description:
    Creates a form for adding and editing pyament methods
    """

    class Meta:
        model = ASHPenserPaymentMethod
        fields = ["paymethod_name", "description"]