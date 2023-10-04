from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_title = models.CharField(max_length=200)
    category_gif = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_title}"

class RegularPizza(models.Model):
    id = models.BigAutoField(primary_key=True)
    pizza_choice = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return f"Regular Pizza : {self.pizza_choice}"

class SicilianPizza(models.Model):
    id = models.BigAutoField(primary_key=True)
    pizza_choice = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return f"Sicilian Pizza : {self.pizza_choice}"

class Toppings(models.Model):
    id = models.BigAutoField(primary_key=True)
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.topping_name}"


class Sub(models.Model):
    id = models.BigAutoField(primary_key=True)
    sub_filling = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Sub : {self.sub_filling}"

class Pasta(models.Model):
    id = models.BigAutoField(primary_key=True)
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.dish_name}"


class Salad(models.Model):
    id = models.BigAutoField(primary_key=True)
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Salad : {self.dish_name}"



class DinnerPlatters(models.Model):
    id = models.BigAutoField(primary_key=True)
    dish_name = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Platter : {self.dish_name}"

class UserOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    order = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    time_of_order  = models.DateTimeField(default=datetime.now, blank=True)
    delivered = models.BooleanField()

    def __str__(self):
        return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"
class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField()

    def __str__(self):

        return f"Saved cart for {self.username}"
