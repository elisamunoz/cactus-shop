from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages, auth


def signup_view(request):
    """ This view manages the signup form """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect("products_list")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


