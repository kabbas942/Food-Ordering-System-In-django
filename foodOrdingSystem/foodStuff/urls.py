from django.contrib import admin
from django.urls import path
from foodStuff import views

urlpatterns = [
    path('',views.index,name="homeFoodStuff"),
    path('productFoodStuff/<foodId>',views.productFoodStuff,name="productFoodStuff"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('foodSearch',views.search,name="foodSearch"),
    path('foodDescription/<foodId>',views.foodDescription,name="foodDescription"),

]
