from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')