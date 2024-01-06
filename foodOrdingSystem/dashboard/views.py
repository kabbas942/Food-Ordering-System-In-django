from django.shortcuts import render,HttpResponse
from account.decorator import allowed_users
# Create your views here.

@allowed_users(allowed_roles=['Admin'])
def index(request):
    return render(request,"dashboard/index.html")