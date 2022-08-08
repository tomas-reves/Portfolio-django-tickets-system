from django.test import TestCase
from django.contrib.auth.models import User


def pvz():
    users = User.objects.all()
    user_list = []
    for user in users:
        print(user)

pvz()