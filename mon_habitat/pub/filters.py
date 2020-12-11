import django_filters
from .models import *


class PublicationFilter(django_filters.FilterSet):
    class Meta:
        model = Publication
        fields = (
            'cities', 'categories', 'status'
        )