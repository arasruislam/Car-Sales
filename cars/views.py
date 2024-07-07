from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models


# Create your views here.
def home(request):
    data = models.Car.objects.all()
    brand_id = request.Get.get("brand")

    if brand_id is not None:
        brand = models.Brand.get(pk=brand_id)
        data = models.Car.objects.filter(brand=brand)
    brands = models.Brand.objects.all()
    return render(request, "index.html", {"cars": data, "brand": brands})


def car_details(request, id):
    car = models.Car.objects.get(pk=id)
    comments = car.comments.all()
    if request.method == "POST":
        if request.user.is_authenticated:
            models.Order.objects.create(user=request.user, car=car)
            car.quantity -= 1
            car.save()
            return redirect("profile")
        else:
            return redirect("login")
    return render(request, "car_details.html", {"car": car, "comments": comments})

@login_required
def add_comments(request, id):
    car = models.Car.objects.get(pk = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        models.Comment.objects.create(car = car, name = name, comment = comment_text)
        return redirect("car_details", pk = id)
    return redirect("car_details", pk=id)

