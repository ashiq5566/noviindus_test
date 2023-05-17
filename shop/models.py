from django.db import models
from django.contrib.auth.models import User
import datetime
import os


class new_user(models.Model):
    username=models.CharField(max_length=100, null=False)
    password=models.CharField(max_length=100, null=False)
    email=models.CharField(max_length=100, null=False)
    
class product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    company_name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    black = models.BooleanField(default=False, help_text="0=default, 1=Black")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.product_qty * self.product.price

    def total(self):
        self.product.price + 50