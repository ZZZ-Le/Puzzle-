from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),  # 添加这一行
]