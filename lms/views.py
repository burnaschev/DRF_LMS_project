from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter

from lms.models import Lesson, Well, Payments, Subscription
from lms.paginators import LMSPaginator
from lms.permission import IsModerator, IsUser
from lms.serializers import LessonSerializers, WellSerializers, PaymentsSerializer, SubscriptionSerializer
from users.models import UserRoles


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsModerator | IsUser]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsUser]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsUser]
    pagination_class = LMSPaginator

    def get_queryset(self):
        if self.request.user.role == UserRoles.MEMBER:
            return Lesson.objects.filter(users=self.request.user)
        return Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsUser]


class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializers
    queryset = Well.objects.all()
    permission_classes = [IsModerator | IsUser]
    pagination_class = LMSPaginator

    def get_queryset(self):
        if self.request.user.role == UserRoles.MEMBER:
            return Well.objects.filter(users=self.request.user)
        return Well.objects.all()

    def get(self, request, *args, **kwargs):
        well = self.get_object()
        serializer = WellSerializers(well)


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsModerator | IsUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('well', 'lesson', 'payment_method',)
    ordering_fields = ('date_payment',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsUser]

    def perform_create(self, serializer):
        new_sub = serializer.save()
        new_sub.users = self.request.user
        new_sub.save()


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsUser]
