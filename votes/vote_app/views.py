from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    """List all votes, or create a new vote"""
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a vote"""
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer