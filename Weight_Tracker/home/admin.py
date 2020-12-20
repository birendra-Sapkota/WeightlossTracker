from django.contrib import admin

# Register your models here.

from django.contrib import admin
from home.models import Person, ConsumeFoodDetail, FoodDetail, Bmi

admin.site.register(Person)
admin.site.register(ConsumeFoodDetail)
admin.site.register(FoodDetail)
admin.site.register(Bmi)