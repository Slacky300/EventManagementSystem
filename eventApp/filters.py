import django_filters
from . models import *
class VenueFilter(django_filters.FilterSet):

    class Meta:
        model = Venues
        fields = {
            'speciality' : ['exact'],
            'city' : ['exact'],
        }

