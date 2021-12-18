from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseNotFound, \
    HttpResponse,HttpResponseRedirect
monthlyChalleng = {
    "jan":"Sleep",
    "feb":"Walk"
}

#Django template lang.

# Create your views here.
def monthly_challenge_number(request, month):
    # redirect to month it self
    months = list(monthlyChalleng.keys())
    if month > len(months):
        return HttpResponseNotFound("plz provide suitable value")
    redirectmonths = months[month-1]
    # return HttpResponse(month)
    redirect = reverse("monthlyChallenge",args=[redirectmonths])
    return HttpResponseRedirect(redirect)

    # return HttpResponseRedirect("/"+redirectmonths)

def monthly_challenge(request, month):
    if month == 'jan':
        challenge = 'Pray Al-Fajr Every day'
    elif month == 'Feb':
        challenge = 'Walk for 30 min daily'
    else:
        return HttpResponseNotFound("No challeng added for this month")
    return HttpResponse(challenge)
