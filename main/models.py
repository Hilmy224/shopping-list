from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    #Each user having diffrent proudcts
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    
    
