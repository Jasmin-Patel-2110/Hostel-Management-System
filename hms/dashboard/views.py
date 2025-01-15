from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

@login_required
def profile(request):
   
    context = {
        "userName": User.get_username(request.user),
        "fullName": User.get_full_name(request.user),
        "emailId": request.user.email,
    }
    return render(request, 'dashboard/profile.html',context=context)

@login_required
def logout_confirmation(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page
    return render(request, 'dashboard/logout_confirmation.html')