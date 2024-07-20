import random
from django.core.mail import EmailMessage
from django.conf import settings
from scholmatch.auth.models import OTP
from django.utils import timezone


def generate_otp_code():
    return random.randint(100000, 999999)

def send_email(to_email, message, subject):   
    try:
        email = EmailMessage(
            subject,
            message,
            [to_email],
        )
        email.send(fail_silently=False) 
        return True
    except Exception as e:
        return False

def send_otp_to_user(to_user):
    subject = 'Your OTP Code'
    message = f'Dear User,\n\nYour OTP code is {otp_code}. Use this code to complete your verification process. Do not share this code with anyone.\n\nBest Regards,\nYour Company Name'
    
    otp_code = generate_otp_code()
    
    otp_instance, created = OTP.objects.get_or_create(user=to_useruser, defaults={'otp_code': otp_code})

    if not created:

        otp_instance.otp_code = otp_code
        otp_instance.created_at = timezone.now() 
        otp_instance.save()

    check = send_email(to_user.email, message, subject)

    return check
