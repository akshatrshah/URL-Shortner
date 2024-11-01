from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shortner.views import (
    DeleteView, NewView, UpdateView, StubView, StatsView, ListUrlsView,
    signup, signout, signin, CustomView, home, delete_all_urls, about_us,
    create_url, login_test, homepage
)

class TestUrls(SimpleTestCase):
    def test_add_url_is_resolved(self):
        url = reverse('add_new')
        self.assertEqual(resolve(url).func.view_class, NewView)

    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=['special'])
        self.assertEqual(resolve(url).func.view_class, DeleteView)

    def test_update_url_is_resolved(self):
        url = reverse('update')
        self.assertEqual(resolve(url).func.view_class, UpdateView)
