from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import serializers

from appAccounts.models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProjectSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')
