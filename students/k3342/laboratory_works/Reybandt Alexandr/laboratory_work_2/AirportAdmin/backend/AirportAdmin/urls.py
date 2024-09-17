from django.contrib import admin
from django.urls import path, include
from flight_board.views import redirect_flight

urlpatterns = [
    path('', redirect_flight),
    path('admin/', admin.site.urls),
    path('api/v1/', include('flight_board.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
