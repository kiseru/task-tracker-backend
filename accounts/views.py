from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import LoginSerializer, TokenSerializer, UserSerializer


class AuthViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data['username'])
        if user is None or not user.check_password(serializer.validated_data['password']):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user_id=user.id)
        return Response(TokenSerializer(token).data)

    @action(detail=False, permission_classes=(IsAuthenticated,))
    def me(self, request):
        return Response(UserSerializer(request.user).data)
