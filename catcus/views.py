from django.shortcuts import render, redirect

 
def home(request):
    return render(request, 'home.html')

def about(request):
    return redirect('home', _anchor='about')

def error_page(request):
    return render(request, 'error_page.html')