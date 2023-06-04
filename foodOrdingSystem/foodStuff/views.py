from django.shortcuts import render,redirect,HttpResponse
from foodStuff.models import *
from django.contrib import sessions

# Create your views here.
def index(request):
    #request.session.flush()
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
        query = request.GET.get('foodProductSearch') 
        # Get the search query from the request's GET parameters
        foodProductList = FoodProduct.objects.filter(foodName__icontains=query)  # Perform case-insensitive search on the 'name' field        
        if foodProductList:
            foodProductList = foodProductList | FoodProduct.objects.filter(foodProductDescription__icontains=query)
            foodProductList = foodProductList | FoodProduct.objects.filter(foodCategory__categoryName__icontains=query)
            productParameter={'foodProduct':foodProductList,'foodSearch': query}
        else:
            foodProductList = FoodProduct.objects.filter(foodCategory__categoryName__icontains=query)
            productParameter={'foodProduct':foodProductList,'foodSearch': query}
        return render(request,"foodStuff/foodProducts.html",productParameter)
    return redirect("/foodStuff")

def foodDescription(request,foodId):
    productDescription = FoodProduct.objects.get(uid = foodId)
    return render(request,"foodStuff/foodDescription.html",{'productDescription':productDescription})

def addToCart(request):
    if request.method == "POST":
        foodId = str(request.POST.get("foodItemId"))
        foodItem = request.session.get('item')        
        if foodItem:
            quantity = foodItem.get(foodId)
            if quantity:
                foodItem[foodId] = quantity + 1
            else:
                foodItem[foodId] = 1
        else:
            foodItem = {} 
            foodItem[foodId] = 1      
        request.session['item']=foodItem
        totalCartQuantity = sum(request.session['item'].values())    
        request.session['quantity']=totalCartQuantity
    return redirect(request.META.get('HTTP_REFERER'))


def foodCart(request):
    if request.session.get('item'):
        cartDictionary = request.session.get('item')
        keyDict = request.session['item'].keys()
        keyList = [x for x in keyDict]        
        cartFoodPrice = []
        cartPriceDictionary = {}
        for key in keyList:
            foodPrice = cartDictionary.get(key) * FoodProduct.objects.get(uid = key).foodPrice
            cartPriceDictionary[key]=foodPrice
            cartFoodPrice.append(foodPrice)        
        cartProducts = {'foodProducts':FoodProduct.objects.filter(uid__in = keyList), 'foodDictionary':cartDictionary,'total':sum(cartFoodPrice),'productPriceList':cartPriceDictionary}
        return render(request,"foodStuff/foodCart.html",cartProducts)
    else:       
        return render(request,"foodStuff/foodCart.html")
    
    
def foodCartUpdateQty(request):
    if request.method=="POST":
        #get dictionary from cart quantity control
        for key, value in request.POST.items():
            if key.startswith('foodProductId_'):
                cartProductId=value   
               
            if key.startswith('foodUpdateQuantity_'):
               updateQuantity = value    
         #get session and store in cart                        
        cartValue = request.session.get('item')
        if cartValue:
           cartValue[cartProductId] =int(updateQuantity)                      
        request.session['item']=cartValue
        totalCartQuantity = sum(request.session['item'].values())
        request.session['quantity']=totalCartQuantity      
    return redirect("/foodStuff/foodCart")

def checkout(request):
    return HttpResponse("checkout")