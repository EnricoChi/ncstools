from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from appAPIv1.serializers import UserSerializer, GroupSerializer, ProjectSerializer
from appAccounts.models import Project



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    User = get_user_model()
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        token = self.headers.get('token')
        if token is None:
            return
        data = {'token': token}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']
        return Project.objects.filter(user=user)
