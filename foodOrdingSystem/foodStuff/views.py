from django.shortcuts import render
from foodStuff.models import *

# Create your views here.
def index(request):
    allData = FoodCategory.objects.all()    
    return render(request,"foodStuff/index.html",{'foodProduct':allData} )

def productFoodStuff(request,foodId):
    foodCategoryInfo = FoodCategory.objects.get(uid = foodId)
    allData = FoodProduct.objects.filter(foodCategory=foodCategoryInfo.uid)   
    return render(request,"foodStuff/foodProducts.html",{'foodProduct':allData,'categoryName': foodCategoryInfo.categoryName} )
    