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


class Count(models.Model):
    count = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField(blank=True)
    menu = models.ForeignKey(Menu)
    category = models.ForeignKey(Category)
    cnt_in_store = models.IntegerField()
    count = models.ForeignKey(Count)

    def __str__(self):
        return self.name


def add_dishes(sender, instance, **kwargs):
    dish_item = Dish.objects.get(pk=instance.pk)
    dish_components = DishComponent.objects.filter(dish=dish_item)
    ing = False
    if instance.count.count < instance.cnt_in_store:
        for item in dish_components:
            weight = item.weight*(instance.cnt_in_store - instance.count.count)
            if item.ingredient.weight_in_store - weight >= 0:
                item.ingredient.weight_in_store -= weight
                item.ingredient.save()
            else:
                ing = True
                break
        if ing:
            return('Not enought ingredients')
    instance.count.count = instance.cnt_in_store
    instance.count.save()


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
