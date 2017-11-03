from django.core.mail import send_mail

send_mail('Your Email subject', 'Your Email message.', 'sender_email@example.com', ['recipient_email@example.com'], fail_silently=False)