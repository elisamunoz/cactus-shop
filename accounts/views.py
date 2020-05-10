from django.shortcuts import render

def signup_view(request):
    """ This view manages the signup form """
    return render(request, 'signup.html')