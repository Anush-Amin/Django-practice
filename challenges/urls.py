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
    path("", views.index, name="index"),  # this is for url /challenge/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    # here name is used to construct path for url
    
    # variable inside <> can be anything but same name needs to be used in views.py 
    ## as arguement for monthly_challenge
    ## here we can specify the datatype expected
]