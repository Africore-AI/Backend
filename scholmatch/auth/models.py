from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import os

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.email} - {self.otp_code}'
    
    def is_expired(self):
        expiry_minutes = int(os.getenv("OTP_EXPIRY_MINUTES"))
        expiry_time = self.created_at + timedelta(minutes=expiry_minutes)
        return timezone.now() > expiry_time
