from django.db import models
from datetime import date


class Installation(models.Model):
    customer_name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    appointment_date = models.DateField()
    date_created = models.DateField(default= date.today)
    date_modified = models.DateField(default= date.today)


    def __str__(self):
        return self.customer_name



class Status(models.Model):

    class StatusIndication (models.Choices):
        REQUESTED = 'Requested'
        IN_PROGRESS = 'In Progress'
        COMPLETE = 'Complete'
        REJECTED = 'Rejected'

    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, choices= StatusIndication.choices, default=StatusIndication.REQUESTED)
    notes = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.status