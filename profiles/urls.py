from django.urls import path
from profiles.views import CreateProfileView
urlpatterns = [
    path("test",CreateProfileView.as_view(),name="fileupload"),
]