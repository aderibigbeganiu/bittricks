import uuid
from django.db import models
from django.conf import settings

class Order(models.Model):
    BUY = "BUY"
    SELL = "SELL"
    ORDER_TYPE_CHOICE = [
        (BUY, 'BUY'),
        (SELL, 'SELL'),
    ]
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    order_type  = models.CharField(max_length=5, choices=ORDER_TYPE_CHOICE)
    amount      = models.DecimalField(max_digits=11, decimal_places=2)
    ref_number  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    completed   = models.BooleanField(default=False)
    date_created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
