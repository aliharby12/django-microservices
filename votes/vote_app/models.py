from django.db import models


class Vote(models.Model):
    """
    Model for votes
    """
    poll_id = models.PositiveIntegerField()
    choice_id = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id}'
