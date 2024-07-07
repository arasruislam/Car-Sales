from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("car_details/<int:id>", views.car_details, name="car_details"),
    path("comment/<int:id>", views.add_comments, name="add_comments"),
]
