from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateTimeField()

    def __str__(self):
        return 'Menu' + ' - ' + self.name + '/' + self.date.strftime('%m/%d/%Y')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField(blank=True)
    menu = models.ForeignKey(Menu)
    category = models.ForeignKey(Category)
    cnt_in_store = models.IntegerField()

    def __str__(self):
        return self.name


def add_dishes(self, dish_id, count, **kwargs):
        dish_item = Dish.objects.get(pk=dish_id)
        dish_components = DishComponent.objects.filter(dish=dish_id)
        luck = False
        for item in dish_components:
            weight = dish_components.weight*count
            if dish_components.ingredient.weight_in_store - weight >= 0:
                dish_components.ingredient.weight_in_store -= weight
                dish_components.ingredient.weight_in_store.save()
            else:
                luck = True
                break
        if luck:
            add_dishes(self, dish_id, count-1)
        else:
            dish_item.cnt_in_store += count

post_save.connect(add_dishes, sender=Dish, dispatch_uid="update_ingredients")


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    weight_in_store = models.IntegerField()

    def __str__(self):
        return self.name


class DishComponent(models.Model):
    dish = models.ForeignKey(Dish)
    ingredient = models.ForeignKey(Ingredient)
    weight = models.FloatField()
