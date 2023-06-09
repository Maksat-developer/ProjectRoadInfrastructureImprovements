from rest_framework import serializers
from .models import *


class MessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = "__all__"