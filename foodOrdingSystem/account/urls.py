from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('signIn',views.signIn,name="signIn"),
    path('signUp',views.signUp,name="signUp"),
    path('signOut',views.signOut,name="signOut"),
    path('profile',views.userProfile,name="userProfile"),
    path('ordersProfile',views.ordersProfile,name="ordersProfile"),
    path('addressProfile',views.addressProfile,name="addressProfile"), 
    path('resetPassword',views.resetPassword,name="passwordReset"),
    path('baseProfile',views.baseProfile),
]
