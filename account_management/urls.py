from django.urls import path, include
from .views import (
    UserProfileViewSet,RoleViewSet,
    SearchUserProfileViewSet, AllUsersViewSet
)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('me', UserProfileViewSet)
router.register('all', AllUsersViewSet)
router.register('search', SearchUserProfileViewSet)
router.register('role', RoleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
