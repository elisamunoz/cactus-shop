from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def signup_view(request):
    """ This view manages the signup form """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            messages.success(request, "You have successfully signed up")
            return redirect("products_list")
        else:
            messages.error(
                request, "Sorry, unable to sign you up at this time")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    """ This view manages the signin """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in")

            return redirect("products_list")
        else:
            messages.error(request, "User or password are incorrect")
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {'form': form})


def logout_view(request):

    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('products_list')


@login_required
def profile_view(request):
    """ View that displays the profile page of a logged in user"""
    return render(request, 'profile.html')
