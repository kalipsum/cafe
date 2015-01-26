from django.db import models

# Create your models here.


class Menu(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return 'Menu'


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Dish(models.Model):
    dish_name = models.CharField(max_length=70)
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField(blank=True)
    menu_ID = models.ForeignKey(Menu)
    category_ID = models.ForeignKey(Category)

    def __str__(self):
        return self.dish_name


class Ingredient(models.Model):
    ing_name = models.CharField(max_length=30)

    def __str__(self):
        return self.ing_name


class DishComponent(models.Model):
    dish_ID = models.ForeignKey(Dish)
    ingredient_ID = models.ForeignKey(Ingredient)
    weight = models.FloatField()




