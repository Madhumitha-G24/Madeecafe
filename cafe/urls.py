from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('address/', views.address, name='address'),
    path('payment/', views.payment, name='payment'),
    path('gpay/', views.gpay, name='gpay'),
    path('success/', views.success, name='success'),
]
