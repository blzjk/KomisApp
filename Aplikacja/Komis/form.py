from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import Samochod, Kontakt

class MySignupForm(UserCreationForm):
    # dodajemy do formularza pole e-mail
    email = forms.EmailField(required=True)

    # wyświetalnie pola e-mail w formularzu
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MySignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Hasło"}))



class DateInput(forms.DateInput):
    input_type = 'date'

class CarForm(forms.ModelForm):
    class Meta:
        model = Samochod
        fields = ['marka', 'model', 'silnik', 'opony', 'skrzynia_biegow',
                  'moc', 'data_produkcji', 'kolor', 'opis', 'cena']
        widgets = {
            'data_produkcji': DateInput(),
        }


class ContactForm(ModelForm):
    temat = forms.CharField(max_length=70)
    class Meta:
        model = Kontakt
        fields = ('auto', 'wiadomosc')


class RentCarForm(forms.Form):
    liczbaDni = forms.ChoiceField()


