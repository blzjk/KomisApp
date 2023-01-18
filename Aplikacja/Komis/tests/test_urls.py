from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Komis.views import cars


class TestsUrls(SimpleTestCase):
    def test_home_is_resolved(self):
        url = reverse('samochody')
        print(resolve(url))
        self.assertEqual(resolve(url).func, cars)