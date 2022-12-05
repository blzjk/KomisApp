import django_filters

from .models import Samochod


class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Samochod
        fields = {
            'marka': ['exact'],
            'model' : ['exact']
        }