from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('registration/', views.register, name='registration'),
   path('login/', auth_views.LoginView.as_view(template_name='login'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('order_history/', views.order_history, name='order_history'),
   path('create_pizza/', views.create_pizza, name='create_pizza'),
   path('delivery_details/', views.delivery_details, name='delivery_details'),
   path('order_summary/', views.order_summary, name='order_summary'),
]