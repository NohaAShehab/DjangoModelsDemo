from django.urls import path, reverse
from monthly_challenge.views import monthly_challenge, monthly_challenge_number


urlpatterns = [
    path('<int:month>', monthly_challenge_number),
    path('<str:month>', monthly_challenge, name="monthlyChallenge"),

]