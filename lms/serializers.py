from rest_framework import serializers

from lms.models import Lesson, Well, Payments, Subscription
from lms.services import create_payment_intent, retrieve_payment_intent
from lms.validators import validator_scam_url


# from lms.validators import validator_scam_url


class LessonSerializers(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validator_scam_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class WellSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializers(source='lessons', many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Well
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lessons.all().count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if obj.well_sub.all().filter(users=user).exists():
            return "Подписан на курс"
        else:
            return "Не подписан"


class PaymentsSerializer(serializers.ModelSerializer):
    payment_stripe = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payments
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get('request')

    def get_payment_stripe(self, obj):
        if self.request.method == 'POST':
            payment_stripe_id = create_payment_intent(obj.amount)
            obj_payment = Payments.objects.get(id=obj.id)
            obj_payment.payment_stripe_id = payment_stripe_id
            obj_payment.save()

            return retrieve_payment_intent(payment_stripe_id)

        if self.request.method == 'GET':
            if not obj.payment_stripe_id:
                return None
            return retrieve_payment_intent(obj.payment_stripe_id)


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
