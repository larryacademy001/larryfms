"""
Form Module

Description:
This module specifies the in-built and custom form elements for
gathering data about users
"""

from typing import Any
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)

from apm_accounts.choices import *
from apm_accounts.models import ASHPenser


class ASHPenserCreationForm(UserCreationForm):
    """
    Create New User

    Description:
    Creates a form for the resgistration of new users
    """

    class Meta(UserCreationForm):
        model = ASHPenser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
    
    def clean_ashpenser_username(self):
        """
        Unique Username

        Description:
        Eliminates duplicate usernames. It prompts the user for
        an attempt to provide a duplicate username
        
        Returns:
        The username
        """

        username = self.clean_data.get("username")
        err_msg = f"{username} already taken.\nPlease choose a different username."

        if ASHPenser.objects.filter(username=username).exists():
            raise forms.ValidationError(err_msg)
        
        return username 


class ASHPenserChangeForm(LoginRequiredMixin, UserChangeForm):
    """
    Update User Data

    Description:
    Creates a form for updating the data of a user
    """

    class Meta:
        model = ASHPenser
        fields = (
            "last_name",
            "first_name",
            "username",
            "email",
            "security_question",
            "security_answer",
            "image",
        )


class ASHPenserLoginForm(forms.Form):
    """
    Login User

    Description:
    Creates a custom login feature to authenticate users
    """

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ASHPenserPassChangeForm(LoginRequiredMixin, PasswordChangeForm):
    """
    Change Password

    Description:
    Includes custom fields on form for changing user's password
    """

    security_question = forms.ChoiceField(choices=SECURITY_QUESTIONS, required=True, label="Security question")
    security_answer = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Security answer")

    def __init__(self, *args, **kwargs):
        user = kwargs.get("user")
        super().__init__(*args, **kwargs)

        if user:
            self.fields["security_question"].initial = user.security_question
        
        # Override the custom help texts
        self.fields['old_password'].help_text = ""
        self.fields['new_password1'].help_text = ""
        self.fields['new_password2'].help_text = ""
    
    def clean_security_answer(self):
        user = self.user
        security_answer = self.cleaned_data.get("security_answer")
        err_msg = "Sorry, security answer is incorrect!"

        if security_answer != user.security_answer:
            raise forms.ValidationError(err_msg)
        
        return security_answer