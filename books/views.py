from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Avg
# Create your views here.
from books.models import Book

def index(request):
    books = Book.objects.all().order_by("-title")
    count= books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "books/index.html", context={
        "books":books,
        "count":count,
        "avg_rating":avg_rating
    })


def bookdetail(request, id):
    # book = Book.objects.get(pk=id)
    book = get_object_or_404(Book,pk=id)


    return render(request, "books/detail.html", context={
        "book": book
    })

