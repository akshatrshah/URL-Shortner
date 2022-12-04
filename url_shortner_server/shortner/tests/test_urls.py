from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shortner.views import DeleteView, NewView, UpdateView, StubView, StatsView, ListUrlsView


class TestUrls(SimpleTestCase):
    def test_add_url_is_resolved(self):
        url = reverse('add_new')
        self.assertEquals(resolve(url).func.view_class, NewView)

    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=['special'])
        self.assertEquals(resolve(url).func.view_class, DeleteView)

    def test_update_url_is_resolved(self):
        url = reverse('update')
        self.assertEquals(resolve(url).func.view_class, UpdateView)

    def test_stub_url_is_resolved(self):
        url = reverse('stub', args=['some-url'])
        self.assertEquals(resolve(url).func.view_class, StubView)

    def test_stats_url_is_resolved(self):
        url = reverse('stats')
        self.assertEquals(resolve(url).func.view_class, StatsView)
    
    def test_list_url_is_resolved(self):
        url=reverse('list')
        self.assertEquals(resolve(url).func.view_class, ListUrlsView)
