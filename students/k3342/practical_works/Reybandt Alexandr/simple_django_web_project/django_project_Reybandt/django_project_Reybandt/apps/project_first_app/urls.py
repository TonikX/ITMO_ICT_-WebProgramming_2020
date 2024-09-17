from django.urls import path
from . import views
from .views import CarList, CreateCar

urlpatterns = [
	path('', views.owners_list),
	path('owner_info', views.info, name = 'info'),
	path('owner/<int:ownership_id>', views.detail, name = 'detail'),
	path('car_list', CarList.as_view()),
	path('create_view', views.create_view),
	path('car_model', CreateCar.as_view()),
]
