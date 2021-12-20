from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from reviews.forms import ReviewForm

# Create your views here.

def addreview(request):
    if request.method == 'POST':
        # review= request.POST("username")
        thankyou = reverse("thankyoupage")
        form = ReviewForm(request.POST)
        if form.is_valid():
            print("valid")
            print(form.cleaned_data)
            return HttpResponseRedirect(thankyou)
            # return HttpResponse(form.cleaned_data)
        else:
            form = ReviewForm()
    form = ReviewForm()
    return render(request, "reviews/review.html",context={"form": form})


def thankyou(request):
    return render(request, "reviews/Thank-you.html")
