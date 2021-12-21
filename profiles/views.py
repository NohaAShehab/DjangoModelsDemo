from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from profiles.forms import ProfileForm


# Create your views here.

def storefile(file):
    with open("temp/images.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", context={
            "form": form
        })

    def post(self, request):
        # print(request.FILES["image"])
        submitted = ProfileForm(request.POST, request.FILES["user_image"])
        if submitted.is_valid():
            storefile(request.FILES["user_image"])
            return HttpResponse("fff")

        return render(request, "profiles/create_profile.html", context={
            "form": submitted
        })
