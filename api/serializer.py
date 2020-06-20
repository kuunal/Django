from rest_framework import serializers
from register.models import Register, Register

class SnipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'