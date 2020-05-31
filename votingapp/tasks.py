import smtplib

from django.core.mail import send_mail
from django.template.loader import render_to_string

from UniLikes import settings
from UniLikes.celery import app


@app.task
def send_email_task(subject, from_email, to_email, template, args):
    server = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
    server.starttls()
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    html = render_to_string(template, args)
    send_mail(
        subject=subject,
        message='',
        from_email=from_email,
        recipient_list=[to_email],
        html_message=html
    )