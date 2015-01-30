from django.shortcuts import render
from django.shortcuts import render_to_response
from kitchen.models import Menu, Dish, DishComponent,Ingredient
from django.http import HttpResponse
# Create your views here.


def menu(request):
    dish_list = Dish.objects.all()
    menu_list = Menu.objects.all()
    return render_to_response('menu.html', {'menu_list': menu_list})


def dish(request, dish_id):
    dish_list = Dish.objects.all()
    menu_list = Menu.objects.all()
    dish_element = Dish.objects.get(id=dish_id)
    values = DishComponent.objects.filter(dish=dish_element).select_related()
    return render_to_response('dish.html', {'dish': dish_element, 'dish_list': dish_list, 'values': values, 'menu_list': menu_list})

def menu_items(request, menu_id):
    menu_list = Menu.objects.all()
    menu_element = Menu.objects.get(id=menu_id)
    values = Dish.objects.filter(menu=menu_element)
    return render_to_response('menu.html', {'menu': menu_element, 'menu_list': menu_list,'menu_items': values})
