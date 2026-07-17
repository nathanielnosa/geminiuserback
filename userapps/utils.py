from django.core.mail import send_mail
from django.conf import settings

def sendEmail(email,fullname):
    subject = f'Welcome Message from Gemini'
    message = f'''
                    Welcome {fullname},
                    Thank you for registering with us. We are excited to have you on board!
                    Our team will reach out to you.
                '''

    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)