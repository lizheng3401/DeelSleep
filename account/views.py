from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from .models import User
from .serializers import UserSerializer
from utils.permissions import IsAdminOrUpdateSelf
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        # Token定制化
        re_dict = serializer.data
        paylaod = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(paylaod)
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

