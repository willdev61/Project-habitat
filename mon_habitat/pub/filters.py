import django_filters
from .models import *
from django_filters import  ChoiceFilter


class PublicationFilter(django_filters.FilterSet):
    class Meta:
        model = Publication
        fields =[
            'cities', 'categories', 'status'
        ]


# cities = ChoiceFilter(choices=CITIES_CHOICES)
    # categories = ChoiceFilter(choices=CATEGORIES_CHOICES)
    # status = ChoiceFilter(choices=STATUS_CHOICES)