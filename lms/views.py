from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from lms.models import Lesson, Well, Payments
from lms.serializers import LessonSerializers, WellSerializers, PaymentsSerializer
from rest_framework import generics, viewsets


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializers
    queryset = Well.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('well', 'lesson', 'payment_method', )
    ordering_fields = ('date_payment',)
