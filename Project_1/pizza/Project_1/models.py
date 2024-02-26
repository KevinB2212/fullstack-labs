from django.db import models

# Create your models here.
class PizzaSize(models.Model):
    name = models.CharField(max_length=50)

class PizzaCrust(models.Model):
    name = models.CharField(max_length=50)

class PizzaSauce(models.Model):
    name = models.CharField(max_length=50)

class CheeseType(models.Model):
    name = models.CharField(max_length=50)

class PizzaTopping(models.Model):
    name = models.CharField(max_length=50)

class Pizza(models.Model):
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(CheeseType, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(PizzaTopping)


from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    delivery_date_time = models.DateTimeField()
    payment_info = models.TextField()
    
