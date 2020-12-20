from rest_framework import viewsets
from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
    queryset            = Order.objects.all()
    serializer_class    = OrderSerializer
    lookup_field        = 'pk'