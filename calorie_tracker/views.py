

# Create your views here.
from django.shortcuts import render, redirect
from .models import FoodItem
from django.utils import timezone

def index(request):
    today = timezone.now().date()
    foods = FoodItem.objects.filter(date_added=today)
    total = sum(item.calories for item in foods)

    if request.method == "POST":
        name = request.POST.get("name")
        calories = request.POST.get("calories")
        if name and calories:
            FoodItem.objects.create(name=name, calories=int(calories))
            return redirect('index')

    return render(request, "calorie_tracker/index.html", {"foods": foods, "total": total})

def delete_item(request, item_id):
    FoodItem.objects.get(id=item_id).delete()
    return redirect('index')

def reset_day(request):
    FoodItem.objects.filter(date_added=timezone.now().date()).delete()
    return redirect('index')
