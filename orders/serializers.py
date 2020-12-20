from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model               = Order
        fields              = ['url', 'user', 'order_type', 'currency', 'amount','ref_number', 'completed', 'date_created']
        read_only_fields    = ['completed', 'ref_number']
        extra_kwargs        = {
            'url': {'view_name': 'order-detail', 'lookup_field': 'pk'}
        }