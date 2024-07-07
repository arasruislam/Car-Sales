from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id": "required"}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
