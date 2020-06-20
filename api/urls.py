from django.urls import include
from .router import router
from rest_framework.compat import path


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]