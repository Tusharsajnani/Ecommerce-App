from django.db import models
import datetime

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    shipment_date = models.DateTimeField(default=datetime.datetime.today) 
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    user_id = models.ForeignKey('User',on_delete=models.CASCADE,related_name='customer')
    
    def __str__(self):
        return self.country