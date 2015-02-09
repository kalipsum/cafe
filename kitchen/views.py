from django.shortcuts import render
from django.shortcuts import render_to_response
from kitchen.models import Menu, Dish, DishComponent, Ingredient
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import *
from django.db.models import Q
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
    ing = Ingredient.objects.all()
    components = request.GET.getlist('component[]', [])
    query_param = {}
    qn = ''
    qmin = '0'
    qmax = '100'
    if 'name' in request.GET and request.GET['name']:
        query_param['name'] = request.GET['name']
    if 'component[]' in request.GET and request.GET.getlist('component[]'):
        query_param['component'] = request.GET.getlist('component[]')

    if 'min' in request.GET and request.GET.getlist('min'):
        query_param['min'] = request.GET['min']

    if 'min' in request.GET and request.GET.getlist('min'):
        query_param['max'] = request.GET['max']

    dish_items = Dish.objects.all()
    if 'name' in query_param:
        qn = query_param['name']
        dish_items = dish_items.filter(name__icontains=query_param['name'])
    if 'min' in query_param:
        qmin = query_param['min']
        dish_items = dish_items.filter(price__gte=query_param['min'])
    if 'max' in query_param:
        qmax = query_param['max']
        dish_items = dish_items.filter(price__lte=query_param['max'])


    qcomp = []
    components_criteria = []
    if 'component' in query_param:
       # for item in query_param['component']:
       #    components_criteria.append(Q(dishcomponent__ingredient__pk=item))
    #dish_items = dish_items.filter(*components_criteria).all()

        for item in query_param['component']:
            dish_items = dish_items.filter(dishcomponent__ingredient__pk=item)
            qcomp.append(int(item))
        dish_items.all()
    return render_to_response('filter.html', {'ing': ing, 'dish_items': dish_items, 'qn': qn, 'qmax': qmax, 'qmin': qmin, 'qcomp': qcomp})

