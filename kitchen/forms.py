from django import forms
from kitchen.models import Ingredient
from django.utils.safestring import mark_safe

ingredient = Ingredient.objects.all()
a = [(item.pk, item.name, ) for item in ingredient]


class Filter(forms.Form):
    name = forms.CharField(min_length=3, max_length=30, required=False)
    ingredients = forms.MultipleChoiceField(
        choices=a,
        widget=forms.MultipleHiddenInput,
        required=False
    )
    min = forms.FloatField(required=False)
    max = forms.FloatField(required=False)


