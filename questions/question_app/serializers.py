from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for questions"""
    class Meta:
        model = Question
        fields = "__all__"