from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path('logout-confirmation/', views.logout_confirmation, name='logout_confirmation'),

    # path("complaints/", views.complaints, name="complaints"),
]