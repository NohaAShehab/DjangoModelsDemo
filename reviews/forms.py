from django import forms
from reviews.models import Review

class ReviewForm(forms.Form):
    username=forms.CharField(label="User name",max_length=10,min_length=4,
                             error_messages = {
                                 "required":"plz required name "
                             })

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = "__all__"
        labels = {
            "username":"Your name",
            "review_text": "Feedback",
            "rating": "Your rating"
        }
        error_messages = {
            "username":{
                "required": "You must provide name here"
            }
        }
