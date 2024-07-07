from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm, UserEditForm
from cars.models import Order
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CreateUserForm()
    return render(request, "account.html", {"form": form, "type": "Register"})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]

            user = authenticate(username=user_name, password=user_pass)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("index")
            else:
                messages.warning(request, "Login informtion incorrect")
                return redirect("register")
    else:
        form = AuthenticationForm()
    return render(request, "account.html", {"form": form, "type": "Login"})

def user_logout(request):
    logout(request)
    return redirect("index")

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserEditForm(instance=request.user)
    return render(request, "profile.html", {"form": form, "order": orders})
