from django.db import models
from baseFiles.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.
class FoodCategory(BaseModel): 
    categoryName = models.CharField(max_length=100)
    categoryImage = models.ImageField(upload_to="Category")
  
    def __str__(self):
        return self.categoryName
 
class FoodProduct(BaseModel):
    foodName = models.CharField(max_length=100)
    foodCategory = models.ForeignKey(FoodCategory,on_delete=models.CASCADE,related_name="foodCategory",null=True,blank=True)    
    foodProductDescription = models.TextField()
    foodPrice = models.IntegerField()
    foodProductImage = models.ImageField(upload_to="foodProduct")
    #slug = models.SlugField(unique=True,null=True, blank=True)
    def __str__(self):
        return self.foodName


class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(User,on_delete=models.CASCADE,related_name="order",null=True,blank=True)
    orderAddress = models.CharField(max_length=500)
    orderCountry= models.CharField(max_length=52)
    orderState= models.CharField(max_length=52)
    orderZipCode= models.CharField(max_length=52)
    orderMobileNumber = models.IntegerField(default="")
    orderPrice = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.customerId)
    
class OrderDetail(models.Model):
    orderDetailId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(FoodProduct,on_delete=models.CASCADE,related_name="productOrderId",null=True,blank=True)
    orderId = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="orderDetailId",null=True,blank=True)
    orderProductQuantity = models.IntegerField(default=0)
    productPrice = models.IntegerField(default=0)
    def __str__(self):
        return str(self.orderId)
    
    
    
    
    
