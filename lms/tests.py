from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from lms.models import Lesson, Well, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="test",
            password="2486",
            role='member'
        )
        refresh = RefreshToken.for_user(self.user)

        self.access = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access["access"]}')
        self.lesson = Lesson.objects.create(
            title="test",
            users=self.user
        )

    def test_get_list(self):
        """ Test for getting list fo lesson """

        response = self.client.get(
            reverse('lms:lesson_list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.id,
                        "video_url": self.lesson.video_url,
                        "title": self.lesson.title,
                        "description": self.lesson.description,
                        "preview": self.lesson.preview,
                        "well": self.lesson.well,
                        "users": self.lesson.users_id
                    }
                ]
            }
        )

    def test_lesson_create(self):
        data = {
            "title": "test2"
        }

        response = self.client.post(
            reverse('lms:lesson_create'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)

        self.assertEquals(Lesson.objects.all().count(),
                          2
                          )

    def test_update_lesson(self):
        data = {
            'title': 'update test',
        }

        response = self.client.put(
            reverse('lms:lesson_update', args=[self.lesson.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        response = self.client.delete(reverse('lms:lesson_delete', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="test",
            password="2486",
            role='member'
        )
        refresh = RefreshToken.for_user(self.user)

        self.access = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access["access"]}')
        self.well = Well.objects.create(
            title="test"
        )
        self.subscription = Subscription.objects.create(users=self.user, well=self.well)

    def test_create_subscription(self):
        data = {
            "well": self.well.id,
            "users": self.user.id
        }

        response = self.client.post(
            reverse('lms:create-subscription'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)

        self.assertEquals(Subscription.objects.all().count(),
                          2
                          )

    def test_delete_subscription(self):
        response = self.client.delete(reverse('lms:delete-subscription', args=[self.subscription.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
