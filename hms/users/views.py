from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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
            return redirect('index')  # Change 'index' to your main page URL name
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
            return redirect('index')  # Change 'index' to your main page URL name
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def home(request):
    return render(request, 'users/index.html')