from django.test import TestCase
from kitchen.views import build_filter_url

# Create your tests here.


class KitchenTests(TestCase):
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
        request_data = {'ingredients':[5]}
        component_id = 5
        result = build_filter_url(component_id, request_data)
        self.assertNotIn('ingredients='+str(component_id), result)

    def test_should_return_all_ingredients(self):
        request_data = {'ingredients':[5,4]}
        component_id = 1
        result = build_filter_url(component_id, request_data)
        self.assertIn('ingredients='+'5', result)
        self.assertIn('ingredients='+'4', result)

