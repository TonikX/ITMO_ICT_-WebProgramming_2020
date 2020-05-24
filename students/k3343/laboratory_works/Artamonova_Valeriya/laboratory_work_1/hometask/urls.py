from urllib import request

from django.urls import path
from django.contrib.auth import views as view
from . import views
from .views import StudentRegistrationView, AddCommentView, RegisterUserView

urlpatterns = [
    path('', views.index, name='index'),
    path('all_hometasks', views.show_tasks, name='all_hometasks'),
    path('profile', StudentRegistrationView.as_view, name='profile_page'),
    path('add_comment', AddCommentView.as_view, name='add_comment'),
    path('all_comments', views.show_comments, name='all_comments'),
    path('login/', view.LoginView.as_view(), name='login'),
    path('logout/', view.LogoutView.as_view(), name='logout'),
    path('register', RegisterUserView.as_view(), name='register_page'),
]