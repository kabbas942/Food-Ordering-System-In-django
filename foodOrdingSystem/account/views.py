from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model

# Create your views here.

def signIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        userPassword = request.POST.get('password')
        accountData =authenticate(username=username, password=userPassword) 
        print(accountData)
        if accountData is not None:
            login(request,accountData)
            return redirect('/foodStuff')
        else:
            messages.warning(request, "Email Or Password is Invalid")
            return render(request,'account/signIn.html')
    return render(request,"account/signIn.html")


def signOut(request):
    #logout(request)
    return HttpResponse("Logout")

def signUp(request):
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        password= request.POST.get("password")
        getUserModel=get_user_model()
        createUser = getUserModel.objects.create_user(first_name = name, username=email, password=password)
        createUser.save()
        messages.success(request, "Foodia Account Created Successfully")
        return render(request,"foodStuff/index.html")
    else:
        return render(request,"account/signUp.html")       
    return render(request,"account/signUp.html")



