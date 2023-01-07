import math
from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.db.models import F
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML


from .filters import CarFilter
from .form import MySignupForm, LoginForm, CarForm, ContactForm, RentCarForm
from .models import Samochod, Marka, Zdjecie, Kolor, Kontakt
from django.views.generic import View, TemplateView
from django.http import JsonResponse


data = {
    'lang' : 'pl',
    'charset' : 'utf-8',
    'title' : 'komis.samochodowy.online.pl',
}

class MainView(TemplateView):
    template_name = 'index.html'

class CarJsonListView(View):
    def get(self, *args, **kwargs):
        samochody = list(Samochod.objects.values())
        return JsonResponse({'data':samochody}, safe=False)


def index(request):
    return index2(request, 1)


# wyświetlanie 3 ostatnio dodanych pojazdów
def index2(request, page):
    listaWidocznychZatwierdzonychAut = Samochod.objects.all().filter(czyWidoczny=True)
    listaZatwierdzonychAut = listaWidocznychZatwierdzonychAut.filter(czyDoWynajecia=False)
    # wyświetlanie ogłoszenia ostatnio dodanego na samej górze
    cars = listaZatwierdzonychAut.order_by('-id')[0:6]
    # pobranie ilości wszystkich ogłoszeń aby obliczyć ilość stron potrzebnych do wyświetlenia 3 ogłoszeń na stronie
    liczba = listaZatwierdzonychAut.count()
    pagecount = math.ceil(liczba / 3)
    dane = {
        'cars': cars,
        'pagecount': range(pagecount),
        'liczba': liczba,
    }
    return render(request, 'index.html', dane)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = MySignupForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Konto użytkownika: ' + str(user) + ' zostało utworzone.')
            return render(
                request, 'users/register_done.html', {'user': user}
            )
    form = MySignupForm()
    return render(
        request=request,
        template_name='users/register.html',
        context={
            'form': form
        }
    )


def user_login(request):
    # odebranie formularza
    if request.method == 'POST':
        # messages.success(request, 'Zostałeś poprawnie zalogowany.')
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            # sprawdzanie czy użytkownik został znaleziony
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST['next'])
                    return redirect("/")
                else:
                    return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse('Nierawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, "users/logout.html")


def car(request, id):
    try:
        car_user = Samochod.objects.get(pk=id)
        if car_user.rezerwacja:
            date_reservation = car_user.data_rezerwacji.strftime('%Y-%m-%d %H:%M')
            format = '%Y-%m-%d %H:%M'
            count = car_user.ilosc_dni_rezerwacji
            end_date_reservation = datetime.strptime(date_reservation, format) + timedelta(days=count)
        else:
            end_date_reservation = datetime.now()
        if car_user.czyWynajety:
            date_rent = car_user.data_wynajecia.strftime('%Y-%m-%d %H:%M')
            format = '%Y-%m-%d %H:%M'
            count = car_user.okresWynajecia
            end_date_rent = datetime.strptime(date_rent, format) + timedelta(days=count)
        else:
            end_date_rent = datetime.now()
        image_car = Zdjecie.objects.all()
        images = image_car.filter(samochod=car_user)
        return render(request, 'car.html', {
            'car': car_user,
            'image': images,
            'end_date_reservation': end_date_reservation,
            'end_date_rent' : end_date_rent,
        })
    except Samochod.DoesNotExist:
        return render(request, '404.html')
        return render(request, 'car.html', {
            'car': car_user,
            'image': images,
        })


def cars(request):
        carsVisible = Samochod.objects.all().filter(czyWidoczny=True)
        cars = carsVisible.filter(czyDoWynajecia=False)
        image = Zdjecie.objects.all()
        return render(request, 'cars.html', {
            'cars': cars,
            'image': image,
            'ratingRange': range(5)
        })


def carsAll(request):
    cars = Samochod.objects.all()
    image = Zdjecie.objects.all()
    return render(request, 'panel.html', {
        'cars': cars,
        'image': image,
        'ratingRange': range(5)
    })

def search(request):
    carsVisible = Samochod.objects.all().filter(czyWidoczny=True)
    cars = carsVisible.filter(czyDoWynajecia=False)
    car_filter = CarFilter(request.GET, queryset=cars)
    has_filter = any(field in request.GET for field in set(car_filter.get_fields()))
    context = {
        'car_filter': car_filter,
        'has_filter': has_filter
    }
    return render(request, "search.html", context)




@user_passes_test(lambda u: u.is_superuser)
def panel(request):
    cars = Samochod.objects.all()
    car_filter = CarFilter(request.GET, queryset=cars)
    has_filter = any(field in request.GET for field in set(car_filter.get_fields()))
    dane = {
        'cars': cars,
        'car_filter': car_filter,
        'has_filter': has_filter
    }
    return render(request, 'panel.html', dane)


@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        car = form.save(commit=False)
        car.autor = request.user
        if form.is_valid():
            car.save()
            return redirect('dodano_auto')
    form = CarForm()
    return render(
        request,
        'users/add_car.html',
        {
            'form': form
        }
    )


def make_of_car(request, id):
    make_user = Marka.objects.get(pk=id)
    makes = Samochod.objects.filter(marka=make_user)
    dane = {'cars': makes}
    return render(request, 'make_of_car.html', dane)


@login_required
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            admin_address = "blazej.kozikowski@gmail.com"
            responder_address = "komis.samochodowy.online@gmail.com"
            client_address = request.user.email
            auto = Samochod.objects.get(pk=request.POST['auto'])
            message_for_admin = """
                    Tutuł wiadomości: %s
                    Adres użytkownika: %s
                    Auto: %s %s
                    Kolor: %s
                    Nr rejestracyjny: %s
                    VIN: %s
                    Treść zapytania:
                        %s
            """ % (request.POST['subject'], client_address, auto.marka, auto, auto.kolor, auto.numer_rejestracyjny, auto.numer_seryjny, request.POST['wiadomosc'])
            message_for_client = """
                    Dzień dobry,
                    dziękuję za wysłanie zapytania dotyczącego auta: %s %s, kolor - %s. 
                    Postaram się odpowiedzieć w jak najkrótszym czasie. 
                    
                    Pozdrawiam,
                    Administrator Komisu Samochodowego "Aut-Ko"
                    ----
                    Wiadomość generowana automatycznie. Proszę nie odpowiadać na tego emaila.
            """ % (auto.marka, auto, auto.kolor)
            try:
                send_mail(auto, message_for_admin, responder_address, [admin_address])
                send_mail(auto, message_for_client, responder_address, [client_address])
            except BadHeaderError:
                print('Wykryto niepoprawny nagłówek')
            return render(request, "email-sent.html", data)
    else:
        data['form'] = ContactForm()
    return render(request, "contact.html", data)


@login_required
def carsForRent(request):
    carsVisible = Samochod.objects.all().filter(czyWidoczny=True)
    cars = carsVisible.filter(czyDoWynajecia=True)
    image = Zdjecie.objects.all()
    return render(request, 'carsForRent.html', {
        'cars': cars,
        'image': image,
    })


@csrf_exempt
def reservation(request, id):
  if request.method == 'POST':
    samochod = Samochod.objects.get(pk=id)
    samochod.rezerwacja = True
    samochod.data_rezerwacji = datetime.now()
    samochod.ilosc_dni_rezerwacji = 7
    samochod.save()
    return HttpResponse('Samochód został zarezerwowany')
  else:
    return HttpResponse('Nieprawidłowe żądanie')


@csrf_exempt
def cancel_reservation(request, id):
  if request.method == 'POST':
      samochod = Samochod.objects.get(pk=id)
      samochod.rezerwacja = False
      samochod.save()
      return HttpResponse('Samochód został zarezerwowany')
  else:
      return HttpResponse('Nieprawidłowe żądanie')



@csrf_exempt
def rent_a_car(request, id):
  if request.method == 'POST':
      form = RentCarForm(request.POST)
      samochod = Samochod.objects.get(pk=id)
      # samochod.ilosc_dni_rezerwacji = liczbaDni
      samochod.czyWynajety = True
      samochod.data_wynajecia = datetime.now()
      samochod.save()
      return HttpResponse('Samochód został zarezerwowany')
  else:
      return HttpResponse('Nieprawidłowe żądanie')


@csrf_exempt
def end_rent_a_car(request, id):
  if request.method == 'POST':
      samochod = Samochod.objects.get(pk=id)
      samochod.czyWynajety = False
      samochod.save()
      return HttpResponse('Koniec rezerwacji')
  else:
      return HttpResponse('Nieprawidłowe żądanie')


def car_added(request):
    return render(request, 'car_added.html')

@csrf_exempt
def car_visible(request, id):
  if request.method == 'POST':
      samochod = Samochod.objects.get(pk=id)
      samochod.czyWidoczny = True
      samochod.save()
      return HttpResponse('Samochód widoczny')
  else:
      return HttpResponse('Nieprawidłowe żądanie')


@csrf_exempt
def car_unvisible(request, id):
  if request.method == 'POST':
      samochod = Samochod.objects.get(pk=id)
      samochod.czyWidoczny = False
      samochod.save()
      return HttpResponse('Samochód niewidoczny')
  else:
      return HttpResponse('Nieprawidłowe żądanie')

@csrf_exempt
def search_visible(request):
    return render (request, 'panel.html')

@csrf_exempt
def search_unvisible(request):
    return render (request, 'panel.html')

@csrf_exempt
def car_save(request, id):
  if request.method == 'POST':
      samochod = Samochod.objects.get(pk=id)
      price = request.POST.get('price')
      price_rent = request.POST.get('price_rent')
      description = request.POST.get('description')
      samochod.cena = price
      samochod.kosztWynajmuZaDzien = price_rent
      samochod.opis = description
      samochod.save()
      return HttpResponse('Zmiany zapisane')
  else:
      return HttpResponse('Nieprawidłowe żądanie')