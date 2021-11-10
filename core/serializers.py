from rest_framework import serializers
from core.models import list


class listserializer(serializers.ModelSerializer):
    class Meta:
        model = list
        fields = '__all__'
