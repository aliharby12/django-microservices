from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    """List all questions, or create a new question"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a question"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer