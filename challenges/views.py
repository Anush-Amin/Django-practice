from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "febraury": "Walk for atleast 20 min everyday!",
    "march": "Learn Django for atleast 20 min everyday!",
    "april": "Eat no meat for entire month",
    "may": "Walk for atleast 20 min everyday!",
    "june": "Learn Django for atleast 20 min everyday!",
    "july": "Eat no meat for entire month",
    "august": "Walk for atleast 20 min everyday!",
    "september": "Learn Django for atleast 20 min everyday!",
    "october": "Eat no meat for entire month",
    "november": "Walk for atleast 20 min everyday!",
    "december": None
}

# Create your views here.

#def january(request):
#    return HttpResponse("Eat no meat for entire month")

#def february(request):
#    return HttpResponse("Walk for atleast 20 min everyday!")

#def march(request):
#    return HttpResponse("Learn Django for atleast 20 min everyday!")

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    ## note: ctrl+/ to comment multiple lines
    ## instead of using for loop here we can use the for tag in index.html page
    return render(request, "challenges/index.html", {
        "months": months # this "months" will be used in index.html for tags
    })

def monthly_challenge_by_number(request, month):
    """Here if number is entered in the URL it will
    be redirected to the month corresponding to that number
    Ex: if http://127.0.0.1:8000/challenges/2
    it will be redirected to http://127.0.0.1:8000/challenges/february"""
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    #return HttpResponseRedirect("/challenges/"+redirect_month)
    ## instead of hard-coding the url as above we can use 
    ## the main use of this is even if we change the url path in urls.py (inside monthly_challenges) we still get the response
    ## try this by changing "challenge/" to "anyname/"
    redirect_path = reverse("month-challenge", args=[redirect_month]) # this will build path /challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        ## instead of using above 2 lines we can use
        return render(request, "challenges/challenge.html", {
             "text": challenge_text,
             "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    