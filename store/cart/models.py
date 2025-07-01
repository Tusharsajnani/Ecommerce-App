from django.db import models


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='cart', default=1)
    product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name='cart_item')
    
    def __str__(self):
        return f"Cart_id {self.cart_id} - Product: {self.product_id} (User: {self.user_id})"
    
    