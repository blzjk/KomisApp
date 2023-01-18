from django.test import TestCase
from Komis.models import Marka

class KontaktModelTestCase(TestCase):
    def setUp(self):
        self.marka=Marka(
            nazwa = "Alfa Romeo",
        )

    def test_contact_creation(self):
        self.marka.save()
        self.assertIsNone(self.marka.id)
