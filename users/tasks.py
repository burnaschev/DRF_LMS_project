from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def last_login_check():
    now = timezone.now()
    User.objects.filter(last_login=now - timezone.timedelta(days=30)).update(is_active=False)
