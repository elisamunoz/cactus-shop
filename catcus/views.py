from django.shortcuts import render, redirect
from products.models import Product
 
def home(request):
    products = Product.object.all().order_by('name')[:4]
    return render(request, 'home.html',  {"products": products})

def about(request):
    return redirect('home', _anchor='about')

def error_page(request):
    return render(request, 'error_page.html')