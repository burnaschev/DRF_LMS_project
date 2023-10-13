from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, WellViewSet, PaymentsListAPIView, SubscriptionCreateAPIView, SubscriptionDeleteAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'well', WellViewSet, basename='well')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/view/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('subscription/', SubscriptionCreateAPIView.as_view(), name='create-subscription'),
    path('subscription/<int:pk>/', SubscriptionDeleteAPIView.as_view(), name='delete-subscription'),
]

urlpatterns += router.urls
