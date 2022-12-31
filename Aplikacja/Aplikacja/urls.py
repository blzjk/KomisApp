"""Aplikacja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Komis.views import register, user_login, user_logout, index, index2, car, make_of_car, add_car, search, panel, cars, contact_view, carsForRent, CarJsonListView, reservation, cancel_reservation, rent_a_car, end_rent_a_car, car_added


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cars-json/', CarJsonListView.as_view(), name='indexJson'),
    path('samochody', cars, name='samochody'),
    path('rejestracja', register, name='rejestracja'),
    path('kontakt', contact_view, name='kontakt'),
    path('logowanie', user_login, name='logowanie'),
    path('wylogowanie', user_logout, name='wylogowanie'),
    path('strona/<int:page>', index2, name='strona'),
    path('samochod/<id>/', car, name='car'),
    path('wynajem', carsForRent, name='wynajem'),
    path('marka/<id>/', make_of_car, name='marka'),
    path('dodaj_samochod', add_car, name='samochod'),
    path('szukaj/', search, name='szukaj'),
    path('panel/', panel, name='panel'),
    path('dodano_auto/', car_added, name='dodano_auto'),
    path('rezerwacja/<id>', reservation, name='rezerwacja'),
    path('koniec_rezerwacji/<id>', cancel_reservation, name='odwolaj_rezerwacje'),
    path('wynajem/<id>', rent_a_car, name='wynajem'),
    path('koniec_wynajmu/<id>', end_rent_a_car, name ='koniec_wynajmu'),
    path('haslo/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='haslo'),
    path('zmiana-hasla/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
