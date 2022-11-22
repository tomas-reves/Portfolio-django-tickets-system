from django.db import models
from random import randint, choice
from django.utils import timezone
import string
from django.contrib.auth.models import User


def id_gen():
    rand_letter = choice(string.ascii_letters).upper()
    rand_int = randint(1000, 9999)
    return rand_letter + str(rand_int)

def all_users_list():
    all_users = User.objects.values()
    users_tuple = []
    for user in all_users:
        users_lists_items = []
        users_lists_items.append(user['username'])
        users_lists_items.append(user['username'])
        users_lists_items = tuple(users_lists_items)
        users_tuple.append(users_lists_items)
    users_tuple = tuple(users_tuple)
    return users_tuple

def admin_users_list():
    all_users = User.objects.values()
    users_tuple = []
    for user in all_users:
        if user['is_staff'] == True:
            users_lists_items = []
            users_lists_items.append(user['username'])
            users_lists_items.append(user['username'])
            users_lists_items = tuple(users_lists_items)
            users_tuple.append(users_lists_items)
        admin_users_tuple = tuple(users_tuple)
    return admin_users_tuple

class Ticket(models.Model):

    STATUS_CHOICES = (('Open', 'Open'), ('Pending', 'Pending'), ('Resolved', 'Resolved'), ('Closed', 'Closed'))
    URGENCY_CHOICES = (('Urgent', 'Urgent'), ('High', 'High'), ('Moderate', 'Moderate'), ('Low', 'Low'))

    id = models.IntegerField(primary_key=True)
    user_ticket_creator = models.CharField(max_length=50, null=True, choices=all_users_list())
    numb = models.CharField(max_length=50, default=id_gen)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200)
    date_created = models.DateField(default=timezone.now, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS_CHOICES, default='Open')
    urgency = models.CharField(max_length=50, null=True, choices=URGENCY_CHOICES, blank=True)
    status_date = models.DateField(default=timezone.now, null=True)
    owner = models.CharField(max_length=50, null=False, choices=admin_users_list())

    def __str__(self):
        return f"{self.numb}"
