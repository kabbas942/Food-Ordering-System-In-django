from django.shortcuts import render,redirect,HttpResponse
from foodStuff.models import *
from account.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import sessions
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

    

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

def foodCart(request,**kwargs):
    if request.session.get('item'):
        cartDictionary = request.session.get('item')
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)

        else:
            profile=123

        print(profile.mobileNumber)
        keyDict = request.session['item'].keys()
        keyList = [x for x in keyDict]        
        cartFoodPrice = []
        cartPriceDictionary = {}
        for key in keyList:
            foodPrice = cartDictionary.get(key) * FoodProduct.objects.get(uid = key).foodPrice
            cartPriceDictionary[key]=foodPrice
            cartFoodPrice.append(foodPrice)        
        cartProducts = {'foodProducts':FoodProduct.objects.filter(uid__in = keyList), 'foodDictionary':cartDictionary,'total':sum(cartFoodPrice),'productPriceList':cartPriceDictionary,'stripeKey':settings.STRIPE_PUBLISHABLE_KEY,'profile':profile}
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
    return redirect("/foodCart")

def placeOrder(request):
    if request.user.is_anonymous:
        return redirect('/account/signIn')   
    else:
        if request.method == 'POST':       
            userId = User.objects.get(id=request.user.id)
            row=Profile.objects.get(user=userId)
            shippingAddress=row.address
            mobileNumber=row.mobileNumber
            zipCode=row.zipCode
            orderPrice=0
            OrderNow= Order(customerId=userId,orderAddress=shippingAddress,orderZipCode=zipCode,orderMobileNumber=mobileNumber,orderPrice=orderPrice)
            OrderNow.save()
            orderPrice=0
            for productDetailId,Qty in request.session['item'].items(): 
                product= FoodProduct.objects.get(uid=productDetailId)          
                orderId = Order.objects.get(orderId = OrderNow.pk) 
                orderPrice=orderPrice+product.foodPrice
                OrderDetailNow = OrderDetail(productId=product, orderId=orderId, orderProductQuantity=Qty,productPrice=product.foodPrice)
                OrderDetailNow.save()
            
            OrderValue=Order.objects.get(orderId=orderId)
            OrderValue[orderPrice]=orderPrice
            OrderValue.save()

            token = request.POST.get('stripeToken')
            charge = stripe.Charge.create(amount=orderPrice,  # amount in cents
                        currency='usd',
                        source=token,
                        description='Order place Successfully'
                    )       
            session_key = 'item'  # Replace with the actual session key
            request.session['item'] = {}
            request.session['quantity'] = {}       
            return redirect("/foodStuff")    