from django import forms


class ReviewForm(forms.Form):
    username=forms.CharField(label="User name",max_length=10,min_length=4,
                             error_messages = {
                                 "required":"plz required name "
                             })
