from django.db import models
from random import randint, choice
from django.utils import timezone
import string

def id_gen():
    rand_letter = choice(string.ascii_letters).upper()
    rand_int = randint(1000, 9999)
    return rand_letter + str(rand_int)

class Ticket(models.Model):
    STATUS_CHOICES = (('Open', 'Open'), ('Pending', 'Pending'), ('Resolved', 'Resolved'), ('Closed', 'Closed'))
    URGENCY_CHOICES = (('Urgent', 'Urgent'), ('High', 'High'), ('Moderate', 'Moderate'), ('Low', 'Low'))

    id = models.IntegerField(primary_key=True)
    user_ticket_creator = models.CharField(max_length=50, null=True, choices=[])
    numb = models.CharField(max_length=50, default=id_gen)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200)
    date_created = models.DateField(default=timezone.now, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS_CHOICES, default='Open')
    urgency = models.CharField(max_length=50, null=True, choices=URGENCY_CHOICES, blank=True)
    status_date = models.DateField(default=timezone.now, null=True)
    owner = models.CharField(max_length=50, null=False, choices=[])

    def __str__(self):
        return f"{self.numb}"
