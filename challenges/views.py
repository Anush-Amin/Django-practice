from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

#def january(request):
#    return HttpResponse("Eat no meat for entire month")

#def february(request):
#    return HttpResponse("Walk for atleast 20 min everyday!")

#def march(request):
#    return HttpResponse("Learn Django for atleast 20 min everyday!")

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for entire month"
    elif month == 'february':
        challenge_text = "Walk for atleast 20 min everyday!"
    elif month == 'march':
        challenge_text = "Learn Django for atleast 20 min everyday!"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)