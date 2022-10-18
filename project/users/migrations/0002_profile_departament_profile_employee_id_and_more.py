# Generated by Django 4.0.6 on 2022-10-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='departament',
            field=models.CharField(blank=True, choices=[('Sales', 'Sales'), ('Marketing', 'Marketing'), ('Operations', 'Operations'), ('Finance', 'Finance'), ('Human Resources', 'Human Resources')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='employee_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, choices=[('Specialist', 'Specialist'), ('Sr Specialist', 'Sr Specialist'), ('Analyst', 'Analyst'), ('Sr Analyst', 'Sr Analyst'), ('Manager', 'Manager')], max_length=100, null=True),
        ),
    ]