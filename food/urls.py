from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.simple_upload,name='home'),
    path("api/",views.ListTodoAPIView.as_view(),name="todo_list"),
    # path('food/',views.food_list,name='foodlist'),
]