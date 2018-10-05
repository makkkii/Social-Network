from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, required=True, label='First Name')
    last_name = forms.CharField(max_length=254, required=True, label='Last Name')
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    #dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2018)))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')