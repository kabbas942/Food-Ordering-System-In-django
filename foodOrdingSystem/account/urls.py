from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('signIn',views.signIn,name="signIn"),
    path('signUp',views.signUp,name="signUp"),
    path('signOut',views.signOut,name="signOut"),
]
