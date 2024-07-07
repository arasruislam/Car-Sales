from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
