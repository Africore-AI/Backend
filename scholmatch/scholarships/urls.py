# scholarships/urls.py

from django.urls import path
from .views import UserProfileView, ScholarshipListView, ScholarshipRecommendationView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('scholarships/', ScholarshipListView.as_view(), name='scholarship-list'),
    path('recommendations/', ScholarshipRecommendationView.as_view(), name='scholarship-recommendations'),
]
