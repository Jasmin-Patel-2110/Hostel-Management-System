from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('onboarding/', views.onboarding_view, name='onboarding'),
    # path('index/', views.logout_view, name='logout'),
]
