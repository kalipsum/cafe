import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from cafe.pkg.kitchen.models import Dish, Menu, Category, Count
from cafe.pkg.orders.models import Order, OrderStatus, Customer, Basket


# Create your tests here.


class OrderTests(TestCase):
    def setUp(self):
        menu1 = Menu.objects.create(name="day", date=datetime.datetime.now())
        category = Category.objects.create(name='starters')
        cnt1 = Count.objects.create(count=200)
        cnt2 = Count.objects.create(count=300)
        dish1 = Dish.objects.create(name='pizza', price=3, image='some_src', menu=menu1, category=category,
                                    cnt_in_store=200, count=cnt1)
        dish2 = Dish.objects.create(name='potato', price=3, image='some_src', menu=menu1, category=category,
                                    cnt_in_store=300, count=cnt2)
        dish3 = Dish.objects.create(name='ice-cream', price=1, image='some_src', menu=menu1, category=category,
                                    cnt_in_store=300, count=cnt2)
        OrderStatus.objects.create(status_name='in progress')
        OrderStatus.objects.create(status_name='delivery')
        OrderStatus.objects.create(status_name='closed')
        user1 = User.objects.create(username='user1', password='password')
        customer = Customer.objects.create(user=user1, user_hash='some_hash')
        Basket.objects.create(dish=dish1, quantity=2, price=20, customer=customer)
        Basket.objects.create(dish=dish2, quantity=3, price=10, customer=customer)
        Basket.objects.create(dish=dish3, quantity=1, price=30, customer=customer)

    def test_should_return_200(self):
        params = {'item': '2', 'quantity': '2'}
        response = self.client.get('/add/basket/', params)
        self.assertEqual(response.status_code, 200)

    def test_should_return_cookie(self):
        params = {'item': '2', 'quantity': '3'}
        response = self.client.get('/add/basket/', params)
        self.assertIn('id', response.client.cookies.keys())

    def test_adding_item_should_create_record_in_table(self):
        params = {'item': '2', 'quantity': '1'}
        response = self.client.get('/add/basket/', params)
        dish = Dish.objects.get(pk=params['item'])
        result = Basket.objects.filter(dish=dish, quantity=params['quantity']).exists()
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
        dish = Dish.objects.get(pk=params['item'])
        for item in Basket.objects.all():
            print(item.dish)
            print(item.quantity)
        result = Basket.objects.filter(dish=dish, quantity=int(params['quantity'])+int(other_params['quantity'])).exists()
        self.assertTrue(result)

    def test_should_have_unique_items(self):
        params = {'item': '1', 'quantity': '12'}
        response = self.client.get('/add/basket/', params)
        other_params = {'item': '1', 'quantity': '8'}
        response = self.client.get('/add/basket/', other_params)
        dish = Dish.objects.get(pk=params['item'])
        result = Basket.objects.filter(dish=dish, customer__user_hash=response.client.cookies['id'].value).count()

        self.assertEquals(result, 1)

    def test_should_remove_item_from_basket(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        item = 2
        delete_params = {'remove': item}
        response = self.client.get('/basket/', delete_params)
        result = Basket.objects.filter(pk=item, customer__user_hash=response.client.cookies['id'].value).exists()
        self.assertFalse(result)

    def test_should_not_create_basket_item_if_dish_does_not_exist_or_quantity_is_negative(self):
        params = {'item': '6', 'quantity': '10'}
        response = self.client.get('/add/basket/', params)
        result = Basket.objects.filter(pk=params['item']).exists()
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
        delete_params = {'remove': 2}
        response = self.client.get('/basket/', delete_params)
        self.assertEquals(response.context['total'], 40)

    def test_should_return_user_basket(self):
        params = {'item': '2', 'quantity': '12'}
        response = self.client.get('/add/basket/', params)
        a = response.client.cookies
        dish = Dish.objects.get(pk=params['item'])
        result = Basket.objects.filter(dish=dish, customer__user_hash=a['id'].value).count()
        self.assertEquals(result, 1)

    def test_should_not_remove_from_basket_if_item_does_not_exist(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        res = Basket.objects.all().count()
        item = 10
        delete_params = {'remove': item}
        response = self.client.get('/basket/', delete_params)
        result = Basket.objects.all().count()
        self.assertEquals(result, res)

    def test_should_clean_basket(self):
        params1 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        params2 = {'item': '3', 'quantity': '10'}
        response = self.client.get('/add/basket/', params2)
        response = self.client.get('/clean/basket/')
        a = response.client.cookies
        basket_items = Basket.objects.filter(customer__user_hash=a['id'].value).count
        self.assertTrue(basket_items, 0)
