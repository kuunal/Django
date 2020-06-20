# from rest_framework import Response
from rest_framework import status
# from rest_framework import api_view
from .serializer import SnipperSerializer
from rest_framework import routers, viewsets
from register.models import Register as r
from api import serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = r.objects.all()
    serializer_class = SnipperSerializer 
