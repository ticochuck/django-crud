from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Records

# Create your tests here.

class RecordTest(TestCase):

    def test_homepage_status(self):
        self.helper_status_tests('home')


    def helper_status_tests(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_homepage_template(self):
        self.templates_tests('home', 'home.html')

    
    def templates_tests(self, url_name, template_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


class TestModels(TestCase):

    def setUp(self):
        
        self.user = get_user_model().objects.create_user(
            username="test",
            email="test@email.com",
            password="testing123456"
        )
        
        self.record = Records(
            title="one",
            author=self.user,
            artist="U2",
            description="One from U2"
        )
        
        self.record.save()

        self.records = Records.objects.get(pk=1)


    def test_post(self):
        self.assertEqual(self.record, self.records)

    
    def test_model_title(self):
        self.assertEqual(self.record.title, self.records.title)


    def test_create_redirect_home(self):
        response = self.client.post(reverse("create"), {
            "title" : "one",
            "author" : self.user,
            "artist" : "U2",
            "description" : "One from U2"
        }
        , follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')