from django_filters import rest_framework as filters
from flight_board.models import Flight


# def get_duration(duration):
#     print('-------------------------------------------')
#     print(duration)
#     print('-------------------------------------------')
#     seconds = duration.total_seconds()
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     return f'{int(hours)} час {int(minutes)} минут'
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FlightFilter(filters.FilterSet):
    number_of_seats_available = filters.RangeFilter()
    transit_landings = filters.BooleanFilter()
    airline_companies = CharFilterInFilter(field_name='airplane__airline_company__name', lookup_expr='in')

    class Meta:
        model = Flight
        fields = ['number_of_seats_available', 'transit_landings', 'airline_companies']
