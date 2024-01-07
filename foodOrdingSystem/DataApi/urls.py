from django.contrib import admin
from django.urls import path
from DataApi import views

urlpatterns = [
    path('',views.lists,name="dashboard"),
]