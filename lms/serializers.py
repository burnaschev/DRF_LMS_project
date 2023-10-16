from rest_framework import serializers

from lms.models import Lesson, Well, Payments, Subscription
from lms.validators import validator_scam_url


# from lms.validators import validator_scam_url


class LessonSerializers(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validator_scam_url], read_only=True)

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
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
