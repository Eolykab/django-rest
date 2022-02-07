from django.db import models
from datetime import date


class Installation(models.Model):
    """This class represents the Installation model."""

    customer_name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    appointment_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.customer_name

class StatusIndication (models.Choices):
        """This class represents the model choices of Status model for field status"""
        REQUESTED = 'Installation Requested'
        IN_PROGRESS = 'Installation In Progress'
        COMPLETE = 'Instalation Complete'
        REJECTED = 'Instalation Rejected'

class Status(models.Model):
    """This class represents the Installation model."""
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    status = models.CharField(max_length = 40, choices= StatusIndication.choices, default=StatusIndication.REQUESTED)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.status