from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = format_suffix_patterns([
    path('flight/', views.FlightListViewSet.as_view({'get': 'list'}), name='flight_list_url'),
    path('flight/<int:pk>/', views.FlightDetailViewSet.as_view({'get': 'retrieve'})),
    # path('flight/check_in/', views.CheckInViewSet.as_view({'post': 'create'})),
    path('flight/profile/<int:pk>/', views.EmployeeView.as_view({'get': 'retrieve'})),
    path('flight/profile/job_app/', views.JobApplications.as_view({'get': 'list'})),
    path('flight/airline_company/', views.AirlineCompanyView.as_view()),
    path('flight/accounts/register/', views.registration_view, name="register"),
    # path('flight/accounts/login/', obtain_auth_token, name="login"),
    path('flight/accounts/login/', views.CustomAuthToken.as_view(), name="login"),
    path('flight/accounts/logout/', views.Logout.as_view(), name="logout")
])
