from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from random import randint

def employee_id_generator():
    rand_int = randint(100000, 999999)
    return rand_int


positions_list = (('Specialist', 'Specialist'), ('Sr Specialist', 'Sr Specialist'), ('Analyst', 'Analyst'),
                  ('Sr Analyst', 'Sr Analyst'), ('Manager', 'Manager'))
departaments_list = (('Sales', 'Sales'), ('Marketing', 'Marketing'), ('Operations', 'Operations'),
                     ('Finance', 'Finance'), ('Human Resources', 'Human Resources'))

class Position(models.Model):
    position = models.CharField(max_length=100, blank=True, null=True)

    @classmethod
    def create(cls, position):
        position = cls(position=position)
        return position


    def __str__(self):
        return f"{self.position}"

class Department(models.Model):
    departament = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.departament}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, default=employee_id_generator)
    position = models.CharField(max_length=100, null=True, choices=positions_list, blank=True)
    departament = models.CharField(max_length=100, null=True, choices=departaments_list, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='users/templates/profile_imgs')

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)