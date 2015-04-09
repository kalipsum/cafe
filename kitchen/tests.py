from django.test import TestCase
from kitchen.views import build_filter_url
from kitchen.models import Dish,Menu,Category,DishComponent,Ingredient
import datetime

# Create your tests here.


class KitchenTests(TestCase):

    def setUp(self):
        menu1 = Menu.objects.create(name="day", date=datetime.datetime.now())
        category = Category.objects.create(name='starters')
        Dish.objects.create(name='potato', price=10, image='some src', menu=menu1, category=category)
        dish = Dish.objects.create(name='pizza', price=50, image='some src', menu=menu1, category=category)
        ingredient1 = Ingredient.objects.create(name='chicken')
        ingredient2 = Ingredient.objects.create(name='mushrooms')
        DishComponent.objects.create(dish=dish, ingredient=ingredient1, weight=5)
        DishComponent.objects.create(dish=dish, ingredient=ingredient2, weight=5)

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
