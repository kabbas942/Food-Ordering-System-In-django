from django.shortcuts import render,HttpResponse
from account.decorator import allowed_users
from account.models import Profile
from django.contrib.auth.models import User
from foodStuff.models import FoodProduct,FoodCategory,Order,OrderDetail
from itertools import chain
# Create your views here.

@allowed_users(allowed_roles=['Admin'])
def index(request):
    users=User.objects.all()
    product = FoodProduct.objects.all()
    productCategories = FoodCategory.objects.all()
    foodOrder = Order.objects.all()
    productSold = OrderDetail.objects.all()
    lists=[]
    distinctProduct=[list(tup) for tup in OrderDetail.objects.values_list('productId').distinct()]
    distinctProduct=list(chain(*distinctProduct)) #convert [[],[],[]] to [,,]
    count = {FoodProduct.objects.get(pk=item).foodName:len(OrderDetail.objects.filter(productId=item)) for item in distinctProduct}
    maximum = max(count,key=count.get)
    maximum ={maximum:max(count.values())}
    info = {'Product':product,'Categories':productCategories,'Order':foodOrder,'users':users,'productSold':productSold,'mostProduct':maximum}
    return render(request,"dashboard/index.html",info)