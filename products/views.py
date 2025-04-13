from django.shortcuts import render
from .models import Product  # Załóżmy, że masz model Product

def home(request):
    products = Product.objects.all()  # Pobierz wszystkie produkty
    return render(request, 'products/home.html', {'products': products})
