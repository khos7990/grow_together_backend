from django.urls import path
from .views import BestMatch, Matches, MatchMaker, MyPlants

urlpatterns = [
    path('bestmatch/', BestMatch.as_view()),
    path('matches/', Matches.as_view()),
    path('matchmaker/', MatchMaker.as_view()),
    # path('plants/delete/', DeletePlant.as_view()),
    path('myplants/', MyPlants.as_view())
]