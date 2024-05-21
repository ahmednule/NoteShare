import django_filters
from .models import Resource

class ResourceFilter(django_filters.FilterSet):
    
    created_at = django_filters.DateFromToRangeFilter()
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = Resource
        fields = ['title', 'description', 'created_at']
