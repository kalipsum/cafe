import datetime
from django.test import TestCase
from cafe.pkg.kitchen.views import build_filter_url
from cafe.pkg.kitchen.models import Dish, Menu, Category, DishComponent, Ingredient, Count


# Create your tests here.


class KitchenTests(TestCase):

    def setUp(self):
        menu1 = Menu.objects.create(name="day", date=datetime.datetime.now())
        category = Category.objects.create(name='starters')
        cnt1 = Count.objects.create(count=200)
        cnt2 = Count.objects.create(count=300)
        dish1 = Dish.objects.create(name='potato', price=10, image='some src', menu=menu1, category=category,
                            cnt_in_store=300, count=cnt2)
        dish = Dish.objects.create(name='pizza', price=50, image='some src', menu=menu1, category=category,
                                   cnt_in_store=200, count=cnt1)
        ingredient1 = Ingredient.objects.create(name='chicken', weight_in_store=5000)
        ingredient2 = Ingredient.objects.create(name='mushrooms', weight_in_store=10000)
        DishComponent.objects.create(dish=dish, ingredient=ingredient1, weight=5)
        DishComponent.objects.create(dish=dish, ingredient=ingredient2, weight=10)

    def test_should_return_name_param(self):
        request_data = {'name': 'foo'}
        component_id = 1
        result = build_filter_url(component_id, request_data)
        self.assertIn('name=', result)

    def test_should_return_min_param(self):
        request_data = {'min': 'foo'}
        component_id = 1
        result = build_filter_url(component_id, request_data)
        self.assertIn('min=', result)

    def test_should_return_max_param(self):
        request_data = {'max': 'foo'}
        component_id = 1
        result = build_filter_url(component_id, request_data)
        self.assertIn('max=', result)

    def test_should_return_component_id_if_not_in_request(self):
        request_data = {}
        component_id = 4
        result = build_filter_url(component_id, request_data)
        self.assertIn('ingredients='+str(component_id), result)

    def test_should_not_return_component_id_if_in_request(self):
        request_data = {'ingredients': [5]}
        component_id = 5
        result = build_filter_url(component_id, request_data)
        self.assertNotIn('ingredients='+str(component_id), result)

    def test_should_return_all_ingredients(self):
        request_data = {'ingredients': [5, 4]}
        component_id = 1
        result = build_filter_url(component_id, request_data)
        self.assertIn('ingredients='+'5', result)
        self.assertIn('ingredients='+'4', result)

    def test_should_return_expected_dishes_list_if_max_set(self):
        params = {'max': 10}
        query_params = {'price__lte': params['max']}
        self.dish_list( query_params, params)

    def test_should_return_expected_dishes_list_if_min_set(self):
        params = {'min': 10}
        query_params = {'price__gte': params['min']}
        self.dish_list(query_params, params)

    def test_should_return_expected_dishes_list_if_name_set(self):
        params = {'name': 'potato'}
        query_params = {'name': params['name']}
        self.dish_list(query_params, params)

    def test_should_return_expected_dishes_list_if_ingredients_set (self):
        params = {'ingredients': [1, 2]}
        self.ingredient_list(params['ingredients'], params)

    def test_should_return_expected_dishes_list(self):
        params = {'name': 'pizza', 'min': 3, 'max': 12, 'ingredients': [1, 2]}
        query_params = {'price__lte': params['max'], 'price__gte': params['min'], 'name': params['name']}
        self.dish_list(query_params, params)
        self.ingredient_list(params['ingredients'], params)

    def dish_list(self, query_params, params):
        response = self.client.get('/dish/filter/', params)
        result = response.context['menu_items']
        final = []
        for item in result:
            final.append(item.pk)
        dish_count = Dish.objects.filter(pk__in=final, **query_params).count()
        self.assertEqual(dish_count, len(set(final)))

    def ingredient_list(self, ingredients,params):
        for item in ingredients:
            query_params = {'dishcomponent__ingredient__pk': item}
            self.dish_list(query_params, params)

    def test_should_increase_count(self):
        dish = Dish.objects.get(pk=1)
        dish.cnt_in_store = 500
        dish.save()
        self.assertEquals(dish.count.count, 500)

    def test_should_decrease_ingredient_weight(self):
        dish = Dish.objects.get(pk=2)
        dish_items = DishComponent.objects.filter(dish=dish)
        dish.cnt_in_store = 201
        for item in dish_items:
            ingredient_weight = item.ingredient.weight_in_store - (dish.cnt_in_store-dish.count.count)*item.weight
            dish.save()
            self.assertEquals(ingredient_weight, DishComponent.objects.get(ingredient=item.ingredient).ingredient.weight_in_store)

    def test_should_decrease_dish_count(self):
        params = {'item': '1', 'quantity': '10'}
        count = Dish.objects.get(pk=params['item']).count.count - int(params['quantity'])
        response = self.client.get('/add/basket/', params)
        self.assertEquals(count, Dish.objects.get(pk=params['item']).count.count)

    def test_should_increase_count_if_item_was_removed(self):
        params1 = {'item': '1', 'quantity': '10'}
        response = self.client.get('/add/basket/', params1)
        params2 = {'item': '2', 'quantity': '10'}
        response = self.client.get('/add/basket/', params2)
        count1 = Dish.objects.get(pk=params1['item']).count.count
        count2 = Dish.objects.get(pk=params2['item']).count.count
        response = self.client.get('/clean/basket/')
        self.assertEquals(count1 + int(params1['quantity']), Dish.objects.get(pk=params1['item']).count.count)
        self.assertEquals(count2 + int(params2['quantity']), Dish.objects.get(pk=params2['item']).count.count)