from django.contrib import admin
from django.urls import path
from foodStuff import views

urlpatterns = [
    path('',views.index,name="homeFoodStuff"),

]
