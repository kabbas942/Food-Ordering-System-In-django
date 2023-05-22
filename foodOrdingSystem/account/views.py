from django.shortcuts import render,HttpResponse

# Create your views here.

def signIn(request):
    return HttpResponse("signIn")

def signUp(request):
    return HttpResponse("signUp")

def signOut(request):
    return HttpResponse("signOut")
