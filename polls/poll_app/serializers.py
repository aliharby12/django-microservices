from rest_framework import serializers
from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    """Serializer for polls"""
    class Meta:
        model = Poll
        fields = "__all__"