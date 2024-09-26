from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars),
    path('owner/<int:owner_id>', views.owner),
    path('all_owners', views.all_owners),
    path('all_cars', views.AllCars.as_view()),
    path('add_owner', views.add_owner),
    path('add_car', views.AddCar.as_view())
]