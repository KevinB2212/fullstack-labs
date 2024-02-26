from django.contrib import admin
from .models import PizzaSize, PizzaCrust, PizzaSauce, CheeseType, PizzaTopping

admin.site.register(PizzaSize)
admin.site.register(PizzaCrust)
admin.site.register(PizzaSauce)
admin.site.register(CheeseType)
admin.site.register(PizzaTopping)