from django.db import models
from baseFiles.models import BaseModel
# Create your models here.

class SubCategory(BaseModel):
    subCategoryName = models.CharField(max_length=100)
    subCategoryImage = models.ImageField()    

class Category(BaseModel):
    categoryName = models.CharField(max_length=100)
    categoryImage = models.ImageField()    

class Product(BaseModel):
    foodName = models.CharField(max_length=100)
    foodCategory = models.CharField(max_length=100)
    foodSubCategory = models.CharField( max_length=1000)
    product_description = models.TextField()
    price = models.IntegerField()
    #slug = models.SlugField(unique=True,null=True, blank=True)