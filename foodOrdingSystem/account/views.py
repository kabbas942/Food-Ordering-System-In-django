from django.shortcuts import render,HttpResponse

# Create your views here.

def signIn(request):
    return render(request,"account/signIn.html")

def signUp(request):
    return render(request,"account/signUp.html")

def signOut(request):
    return HttpResponse("Logout")
