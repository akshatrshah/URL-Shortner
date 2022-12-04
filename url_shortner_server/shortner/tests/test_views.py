# from unittest import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from shortner.models import give_link_by_username_long_url

# from shortner.models import Link
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_new_url = reverse("add_new")
        self.update_url = reverse("update")

        # User.objects.create(username='akash2', password='password', email = 'ak@google.com')

        # self.delete_url = reverse("delete")

    def test_all_view(self):
        req_long_url = "https://www.google.com/"

        http_response = self.client.post(
            reverse('signup'),
            {'username' : 'akash2', 'pass1':'password', 'pass2' : 'password', 'fname' : 'Akash', 'lname' : 'Sarda', 'email' : 'aks@google.com'}
        )

        http_response = self.client.post(
            reverse('signin'),
            {'username' : 'akash2', 'pass1':'password'}
        )
        
        http_response = self.client.post(
            reverse('add_new'),
            {"long-url": req_long_url},
        )
        
        self.assertEquals(http_response.status_code, 302)
        link = give_link_by_username_long_url('akash2', req_long_url)

        long_url = link.long_url
        stub = link.stub
        special_code = link.special_code
        self.assertEquals(10, len(stub))
        self.assertNotEquals(9, len(stub))
        self.assertEquals(long_url, req_long_url)

        self.stub_url = reverse("stub", args=[stub])
        http_response = self.client.get(self.stub_url)
        self.assertEquals(http_response.status_code, 302)

        # Verify invalid put request with incorrect stub
        update_response = self.client.put(
            self.update_url,
            {
                "new_long_url": new_long_url,
                "special_code": special_code,
                "stub": stub + "0",
            },
            content_type="application/json",
        )
        self.assertEquals(update_response.status_code, 404)

        self.stub_url = reverse("stub", args=[stub])
        http_response = self.client.get(self.stub_url)
        print(http_response)
        self.assertEquals(http_response.status_code, 302)
        self.assertEquals(http_response.url, new_long_url)
        # Valid delete
        delete_reponse = self.client.delete(
            self.delete_url,
            {"special_code": special_code},
            content_type="application/json",
        )
        self.assertEquals(delete_reponse.status_code, 204)
        # Verify error in deleting deleted entry
        delete_reponse = self.client.delete(
            self.delete_url,
            {"special_code": special_code},
            content_type="application/json",
        )
        self.assertEquals(delete_reponse.status_code, 404)

        self.stub_url = reverse("stub", args=[stub])
        http_response = self.client.get(self.stub_url)
        self.assertEquals(http_response.status_code, 302)
