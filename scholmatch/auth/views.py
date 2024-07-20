from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from scholmatch.utils.email_util import send_otp_to_user
from scholmatch.auth.models import OTP

class VerifyEmailView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Please provide your email address'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        result = send_otp_to_user(user)
        if not result:
            return Response({'error': 'Failed to send OTP code'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        return Response({'success': 'OK'}, status=status.HTTP_200_OK)

class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp_code = request.data.get('otp_code')
        if not email or not otp_code:
            return Response({'error': 'Please provide your email address and OTP code'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        otp = OTP.objects.filter(user=user, otp_code=otp_code).first()

        if otp and otp.is_expired():
            user.is_active = True
            otp.delete()
            return Response({'message': 'OTP code is valid'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP code or is expired'}, status=status.HTTP_400_BAD_REQUEST)