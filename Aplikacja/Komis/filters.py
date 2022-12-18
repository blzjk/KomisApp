import django_filters
from crispy_forms.layout import Div, Field
from django_filters import CharFilter

from .models import Samochod


class CarFilter(django_filters.FilterSet):

    CHOICES = (
        ('rosnąco', 'Rosnąco'),
        ('malejąco', 'Malejąco')
    )
    ordering = django_filters.ChoiceFilter(label='Sortuj wg. daty produkcji', choices=CHOICES, method='filter_by_order')
    class Meta:
        model = Samochod
        fields = {
            'model': ['icontains'],
            'marka': ['exact'],
            'kolor': ['exact'],
            'typ': ['exact'],
            'paliwo': ['exact'],
            'naped': ['exact'],
            'cena': ['lt', 'gt'],
            'opis': ['contains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'data_produkcji' if value =='rosnąco' else '-data_produkcji'
        return queryset.order_by(expression)