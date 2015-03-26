from django.db import models
from django.contrib.auth.models import User
from kitchen.models import Dish


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=70)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    status_name = models.ForeignKey(OrderStatus)
    date = models.DateTimeField()
    total = models.FloatField()
    user_notes = models.CharField(max_length=1000, blank=True)
    manager_notes = models.CharField(max_length=1000, blank=True)
    address = models.CharField(max_length=500, blank=True)


class Customer(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, default=None)
    user_hash = models.CharField(max_length=100, unique=True)


class Basket(models.Model):
    dish = models.ForeignKey(Dish)
    quantity = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, blank=True, null=True)
    customer = models.ForeignKey(Customer)


