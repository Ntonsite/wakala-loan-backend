from .serializers import (
    UserProfileSerializer,RoleSerializer
)
from .permissions import CheckPermission

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from account_management.models import User,Role
from rest_framework import filters, mixins, status
from rest_framework.response import Response


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(id=self.request.user.pk)
        return query_set

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (CheckPermission, IsAuthenticated,)
    http_method_names = ['get', 'post']


class AllUsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]


class SearchUserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    http_method_names = ['get']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('email',)


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    http_method_names = ['get']
    # def get_queryset(self):
    #     queryset = self.queryset
    #     query_set = queryset.filter(id=self.request.user.pk)
    #     return query_set

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (CheckPermission, IsAuthenticated,)
