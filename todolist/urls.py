from django.urls import path,re_path
from . import views as todo 
urlpatterns = [
    path('',todo.todoList,name='todoHome'),
    path('add-task',todo.addTask,name='addTask'),
    re_path(r"^complete/(?P<identity>[a-zA-Z0-9!@#$%^&*()_+=<>/?'';-.:/]+)$",todo.complete,name='complete'),
    re_path(r"^delete/(?P<identity>[a-zA-Z0-9!@#$%^&*()-_+=;:''<>,.?/]+)$",todo.delete,name='delete'),
]
 