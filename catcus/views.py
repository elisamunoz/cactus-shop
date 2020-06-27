from django.shortcuts import render, redirect
from products.models import Product
 
def home(request):
    products = Product.object.all().order_by('name')[:4]
    return render(request, 'home.html',  {"products": products})

def about(request):
    return render(request, 'about.html')

def error_page(request):
    return render(request, '404.html')