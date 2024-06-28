"""
Categories Admin Module
"""

from django.contrib import admin

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod
)


# Register your models here.
@admin.register(ASHPenserCategories)
class ASHPenserCategoriesAdmin(admin.ModelAdmin):
    """
    Customise Admin
    
    Description:
    Customises the admin panel for categories
    """

    list_display = ["category_name", "category_type", "date_created", "description", "ashpenser_data"]
    list_filter = ("category_name", "category_type", "date_created", "ashpenser_data")
    search_fields = ["category_name", "ashpenser_data"]
    fieldsets = (
        ("Period", {
            "fields": ("date_created", ),
            "description": "Current date and time for creating category",
        }),
        ("Category Particulars", {
            "fields": ("category_name", "category_type", "description", "ashpenser_data",),
            "description": "Category details",
        }),
    )


@admin.register(ASHPenserSubCategories)
class ASHPenserSubCategoriesAdmin(admin.ModelAdmin):
    """
    Custom Admin for Sub-categories

    Description
    Customises the admin panel for sub-categories
    """

    list_display = ["subcategory_name", "category_data", "subcategory_type", "date_created", "description", "ashpenser_data"]
    list_filter = ("subcategory_name", "date_created", "category_data", "ashpenser_data")
    search_fields = ["subcategory_name", "category_data", "ashpenser_data"]
    fieldsets = (
        ("Period", {
            "fields": ("date_created",),
            "description": "Current date and time"
        }),
        ("Sub-category Particulars", {
            "fields": ("category_data", "subcategory_name", "description", "ashpenser_data")
        }), 
    )


@admin.register(ASHPenserPaymentMethod)
class ASHPenserPaymentMethodAdmin(admin.ModelAdmin):
    """
    Custom Admin for Payment Methods

    Description
    Customises the admin panel for Payment Methods
    """

    list_display = ["paymethod_name", "date_created", "description", "ashpenser_data"]
    list_filter = ("paymethod_name", "date_created", "ashpenser_data")
    search_fields = ["paymethod_name", "ashpenser_data"]
    fieldsets = (
        ("Period", {
            "fields": ("date_created",),
            "description": "Current date and time"
        }),
        ("Sub-category Particulars", {
            "fields": ("paymethod_name", "description", "ashpenser_data")
        }), 
    )


# admin.site.site_header = "Categories Administration Section"