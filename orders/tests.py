from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from kitchen.models import Dish, Menu, Category
from orders.models import Basket, Customer, Order,OrderStatus
from django.shortcuts import HttpResponse
import datetime
# Create your tests here.


class OrderTests(TestCase):
    def setUp(self):
        menu1 = Menu.objects.create(name="day", date=datetime.datetime.now())
        category = Category.objects.create(name='starters')
        Dish.objects.create(name='pizza', price=3, image='some_src', menu=menu1, category=category)
        Dish.objects.create(name='potato', price=3, image='some_src', menu=menu1, category=category)
        Dish.objects.create(name='ice-cream', price=1, image='some_src', menu=menu1, category=category)
        OrderStatus.objects.create(status_name='in progress')


    def test_should_return_ok_response(self):
        params = {'item': '2', 'quantity': '2'}
        response = self.client.get('/add/basket/', params)
        self.assertEqual(response.status_code, 200)

    def test_should_return_cookie(self):
        params = {'item': '2', 'quantity': '3'}
        response = self.client.get('/add/basket/', params)
        self.assertIn('id', response.client.cookies.keys())

    def test_should_check_if_basket_object_created(self):
        params = {'item': '2', 'quantity': '1'}
        response = self.client.get('/add/basket/', params)
        dish = Dish.objects.get(pk=2)
        result = Basket.objects.filter(dish=dish, quantity=1).exists()
        self.assertTrue(result)

    def test_gets_customer_if_cookies_are_set(self):
        params = {'item': '2', 'quantity': '3'}
        response = self.client.get('/add/basket/', params)
        response = self.client.get('/add/basket/', params)
        customer = Customer.objects.filter(user_hash=response.client.cookies['id'].value).exists()
        self.assertTrue(customer)

    def test_creates_customer_if_cookies_are_not_set(self):
        params = {'item': '2', 'quantity': '3'}
        response = self.client.get('/add/basket/', params)
        hash_item = response.client.cookies['id'].value
        customer = Customer.objects.filter(user_hash=hash_item).exists()
        self.assertTrue(customer)

    def test_should_increase_quantity_if_item_already_exist(self):
        params = {'item': '1', 'quantity': '12'}
        response = self.client.get('/add/basket/', params)
        other_params = {'item': '1', 'quantity': '8'}
        response = self.client.get('/add/basket/', other_params)
        dish = Dish.objects.get(pk=1)
        result = Basket.objects.filter(dish=dish,quantity=20).exists()
        self.assertTrue(result)

    def test_should_remove_item_from_basket(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        delete_params = {'remove': 2}
        response = self.client.get('/basket/', delete_params)
        result = Basket.objects.filter(pk=2, customer__user_hash=response.client.cookies['id'].value).exists()
        self.assertFalse(result)

    def test_if_order_was_created(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        response1 = self.client.get('/make/orders/')
        result = Order.objects.filter(pk=1).exists()
        self.assertTrue(result)


    def test_total_price_of_basket(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        params2 = {'item': '3', 'quantity': '10'}
        response = self.client.get('/add/basket/', params2)
        delete_params = {}
        response = self.client.get('/basket/', delete_params)
        self.assertEquals(response.context['total'], 40)

    def test_total_price_if_item_was_removed(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        params2 = {'item': '3', 'quantity': '10'}
        response = self.client.get('/add/basket/', params2)
        delete_params = {'remove': 1}
        response = self.client.get('/basket/', delete_params)
        self.assertEquals(response.context['total'], 10)













