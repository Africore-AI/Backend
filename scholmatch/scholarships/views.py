# scholarships/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import UserProfile, Scholarship
from .serializers import UserProfileSerializer, ScholarshipSerializer
from transformers import pipeline

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile

class ScholarshipListView(generics.ListCreateAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScholarshipRecommendationView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        profile = self.request.user.userprofile
        # Integrate Hugging Face API to get recommendations based on profile
        recommendations = get_scholarship_recommendations(profile)
        return Response(recommendations)

def get_scholarship_recommendations(profile):
    nlp = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')
    profile_text = f"Academic Achievements: {profile.academic_achievements}, Financial Needs: {profile.financial_needs}, Personal Interests: {profile.personal_interests}"
    recommendations = nlp(profile_text)
    return recommendations
