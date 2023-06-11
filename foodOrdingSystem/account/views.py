from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from account.models import Profile
from foodStuff.models import *
from django.contrib import messages
from account.modelForm import AccountForm,extendedAccountForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# Create your views here.

def signIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        userPassword = request.POST.get('password')
        accountData =authenticate(username=username, password=userPassword) 
        if accountData is not None:
            login(request,accountData)
            return redirect('/foodStuff')
        else:
            messages.warning(request, "Email Or Password is Invalid")
            return render(request,'account/signIn.html')
    return render(request,"account/signIn.html")


def signOut(request):
    logout(request)
    return redirect('/account/signIn')

def signUp(request):
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        password= request.POST.get("password")
        getUserModel=get_user_model()
        createUser = getUserModel.objects.create_user(first_name = name, username=email, password=password)
        createUser.save()
        messages.success(request, "Foodia Account Created Successfully")
        return render(request,"account/signIn.html")
    else:
        return render(request,"account/signUp.html")       
    return render(request,"account/signUp.html")
@login_required
def userProfile(request):    
    if request.user.is_authenticated:         
        userData = User.objects.get(id=request.user.id)
        if request.method == 'POST':
            form = AccountForm(request.POST, instance=userData)
            if form.is_valid():
                form.save(commit=True)
                return redirect('/account/profile')
        else:
            form = AccountForm(instance=userData)
            return render(request,"account/profile.html", {'form':form})
    return redirect("/foodStuff")


def ordersProfile(request):    
    if request.user.is_authenticated:
        productDic={}
        orders = Order.objects.filter(customerId =request.user.id)      
        ordersIdList = [item.orderId for item in orders]  
        for itemNumber in ordersIdList:    
            productList = OrderDetail.objects.filter(orderId = itemNumber)
            productDic[itemNumber] =  productList       
        return render(request,"account/ordersProfile.html",{"orders":orders,"orderDetail":productDic})
    return render(request,"account/signIn.html")

def addressProfile(request):
        if request.user.is_authenticated:         
            profileData = Profile.objects.get(user =request.user.id )
            if request.method == 'POST':
                form = extendedAccountForm(request.POST, instance=profileData)
                if form.is_valid():
                    form.save(commit=True)
                    return redirect('/account/profile')
            else:
                form = extendedAccountForm(initial=model_to_dict(profileData))
                return render(request,"account/addressProfile.html", {'form':form})
        return redirect("/foodStuff")
    #return render(request,"addressProfile.html")



def resetPassword(request):    
    return render(request,"account/resetPassword.html")









           
           