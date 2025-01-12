from django.urls import path
from . import views

urlpatterns = [
    # path("", views.dashboard_home, name="dashboard_home"),
    path("", views.profile, name="profile"),
    # path("complaints/", views.complaints, name="complaints"),
]