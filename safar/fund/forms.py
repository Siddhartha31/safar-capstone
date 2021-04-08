from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Request

class CreateUserForm(UserCreationForm):
    fullname = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','fullname','phone', 'email', 'password1', 'password2']


class CreateRequest(ModelForm):
    class Meta:
        model = Request
        fields = ['account_id', 'request_category', 'amount', 'desc', 'identity_image', 'image1', 'image2', 'deadline']

class AdminForm(ModelForm):
    class Meta:
        model = Request
        fields = ['admin_msg', 'status']


