from django.urls import path

# from same folder import views
from . import views

urlpatterns = [
    path("january", views.january),
    path("february", views.february)
]