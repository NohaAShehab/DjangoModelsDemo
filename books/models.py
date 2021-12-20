from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postalcode}"


# one to one relation author with address
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE, null=True)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()


# 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
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE, null=True, related_name="books")
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    ### utility mehtod
    def __str__(self):
        return f"{self.title} {self.rating}"

    def get_absolute_url(self):
        return reverse("bookdetail", args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        # add validator
