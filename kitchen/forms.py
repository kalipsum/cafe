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
    min = forms.FloatField(required=False, min_value=0)
    max = forms.FloatField(required=False, min_value=0)

    def clean(self):
        cleaned_data = super(Filter, self).clean()
        min_price = cleaned_data.get("min")
        max_price = cleaned_data.get("max")
        if min_price and max_price and (min_price > max_price):
            msg = "max price should be greater then min price"
            self._errors['min'] = self.error_class([msg])
            del cleaned_data['min']
            del cleaned_data['max']
        return cleaned_data


