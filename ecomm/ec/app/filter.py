import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    composition = django_filters.CharFilter(lookup_expr='icontains')
    prodapp = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['title', 'description', 'composition', 'prodapp']
