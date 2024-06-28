"""
Test Cases for the APM Accounts
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
class ASHPenserSignupTest(TestCase):
    """
    Test cases for sign up view
    """

    def test_url_exists_at_correct_location(self):
        """
        Test for the existence of the url at the correct location
        """

        response = self.client.get("/apm_accounts/signup/")
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view_name(self):
        """
        Test for the signup view name and the correct template
        """

        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
    
    def test_signup_form(self):
        """
        Test the signup form
        """

        response = self.client.post(
            reverse("signup"), 
            {
                "username": "testuser",
                "email": "testuser@me.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@me.com")