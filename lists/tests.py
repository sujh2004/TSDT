from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_home_page_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
# class SmokeTest(TestCase):
    
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

# Create your tests here.
