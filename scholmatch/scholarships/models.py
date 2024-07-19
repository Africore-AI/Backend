# scholarships/models.py

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    academic_achievements = models.TextField()
    financial_needs = models.TextField()
    personal_interests = models.TextField()

    def __str__(self):
        return self.user.username

class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    application_deadline = models.DateField()

    def __str__(self):
        return self.name
