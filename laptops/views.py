from django.shortcuts import render
from laptops.models import Laptop


#def home(request):
#    laptops = Laptop.objects.all()
#    return render(request, "index.html")


def home(request):
    queryset = Laptop.objects.all()
    return render(request, "index.html", {'laptops': queryset})
