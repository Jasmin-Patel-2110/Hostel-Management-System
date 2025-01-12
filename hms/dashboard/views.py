from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

@login_required
def profile(request):
    user_name = User.get_username(request.user)
    full_name = User.get_full_name(request.user)
    
    # context = {
    #     user_name: user_name,
    #     full_name: full_name
    # }
   
    context = {
        "userName": user_name,
        "fullName": full_name
    }
    return render(request, 'dashboard/profile.html',context=context)

@login_required
def logout_confirmation(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page
    return render(request, 'dashboard/logout_confirmation.html')