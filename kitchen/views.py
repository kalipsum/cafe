from django.shortcuts import render
from django.shortcuts import render_to_response
from kitchen.models import Menu, Dish, DishComponent,Ingredient
from django.http import HttpResponse
# Create your views here.


def menu(request):
    dish_list = Dish.objects.all()
    return render_to_response('menu.html', {'dish_list': dish_list})

