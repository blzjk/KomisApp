import django_filters
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
            'marka': ['exact'],
            'model': ['icontains'],
            'typ': ['exact'],
            'paliwo': ['exact'],
            'kolor': ['exact'],
            'naped': ['exact'],
            'cena': ['lt', 'gt'],
            'opis': ['contains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'data_produkcji' if value =='rosnąco' else '-data_produkcji'
        return queryset.order_by(expression)