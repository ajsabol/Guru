import django_filters
from .models import Order_item


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Order_item
        fields = ['item_ordered', 'item_vendor', 'item_arrived','item_picked_up']