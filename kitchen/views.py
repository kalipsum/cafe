from django.shortcuts import render
from django.shortcuts import render_to_response
from kitchen.models import Menu, Dish, DishComponent, Ingredient, Basket
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import *
from django.db.models import Q
from kitchen.forms import Filter
from functools import reduce
import operator
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
    ingredients = Ingredient.objects.all()
    ingredients = Ingredient.objects.order_by('name').all()
    dish_items = Dish.objects.all()
    components_criteria = []
    if f.is_valid():
        name = f.cleaned_data['name']
        components = f.cleaned_data['ingredients']
        min_value = f.cleaned_data['min']
        max_value = f.cleaned_data['max']
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
            for item in components:
                components_criteria.append(Q(dishcomponent__ingredient__pk=item))
            dish_items = dish_items.filter(reduce(operator.and_, components_criteria))
            #components_criteria = Q()
            #for item in components:
             #   components_criteria.add(Q(dishcomponent__ingredient__pk=item), Q.AND)
            #dish_items = dish_items.filter(components_criteria)
        dish_items.all()
    filter_urls = []
    comp = []
    for item in ingredients:
        if str(item.pk) in components:
            comp.append(item.name)
        filter_urls.append({'title': item.name, 'url': build_filter_url(item.pk, f.cleaned_data)})
    return render_to_response('filter.html', {'f': f, 'menu_items': dish_items, 'ing': ingredients, 'filter_urls': filter_urls,'comp':comp})


def build_filter_url(component_id, request_data):
    """
    Function builds url for filter
    :param int component_id: id of ingredient function builds url for
    :param dict request_data: filter parameters from request
    :return str: new url for filter
    """
    filter_url = '/dish/filter?'
    components = request_data.get('ingredients', [])
    components = [int(i) for i in components]
    keys = (set(request_data.keys())-set(['ingredients']))
    result = [key + '=' + str(request_data[key]) for key in keys if request_data[key]]
    components_cleaned = (set(components) ^ set([component_id]))
    result.extend(['ingredients=' + str(item) for item in components_cleaned])

    return filter_url + '&'.join(result)


def basket(request):
    data = request.GET
    basket_items = Basket.objects.all()
    if 'remove' in request.GET:
        Basket.objects.filter(pk=data['remove']).delete()
    total_price = 0
    for item in basket_items:
        total_price += item.total
    return render_to_response('basket.html', {'basket': basket_items,'total': total_price})


def order(request):
    return render_to_response('order.html')


def basket_add(request):
    dish_items = Dish.objects.all()
    if request.method == 'GET':
        data = request.GET
        item_name = Dish.objects.get(pk=int(data['item']))
        dish_added = Basket.objects.filter(name=item_name.name).exists()
        if dish_added:
            item = Basket.objects.get(name=item_name.name)
            item.quantity += int(data['quantity'])
            item.total = item.price*item.quantity
            item.save()
        else:
            total_price = item_name.price*int(data['quantity'])
            basket_item = Basket(name=item_name.name, price=item_name.price, quantity=int(data['quantity']), total=total_price,)
            basket_item.save()
    return render_to_response('basket.html')

