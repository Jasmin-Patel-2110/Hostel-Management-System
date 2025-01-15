from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

from users.models import Student


@login_required
def profile(request):
   
    student = get_object_or_404(Student, enrollment_number=request.user.username)  # Assuming username is enrollment number
    isSuperuser = request.user.is_superuser
    
    # context = {
    #     "userName": User.get_username(request.user),
    #     "fullName": User.get_full_name(request.user),
    #     "emailId": request.user.email,
    # }
    return render(request, 'dashboard/profile.html',context={"student": student, "isSuperuser":isSuperuser})

@login_required
def logout_confirmation(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page
    return render(request, 'dashboard/logout_confirmation.html')

def complains(request):
    return render(request,'dashboard/complains.html')

def payments(request):
    return render(request,'dashboard/payments.html')