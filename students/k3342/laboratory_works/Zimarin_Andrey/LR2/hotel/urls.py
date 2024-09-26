from django.urls import path
from . import views


urlpatterns = [
    path('clients/', views.Clients.as_view()),
    path('client_detail/<int:pk>', views.ClientDetailsView.as_view()),
    path('clients_filter/', views.ClientsList.as_view()),
    path('rooms/', views.Rooms.as_view()),
    path('workers/', views.WorkersView.as_view()),
    path('del_worker/<int:pk>', views.DelWorker.as_view()),
    path('room_detail/<int:pk>', views.RoomDetailsView.as_view()),
    path('cleanings/<int:pk>', views.CleaningTable.as_view()),
    path('cleanings_view/<int:pk>', views.CleaningsView.as_view()),
    path('checkin/', views.AddCheckin.as_view()),
    path('checkin_filter/', views.CheckinsList.as_view()),
    path('floors/', views.FloorsView.as_view()),
]
