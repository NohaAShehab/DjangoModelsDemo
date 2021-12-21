from django.urls import path

import reviews.views
from reviews.views import addreview,thankyou

urlpatterns=[
    # path("review",addreview, name="addreview"),
    path("review", reviews.views.ReviewView.as_view(), name="addreview"),

    # path("thank-you", thankyou, name="thankyoupage")
    path("thank-you", reviews.views.ThankYouView.as_view(), name="thankyoupage"),
    path("list", reviews.views.ReviewListView.as_view(), name="listreiviews"),
    # path("list/<int:id>", reviews.views.SingleReviewTemplateView.as_view(), name="thankyoupage")
    path("list/<int:pk>", reviews.views.SingleReviewTemplateView.as_view(), name="singlereview")

]