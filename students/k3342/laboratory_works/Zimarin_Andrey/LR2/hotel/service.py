from django_filters import rest_framework as filters
from .models import Client, Checkin, Cleaning


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ClientCityFilter(filters.FilterSet):
    """Фильтрация клиентов по городу"""
    city = CharFilterInFilter(field_name='city', lookup_expr='in')
    full_name = CharFilterInFilter(field_name='full_name', lookup_expr='in')
    day = filters.NumberFilter(field_name='checkin__date_out', lookup_expr='day')
    year = filters.NumberFilter(field_name='checkin__date_out', lookup_expr='year')
    month = filters.NumberFilter(field_name='checkin__date_out', lookup_expr='month')

    class Meta:
        model = Client
        fields = ['full_name', 'city', 'checkins']


class CheckinFilter(filters.FilterSet):
    client = filters.NumberFilter(field_name='client__id')
    day = filters.NumberFilter(field_name='date_out', lookup_expr='day')
    year = filters.NumberFilter(field_name='date_out', lookup_expr='year')
    month = filters.NumberFilter(field_name='date_out', lookup_expr='month')

    class Meta:
        model = Checkin
        fields = ['client', 'room', 'date_in', 'date_out']


class CleaningFilter(filters.FilterSet):
    worker = filters.NumberFilter(field_name='worker__id')
    day = filters.NumberFilter(field_name='day_of_week', lookup_expr='in')

    class Meta:
        model = Cleaning
        fields = ['worker', 'day_of_week']