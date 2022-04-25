from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """Serializer for votes"""
    class Meta:
        model = Vote
        fields = "__all__"