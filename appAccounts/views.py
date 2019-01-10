from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from rest_auth.serializers import LoginSerializer
from rest_auth.views import LoginView


User = get_user_model()


class NCSLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(username=username)

        if user:
            if not user.last().is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user.last()
        return attrs

class NCSLoginView(LoginView):
    serializer_class = NCSLoginSerializer