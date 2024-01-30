from django.urls import path
from . import views

urlpatterns = [
   path('base.html', views.index, name='base.html'),
   path('variable.html',views.variable, name='variable.html'),
   path('add.html', views.add, name='add.html'),
   path('ex2.html', views.ex2, name='ex2.html'),
   path('fizzbuzz.html', views.fizzbuzz, name='fizzbuzz.html'),
   path('random.html', views.randomnumber, name='random.html'),
   path('', views.base, name='index.html'),
]