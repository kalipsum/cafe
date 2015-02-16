from django import forms


class Filter(forms.Form):
    name = forms.CharField(min_length=3, max_length=30, required=False)
    min = forms.FloatField(required=False, min_value=0)
    max = forms.FloatField(required=False, min_value=0)

