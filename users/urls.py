from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("signup/", views.signup.as_view(), name="signup"),
]
