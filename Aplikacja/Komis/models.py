import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Kolor(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kolor"
        verbose_name_plural = "Kolory"


RODZAJ = (
    ('osobowy', 'Osobowy'),
    ('ciężarowy', 'Ciężarowy')
)

TYP = (
    ('Hatchback ', 'Hatchback'),
    ('Kombi', 'Kombi'),
    ('Sedan', 'Sedan'),
    ('Liftback', 'Liftback'),
    ('SUV ', 'SUV'),
    ('Crossover', 'Crossover'),
    ('Coupe/kabriolet/roadster', 'Coupe/kabriolet/roadster'),
)


class Marka(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Marki"


NAPED = (
    ('przód', 'Przód'),
    ('tył', 'Tył')
)

PALIWO = (
    ('benzyna', 'Benzyna'),
    ('gaz', 'Gaz'),
    ('Diesel', 'Diesel'),
    ('hybryda', 'Hybryda'),
    ('elektryk', 'Elektryk')
)

SKRZYNIABIEGOW = (

    ('automatyczna', 'automatyczna'),
    ('manualana', 'manualna')
)

LICZBADRZWI = (
    ('2', '2'),
    ('3', '3'),
    ('5', '5')
)



class Samochod(models.Model):
    def get_year(self):
        return self.data_produkcji.year



    def clean(self):
        if self.ilosc_dni_rezerwacji is None:
            self.ilosc_dni_rezerwacji = 0

    model = models.CharField(max_length=20)
    marka = models.ForeignKey(Marka, max_length=20, on_delete=models.CASCADE, null=True, blank=True, related_name="model")
    typ = models.CharField(choices=TYP, max_length=50)
    silnik = models.DecimalField(max_digits=3, decimal_places=1)
    kod_silnika = models.CharField(max_length=10, null=True, blank=True)
    foto = models.ImageField(null=True)
    opony = models.CharField(max_length=20)
    skrzynia_biegow = models.CharField(max_length=20, choices=SKRZYNIABIEGOW, default='manualna')
    moc = models.IntegerField()
    numer_rejestracyjny = models.CharField(max_length=20)
    numer_seryjny = models.CharField(max_length=20)
    kolor = models.ForeignKey(Kolor, on_delete=models.CASCADE)
    liczba_drzwi = models.CharField(max_length=3, choices=LICZBADRZWI, default=5)
    cena = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    data_produkcji = models.DateField(max_length=100)
    rodzaj = models.CharField(choices=RODZAJ, max_length=50, default='osobowy')
    opis = models.CharField(null=True, max_length=255)
    paliwo = models.CharField(max_length=50, choices=PALIWO, default='benzyna')
    naped = models.CharField(choices=NAPED, null=True, max_length=255, default='przód')
    rezerwacja = models.BooleanField(default=False)
    data_rezerwacji = models.DateTimeField(blank=True, null=True)
    ilosc_dni_rezerwacji = models.PositiveSmallIntegerField(default=7, blank=True, null=True)
    autor = models.ForeignKey(User, default=User, on_delete=models.CASCADE, null=True)
    data_dodania = models.DateTimeField(default=now, blank=True, editable=False)
    czyDoWynajecia = models.BooleanField(default=False)
    czyWynajety = models.BooleanField(default=False)
    data_wynajecia = models.DateTimeField(blank=True, null=True)
    okresWynajecia = models.IntegerField(null=True, blank=True, default=0)
    data_konca_wynajecia = models.DateTimeField(blank=True, null=True)
    kosztWynajmuZaDzien = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0)
    czyWidoczny = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Auta"

    def __str__(self):
        return str(self.marka) + " " + self.model + " " + str(self.silnik) + str(self.kod_silnika) + " " + str(self.moc) + "KM" + " " + str(self.get_year()) + "r."

class Zdjecie(models.Model):

    def __str__(self):
        return self.samochod.model

    foto = models.ImageField()
    samochod = models.ForeignKey(Samochod, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"


class Kontakt(models.Model):
    uzytkownik = models.ForeignKey(User, default=User, on_delete=models.CASCADE, null=True)
    auto = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    wiadomosc = models.TextField()

    def __str__(self):
        return self.email





