from django.shortcuts import render
<<<<<<< HEAD
from .models import Product  # Załóżmy, że masz model Product

def home(request):
    products = Product.objects.all()  # Pobierz wszystkie produkty
    return render(request, 'products/home.html', {'products': products})
=======

# Create your views here.
>>>>>>> b771156e4ff712a61c31eaea92eaea540009bd72
