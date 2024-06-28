"""
Admin Panel

Description:
Create an administration panel for superuser
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apm_accounts.forms import ASHPenserCreationForm, ASHPenserChangeForm
from apm_accounts.models import ASHPenser


# Register your models here.
class ASHPenserAdminPanel(UserAdmin):
    """
    Customize the admin panel for the super user
    """

    add_form = ASHPenserCreationForm
    form = ASHPenserChangeForm
    nodel = ASHPenser
    list_display = [
        "username",
        "email",
        "last_name",
        "first_name",
        "security_question",
        "security_answer",
        "is_active",
        "image",
        "is_staff",
    ]

    fieldsets = (
        ("Personal Information", {
            "fields": ("last_name", "first_name"),
            "description": "User's personal information",
        }),
        ("Authentication Information", {
            "fields": ("username", "email"),
            "description": "User's authentication information",
        }),
        ("Security Information", {
            "fields": ("security_question", "security_answer"),
            "description": "Security information for password reset",
        }),
        ("Media Information", {
            "fields": ("image",),
            "description": "The photo of the user",
        }),
        ("Staff Information", {
            "fields": ("is_staff",),
            "description": "User staff status",
        }),
        ("Miscellaneous", {
            "fields": ("is_active",),
            "description": "Current status of user",
        })
    )

    list_filter = ("last_name", "first_name", "is_active")
    ordering = ("last_name", "first_name")
    search_fields = ("last_name", "first_name")

admin.site.site_header = "ASHPense Administration Panel"
admin.site.register(ASHPenser, ASHPenserAdminPanel)
admin.site.unregister(Group)