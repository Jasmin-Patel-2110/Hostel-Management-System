from django.urls import include, path

from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('index/', views.home, name='index'),
]
