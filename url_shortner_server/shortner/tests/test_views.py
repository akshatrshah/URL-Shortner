from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from shortner.models import give_link_by_username_long_url, give_links


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_new_url = reverse("add_new")
        self.update_url = reverse("update")

    def tearDown(self) -> None:
        user = User.objects.get(username='akash2')
        user.delete()
        return super().tearDown()

    def test_all_view(self):
        """Test all views"""
        req_long_url = "https://www.google.com/"
        http_response = self.client.post(
            reverse('signup'),
            {'username': 'akash2', 'pass1': 'password', 'pass2': 'password',
                'fname': 'Akash', 'lname': 'Sarda', 'email': 'aks@google.com'}
        )

        http_response = self.client.post(
            reverse('signin'),
            {'username': 'akash2', 'pass1': 'password'}
        )

        http_response = self.client.post(
            reverse('add_new'),
            {"long-url": req_long_url},
        )

        self.assertEqual(http_response.status_code, 302)
        link = give_link_by_username_long_url('akash2', req_long_url)
        long_url = link.long_url
        stub = link.stub
        self.assertEqual(10, len(stub))
        self.assertNotEqual(9, len(stub))
        self.assertEqual(long_url, req_long_url)
        self.stub_url = reverse("stub", args=[stub])
        http_response = self.client.get(self.stub_url)
        self.assertEqual(http_response.status_code, 302)

        link = give_link_by_username_long_url('akash2', req_long_url)
        assert link.ctr == 1
        long_url2 = "https://moodle-courses2223.wolfware.ncsu.edu/gr\
                ade/report/user/index.php?id=2910"
        http_response = self.client.post(
            reverse('add_new'),
            {"long-url": long_url2},
        )

        http_response = self.client.get(
            reverse('list')
        )
        self.assertEqual(http_response.status_code, 200)

        http_response = self.client.get(
            reverse('stats')
        )

        self.assertEqual(http_response.status_code, 200)

        links = give_links('akash2')
        assert len(links) == 2
        delete_reponse = self.client.get(
            reverse('delete', args=[link.special_code]),
        )
        self.assertEqual(delete_reponse.status_code, 302)

        link = give_link_by_username_long_url('akash2', long_url2)
        delete_reponse = self.client.get(
            reverse('delete', args=[link.special_code]),
        )
        self.assertEqual(delete_reponse.status_code, 302)

        # Verify error in deleting deleted entry
        delete_reponse = self.client.delete(
            reverse('delete', args=[link.special_code]),
        )
        self.assertEqual(delete_reponse.status_code, 405)
