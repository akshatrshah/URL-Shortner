from unittest import TestCase
from shortner.models import Link


class TestModel(TestCase):
    def test_create_new_entry(self):
        """Create a new entry"""
        link = Link.objects.create( # pylint: disable=no-member
            long_url="www.ncsu.edu",
            special_code="00000000-0000-0000-0000-000000000000",
            stub="aaaaaaaaaa",
        )
        self.assertIsInstance(link.to_json(), str)
