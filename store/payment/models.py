from django.db import models

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    amount = models.FloatField()
    user_id = models.ForeignKey('User',on_delete=models.CASCADE,related_name='payment')
    
    
    def __str__(self):
        return f"Payment Method #{self.payment_method} | User ID: {self.user_id_id} | Payment Date: ₹{self.payment_date}"
        
    
