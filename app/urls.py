from django.urls import path
from .views import TodosListView, TodosCreateView
from . import views


urlpatterns = [
    path("", TodosListView.as_view(), name='todo-home'),
    path("todo/create/", TodosCreateView.as_view(), name='todo-create'),
    path("delete/<int:todo_id>/", views.todo_delete, name="todo-delete"),
    path("todo/update/<int:todo_id>/", views.todo_update, name="todo-update"),
]
