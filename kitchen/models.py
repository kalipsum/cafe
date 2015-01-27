from django.db import models

# Create your models here.


class Menu(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return 'Menu' + '/' + self.date.strftime('%m/%d/%Y')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField(blank=True)
    menu_id = models.ForeignKey(Menu)
    category_id = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DishComponent(models.Model):
    dish_id = models.ForeignKey(Dish)
    ingredient_id = models.ForeignKey(Ingredient)
    weight = models.FloatField()




