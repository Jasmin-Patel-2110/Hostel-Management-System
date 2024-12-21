from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('index/', views.home, name='index'),
    path('/', views.home, name='index'),
]
