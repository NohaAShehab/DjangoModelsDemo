from django.urls import path, include
from books.views import index, bookdetail

urlpatterns = [
    path("index", index, name="bookindex"),
    path("<int:id>", bookdetail, name="bookdetail")
]