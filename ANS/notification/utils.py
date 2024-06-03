import time
from django.core.mail import send_mail
from django.conf import settings

# def send_email_to_client(absentee_emails):
#     subject = "Notification: Student Absentee"
#     message = "Dear Parent,\n\nYour child was absent today from college.\n\nBest regards,\nCollege Administration"
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = absentee_emails
#     send_mail(subject, message, from_email, recipient_list)

# Example usage:
# absentee_emails = ["parent1@example.com", "parent2@example.com", "parent3@example.com"]
# send_email_to_client(absentee_emails)


def send_email_to_client():
    subject="Notification: Student Absentee"
    message="Dear Parent,\n\nYour child was absent today from college.\n\nBest regards,\nCollege Administration"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["kolatesanika7@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)