from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from users.forms import OnboardingForm

def register(request):
    """
    This view handles the registration of a new user. If the request is a GET
    request, it renders a registration form. If the request is a POST request, it
    validates the form and creates a new user if the form is valid.

    :param request: The request object
    :return: A HttpResponse object
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('onboarding')  # "profile" main page URL name
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    """
    This view handles the login of an existing user. If the request is a GET
    request, it renders a login form. If the request is a POST request, it
    validates the form and logs in the user if the form is valid.

    :param request: The request object
    :return: A HttpResponse object
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Change 'index' to your main page URL name
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page after logout

@login_required
def onboarding_view(request):
    if request.method == 'POST':
        form = OnboardingForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the dashboard or any other page
            return redirect('profile')
    else:
        form = OnboardingForm()

    return render(request, 'users/onboarding.html', {'form': form})