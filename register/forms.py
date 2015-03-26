from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(min_length=3, max_length=30)
    city = forms.CharField(max_length=70)
    street = forms.CharField()
    house = forms.CharField(max_length=10)
    flat = forms.CharField(max_length=10, required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()

    def save(self, commit=True):
        g = self.clean()
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.city = self.cleaned_data["city"]
        user.street = self.cleaned_data["street"]
        user.house = self.cleaned_data["house"]
        user.flat = self.cleaned_data["flat"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone_number = self.cleaned_data["phone_number"]
        if commit: user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'city', 'street','house' , 'flat','first_name','last_name','phone_number')


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=30)
    password = forms.CharField(min_length=3, max_length=30, widget=forms.PasswordInput())
