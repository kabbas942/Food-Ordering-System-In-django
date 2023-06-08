from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib import messages
from account.modelForm import accountForm,extendedAccountForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.forms.models import model_to_dict

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
        return render(request,"account/signIn.html")
    else:
        return render(request,"account/signUp.html")       
    return render(request,"account/signUp.html")

def userProfile(request):    
    if request.user.is_authenticated:         
        userData = User.objects.get(id=request.user.id)
        profileData = Profile.objects.get(user =request.user.id )
        if request.method == 'POST':
            #Record = Profile.objects.get(id=userProfileId)
            form = accountForm(request.POST, instance=userData)
            extended_form = extendedAccountForm(request.POST)
            if form.is_valid() and extended_form.is_valid():
                form.save()
                extended_user = extended_form.save(commit=False)
                extended_user.user = userData
                extended_user.save()
                return redirect('home')
        else:
            #Record = Profile.objects.get(id=userProfileId) 
            form = accountForm(instance=userData)
            extended_form = extendedAccountForm(initial=model_to_dict(profileData))
            dic = {'form':form,"extended_form": extended_form}
            return render(request,"account/profile.html", dic)
    return redirect("/foodStuff")


def ordersProfile(request):
    #return render(request,"ordersProfile.html")
    return HttpResponse("ordersProfile")

def addressProfile(request):
    #return render(request,"addressProfile.html")
    return HttpResponse("addressProfile")


def passwordReset(request):
    #return render(request,"passwordReset.html")
    return HttpResponse("passwordReset")





           
           