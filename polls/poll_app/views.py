from rest_framework import generics
from .models import Poll
from .serializers import PollSerializer


class PollList(generics.ListCreateAPIView):
    """List all polls, or create a new poll"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a poll"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer