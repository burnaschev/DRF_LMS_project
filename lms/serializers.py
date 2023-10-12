from rest_framework import serializers

from lms.models import Lesson, Well, Payments


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class WellSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializers(source='lessons', many=True, read_only=True)

    class Meta:
        model = Well
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lessons.all().count()


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
