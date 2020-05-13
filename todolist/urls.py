from django.urls import path,re_path
from . import views as todo 
urlpatterns = [
    path('',todo.todoList,name='todoHome'),
    path('add-task',todo.addTask,name='addTask'),
    re_path(r"^complete/(?P<identity>[a-zA-Z]+)$",todo.complete,name='complete'),
    re_path(r"^delete/(?P<identity>[a-zA-Z]+)$",todo.delete,name='delete'),
]
 