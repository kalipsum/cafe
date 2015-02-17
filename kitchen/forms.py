from django import forms
from kitchen.models import Ingredient

ingredient = Ingredient.objects.all()
a = []
for item in ingredient:
    a.append((item.pk, item.name,))


class Filter(forms.Form):
    name = forms.CharField(min_length=3, max_length=30, required=False)
    ingredients = forms.MultipleChoiceField(
        choices=a,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    min = forms.FloatField(required=False)
    max = forms.FloatField(required=False)

