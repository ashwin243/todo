from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_create),  # Matches /api/todos/
]
