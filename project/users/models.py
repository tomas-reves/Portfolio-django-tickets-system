from django.db import models
from django.contrib.auth.models import User


positions_list = (('Specialist', 'Specialist'), ('Sr Specialist', 'Sr Specialist'), ('Analyst', 'Analyst'),
                  ('Sr Analyst', 'Sr Analyst'), ('Manager', 'Manager'))
departaments_list = (('Sales', 'Sales'), ('Marketing', 'Marketing'), ('Operations', 'Operations'),
                     ('Finance', 'Finance'), ('Human Resources', 'Human Resources'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, choices=positions_list, blank=True)
    departament = models.CharField(max_length=100, null=True, choices=departaments_list, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='users/templates/profile_imgs')

    def __str__(self):
        return f"{self.user.username} profilis"
