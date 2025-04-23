from django_filters.rest_framework import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta :
        model = Car
        fields = {
            'car_model': ['exact'],
            'price': ['gt','lt']
        }
