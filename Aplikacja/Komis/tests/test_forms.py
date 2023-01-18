from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Komis.form import CarForm


class TestsUrls(SimpleTestCase):
    def test_carForm_valid_data(self):
        form = CarForm(data={
            'marka': 'Opel',
            'model': 'Agila',
            'typ': 'osobowy',
            'foto': 'agila.jpg',
            'silnik':'1,2',
            'opony':'165/14/55',
            'skrzynia_biegow':'manulna',
            'moc':'60',
            'data_produkcji':'2016-02-18',
            'kolor': 'czerwony',
            'opis':'małe i tanie miejskie autko',
            'cena':'7900'
        })

        self.assertTrue(form.is_valid())

    def test_carForm_form_no_data(self):
        form = CarForm(data={})

        self.assertFalse(form.is_valid())
        self. assertEquals(len(form.errors),12)