from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("all_products",views.all_products,name='all_products'),
    path('deserts',views.deserts,name='deserts'),
    path('contact',views.contact,name='contact'),
]   