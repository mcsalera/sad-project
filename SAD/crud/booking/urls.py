from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='booking-home'),
    path('about/', views.about, name='booking-about'),
]