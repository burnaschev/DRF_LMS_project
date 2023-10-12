from rest_framework import viewsets
from rest_framework.response import Response

from users.models import User
from users.permission import IsUser
from users.serializers import UserSerializers, PrivateUserSerializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsUser]

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        if user == self.request.user:
            serializer = UserSerializers(user)
        else:
            serializer = PrivateUserSerializers(user)
        return Response(serializer.data)
