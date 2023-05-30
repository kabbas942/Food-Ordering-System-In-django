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
