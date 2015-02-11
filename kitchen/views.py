from django.shortcuts import render
from django.shortcuts import render_to_response
from kitchen.models import Menu, Dish, DishComponent, Ingredient
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import *
from django.db.models import Q
from kitchen.forms import Filter
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
    return render_to_response('menu.html', {'menu': menu_element, 'menu_list': menu_list, 'menu_items': values})


def filter_dishes(request):
    f = Filter(request.GET)
    if f.is_valid():
        name = f.cleaned_data['name']
        components = f.cleaned_data['ingredients']
        min_value = f.cleaned_data['min']
        max_value = f.cleaned_data['max']
        dish_items = Dish.objects.all()
        if name:
            dish_items = dish_items.filter(name__icontains=name)
        if min_value:
            dish_items = dish_items.filter(price__gte=min_value)
        if max_value:
            dish_items = dish_items.filter(price__lte=max_value)
        if components:
            for item in components:
                dish_items = dish_items.filter(dishcomponent__ingredient__pk=item)
            dish_items.all()
    return render_to_response('filter.html', {'f':f,'menu_items': dish_items})

