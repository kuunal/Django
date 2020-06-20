from rest_framework import routers
from .view import UserViewSet

router = routers.DefaultRouter()
router.register('api',UserViewSet)