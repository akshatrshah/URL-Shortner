from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shortner.views import DeleteView, NewView, UpdateView, StubView
from shortner.views import StatsView, ListUrlsView, signup, signout, signin


class TestUrls(SimpleTestCase):
    def test_add_url_is_resolved(self):
        """Test adding url"""
        url = reverse('add_new')
        self.assertEqual(resolve(url).func.view_class, NewView)

    def test_delete_url_is_resolved(self):
        """Test deleting url"""
        url = reverse('delete', args=['special'])
        self.assertEqual(resolve(url).func.view_class, DeleteView)

    def test_update_url_is_resolved(self):
        """Test updating url"""
        url = reverse('update')
        self.assertEqual(resolve(url).func.view_class, UpdateView)

    def test_stub_url_is_resolved(self):
        """Test stub url"""
        url = reverse('stub', args=['some-url'])
        self.assertEqual(resolve(url).func.view_class, StubView)

    def test_stats_url_is_resolved(self):
        """Test stats url"""
        url = reverse('stats')
        self.assertEqual(resolve(url).func.view_class, StatsView)

    def test_list_url_is_resolved(self):
        """Test list url"""
        url = reverse('list')
        self.assertEqual(resolve(url).func.view_class, ListUrlsView)

    def test_signin_url_is_resolved(self):
        """Test signin url"""
        url = reverse('signin')
        self.assertEqual(resolve(url).func, signin)

    def test_signout_url_is_resolved(self):
        """Test signout url"""
        url = reverse('signout')
        self.assertEqual(resolve(url).func, signout)

    def test_signup_url_is_resolved(self):
        """Test signup url"""
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)
