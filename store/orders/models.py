from django.db import models
from store.payment.models import Payment
from store.shipment.models import Shipment
from store.products.models import Product



class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.FloatField()
    
    # product_id = models.ForeignKey('Products',on_delete=models.CASCADE, related_name='orders')
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='orders')
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='orders')
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, related_name='orders')
    
    def __str__(self):
        return f"Order #{self.order_id} | User ID: {self.user_id} | Total: ₹{self.total_price}"


