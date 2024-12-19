import django_filters
from .models import Emigrant

class EmigrantFilter(django_filters.FilterSet):
    class Meta:
        model = Emigrant
        fields = {
            'gender': ['exact'],
            'marital_status': ['exact'],
            'education': ['exact'],
            'nationality': ['exact'],
            'country_of_emigration': ['exact'],
        }