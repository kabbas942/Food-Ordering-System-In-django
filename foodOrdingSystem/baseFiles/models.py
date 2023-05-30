from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now_add=True)
    
    class  Meta:
        abstract = True
        
        
'''def cart(request):
    if request.method=="POST":
        cartId = int(request.POST.get("cartId"))        
        cartValue = request.session.get('cart')
        if cartValue:
            quantity = cartValue.get(cartId)
            if quantity:
                cartValue[cartId] = quantity + 1
            else:
                cartValue[cartId] = 1
        else:
            cartValue = {} 
            cartValue[cartId] = 1  
        request.session['cart']=cartValue
        totalCartQuantity = sum(request.session['cart'].values())    
        request.session['quantity']=totalCartQuantity
        return redirect(request.META.get('HTTP_REFERER'))'''