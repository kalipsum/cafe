from django.db import models

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

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DishComponent(models.Model):
    dish = models.ForeignKey(Dish)
    ingredient = models.ForeignKey(Ingredient)
    weight = models.FloatField()




