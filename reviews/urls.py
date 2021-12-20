from django.urls import path
from reviews.views import addreview,thankyou

urlpatterns=[
    path("review",addreview, name="addreview"),
    path("thank-you", thankyou, name="thankyoupage")

]