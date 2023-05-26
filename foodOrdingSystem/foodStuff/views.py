from django.shortcuts import render,redirect
from foodStuff.models import *

# Create your views here.
def index(request):
    allData = FoodCategory.objects.all()    
    return render(request,"foodStuff/index.html",{'foodProduct':allData} )

def productFoodStuff(request,foodId):
    foodCategoryInfo = FoodCategory.objects.get(uid = foodId)
    allData = FoodProduct.objects.filter(foodCategory=foodCategoryInfo.uid)   
    return render(request,"foodStuff/foodProducts.html",{'foodProduct':allData,'categoryName': foodCategoryInfo.categoryName})

def contact(request):
    return render(request,"foodStuff/contact.html") 

def about(request):
    return render(request,"foodStuff/about.html") 

def search(request):
    if request.method == 'GET':
        query = request.GET.get('foodProductSearch')  # Get the search query from the request's GET parameters
        foodProductList = FoodProduct.objects.filter(foodName__icontains=query)  # Perform case-insensitive search on the 'name' field
        if foodProductList:
            foodProductList = foodProductList | FoodProduct.objects.filter(foodProductDescription__icontains=query)
            foodProductList = foodProductList | FoodProduct.objects.filter(foodCategory__categoryName__icontains=query)
            productParameter={'products':foodProductList,'search': query}
        else:
            foodProductList = FoodProduct.objects.filter(foodCategory__categoryName__icontains=query)
            productParameter={'foodProducts':foodProductList,'foodSearch': query}

                
              
        
        return render(request,"foodStuff/search.html",productParameter)
    return redirect("/foodStuff")

    return render(request,"foodStuff/about.html") 