from django.urls import path

# from same folder import views
from . import views

urlpatterns = [
    #path("january", views.january),
    #path("february", views.february),
    #path("march", views.march),
    # if we follow the above lines of code, we need to
    ## write for all month individually
    ## It can be done dynamically using the placeholder 
    ## as given below
    path("<month>", views.monthly_challenge)
    # variable inside <> can be anything but same name needs to be used in views.py 
    ## as arguement for monthly_challenge
]