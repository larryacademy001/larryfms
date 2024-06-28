"""
Transactions Admin Module
"""

from django.contrib import admin
# from django.contrib.auth.models import Group

from apm_incomes.models import ASHPenserIncome


# Register your models here.
@admin.register(ASHPenserIncome)
class ASHPenserIncomeAdmin(admin.ModelAdmin):
    """
    Customise Admin
    
    Description:
    Customises the admin panel for income transactions
    """

    list_display = ["ashpenser_data", "income_date", "category", "payer", "payment_method", "amount", "description"]
    list_filter = ("income_date", "category", "payer", "payment_method")
    search_fields = ["category", "payer", "payment_method"]
    fieldsets = (
        ("Period", {
            "fields": ("income_date", ),
            "description": "Time of transaction",
        }),
        ("Payment", {
            "fields": ("payer", "payment_method", "amount", ),
            "description": "Payment information",
        }),
        ("Details", {
            "fields": ("ashpenser_data", "category", "description",),
            "description": "Income particulars",
        }),
    )

admin.site.site_header = "Income Transactions Administration Section"
# admin.site.unregister(Group)