import datetime
from hashlib import md5
from time import time
import random
from django.http import HttpResponse
from django.shortcuts import render_to_response
from cafe.pkg.orders.models import *
from cafe.pkg.kitchen.models import Dish


def basket(request):
    data = request.GET
    user = request.user
    basket_items = Basket.objects.all()
    if 'remove' in request.GET and Basket.objects.filter(pk=data['remove']).exists():
        element = Basket.objects.filter(pk=data['remove'])
        element.dish.cnt_in_store += element.quantity
        element.dish.count.count = element.dish.cnt_in_store
        element.dish.save()
        element.dish.count.save()
        element.delete()
    total = 0
    if 'id' in request.COOKIES:
        item = request.COOKIES['id']
        if request.user.is_anonymous():
            basket_items = Basket.objects.filter(customer__user_hash=item, customer__user=None, order=None)
        else:
            basket_items = Basket.objects.filter(customer__user=request.user, order=None)
        for item in basket_items:
            total += item.price
    else:
        basket_items = []
    return render_to_response('basket.html', {'basket': basket_items, 'total': total})


def order(request):
    total = 0
    if request.user.is_anonymous():
        basket_items = Basket.objects.filter(customer__user_hash=request.COOKIES['id'], customer__user=None)
    else:
        basket_items = Basket.objects.filter(customer__user=request.user)
    date = datetime.datetime.now()
    for item in basket_items:
        if item.order is None:
            total += item.price
    if request.user.is_anonymous():
        order_item = Order(date=date, status_name=OrderStatus.objects.get(pk=1), total=total,)
    else:
        order_item = Order(user=request.user, date=date, status_name=OrderStatus.objects.get(pk=1), total=total,)
    order_item.save()
    for item in basket_items:
        if item.order is None:
            item.order = Order.objects.get(pk=order_item.pk)
            item.save()
    basket_items = []
    return render_to_response('basket.html', {'basket': basket_items})


def orders(request):
    basket_items = Basket.objects.all()
    order_items = Order.objects.filter(user=request.user)
    items = []
    for item in order_items:
        dishes = Basket.objects.filter(order=item)
        items.append({'order': item, 'dishes': dishes})
    return render_to_response('order.html', {'items': items})


def clean(request):
    basket_items = Basket.objects.filter(customer__user_hash=request.COOKIES['id'])
    for item in basket_items:
        item.dish.cnt_in_store += item.quantity
        item.dish.count.count = item.dish.cnt_in_store
        item.dish.save()
        item.dish.count.save()
    basket_items.delete()
    return render_to_response('basket.html', {'basket': basket_items})


def basket_add(request):
    resp = HttpResponse()
    if 'id' in request.COOKIES:
        cookie_id = request.COOKIES['id']
        if request.user.is_anonymous():
            customer_item = Customer.objects.get(user_hash=cookie_id)
        else:
            customer_item = Customer.objects.get(user_hash=cookie_id, user=request.user)
    else:
        cookie_id = md5(('customer' + str(time()) + str(random.random())).encode('utf8')).hexdigest()
        resp.set_cookie('id', cookie_id)
        if request.user.is_anonymous():
            customer_item = Customer(user_hash=cookie_id,)
        else:
            customer_item = Customer(user_hash=cookie_id, user=request.user)
        customer_item.save()
    dish_items = Dish.objects.all()
    if request.method == 'GET':
        data = request.GET
        if Dish.objects.filter(pk=int(data['item'])).exists() and int(data['quantity']) > 0:
            item_dish = Dish.objects.get(pk=int(data['item']))
        else:
            return resp
        dish_added = Basket.objects.filter(dish=item_dish, order=None, customer__user_hash=customer_item.user_hash).exists()
        if dish_added:
            item = Basket.objects.get(dish=item_dish, order=None, customer__user_hash=customer_item.user_hash)
            price_item = item_dish.price
            item.quantity += int(data['quantity'])
            item.price = price_item*item.quantity
            item.save()
            item_dish.cnt_in_store -= int(data['quantity'])
            item_dish.save()
        else:
            total_price = item_dish.price*int(data['quantity'])
            if item_dish.cnt_in_store - int(data['quantity']) >= 0:
                basket_item = Basket(dish=item_dish, quantity=int(data['quantity']), price=total_price, customer=customer_item,)
            item_dish.cnt_in_store -= int(data['quantity'])
            item_dish.save()
            basket_item.save()
    return resp
