from django_filters import rest_framework as filters, DateFromToRangeFilter, NumberFilter, CharFilter
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_it = DateFromToRangeFilter()
    creator = NumberFilter()
    status = CharFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at']
