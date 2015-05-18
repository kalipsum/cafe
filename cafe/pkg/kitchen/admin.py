from django.contrib import admin

from cafe.pkg.kitchen.models import Menu
from cafe.pkg.kitchen.models import Dish
from cafe.pkg.kitchen.models import Category
from cafe.pkg.kitchen.models import Ingredient
from cafe.pkg.kitchen.models import DishComponent, Count

admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(DishComponent)
admin.site.register(Count)
