from django.contrib import admin
from books.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book,BookAdmin)