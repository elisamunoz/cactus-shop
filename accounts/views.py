from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    """ This view manages the signup form """
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})