from django.urls import path
from . import views

urlpatterns = [
    path('homework/<int:homework_id>', views.homework, name="homework_single"),
    path('homework/list_view', views.HomeworkList.as_view()),
    path('', views.empty_path)
]