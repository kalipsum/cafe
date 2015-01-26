from django.contrib import admin
from kitchen.models import Menu
from kitchen.models import Dish
from kitchen.models import Category
from kitchen.models import Ingredient
from kitchen.models import DishComponent
admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(DishComponent)
