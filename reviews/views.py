from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from reviews.forms import ReviewForm, ReviewModelForm
from django import views
from django.views.generic import TemplateView
from reviews.models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, \
    CreateView, UpdateView, DeleteView


# Create your views here.
# class ReviewView(views.View):
#     def get(self,request):
#         form = ReviewModelForm()
#         return render(request, "reviews/review.html", context={"form": form})
#
#     def post(self, request):
#         form = ReviewModelForm(request.POST)
#         form.save()
#         thankyou = reverse("thankyoupage")
#         return HttpResponseRedirect(thankyou)
#


def addreview(request):
    if request.method == 'POST':
        # review= request.POST("username")
        thankyou = reverse("thankyoupage")
        # form = ReviewForm(request.POST)
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return HttpResponseRedirect(thankyou)
            # return HttpResponse(form.cleaned_data)
        else:
            form = ReviewForm()
    form = ReviewModelForm()
    return render(request, "reviews/review.html", context={"form": form})


def thankyou(request):
    return render(request, "reviews/Thank-you.html")


# class ThankYouView(views.View):
#     def get(self, request):
#         return render(request, "reviews/Thank-you.html")


# dealing with get method
# pass context
class ThankYouView(TemplateView):
    template_name = "reviews/Thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Good morning"
        return context


# class ReviewListView(TemplateView):
#     template_name = "reviews/reviewslist.html"
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context["reviews"] =Review.objects.all()
#         return context

class ReviewListView(ListView):
    template_name = "reviews/reviewslist.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        basequery = super().get_queryset()
        data = basequery.filter(id__gte=4)
        return data


# class SingleReviewTemplateView(TemplateView):
#     template_name = "reviews/singleReview.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviewpage = kwargs["id"]
#         context["review"] =Review.objects.get(pk=reviewpage)
#         return context

class SingleReviewTemplateView(DetailView):
    template_name = "reviews/singleReview.html"
    model = Review  # note to use the model in lowercase in the template page
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# form view
# class ReviewView(FormView):
#     form_class = ReviewModelForm
#     template_name = "reviews/review.html"
#
#     def post(self, request):
#         form = ReviewModelForm(request.POST)
#         form.save()
#         thankyou = reverse("thankyoupage")
#         return HttpResponseRedirect(thankyou)


# class ReviewView(FormView):
#     form_class = ReviewModelForm
#     template_name = "reviews/review.html"
#     success_url = "reviews/thank-you"
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    form_class = ReviewModelForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

