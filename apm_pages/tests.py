"""
Test cases for the static page views
"""

from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class ASHPenserHomePageTest(SimpleTestCase):
    """
    Test cases for the home page view
    """

    def test_url_exists_at_correct_location(self):
        """
        Test for the correct path for the home page
        """
        
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        """
        Test for the homepage view name and the correct template used
        """

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")