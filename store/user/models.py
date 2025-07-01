from django.db import models


#create model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username