from rest_framework import serializers

from lms.serializers import PaymentsSerializer
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='user', many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'payments',)


class PrivateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)
