#help to search resources.
import django_filters
from .models import *
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        # implies that we can search by item's name
        fields = ['item_name']

class CategoryFilter(django_filters.FilterSet):
    model = Category
    fields = ['name']