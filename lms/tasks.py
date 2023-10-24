from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from lms.models import Well, Subscription


@shared_task
def send_mail_course_update(well_id):
    well = Well.objects.get(pk=well_id)
    subscription = Subscription.objects.filter(well=well_id)
    for sub in subscription:
        send_mail(
            subject=f"Обновление курса {well.title}",
            message=f"В данном курсе обновление {well.title}, посмотрите",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.users.email],
            fail_silently=True
        )
