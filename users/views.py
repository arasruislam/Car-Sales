from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms


# Create your views here.
class signup(CreateView):
    template_name = "account.html"
    form_class = forms.UsersForm
    success_url = reverse_lazy("profile.html")


def profile(request):
    return render(request, "profile.html")
