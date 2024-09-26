from django.urls import path
from . import views

urlpatterns = [
    path('owner/', views.CarOwner),
    path('owner/<int:birthdate>/', views.CarOwner),
]