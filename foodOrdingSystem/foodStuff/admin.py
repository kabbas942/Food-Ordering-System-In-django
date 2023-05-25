from django.contrib import admin
from foodStuff.models import *

# Register your models here.
admin.site.register([FoodCategory,
FoodProduct,
FoodCart])
