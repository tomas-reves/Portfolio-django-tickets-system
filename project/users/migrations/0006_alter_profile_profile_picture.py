# Generated by Django 4.0.6 on 2022-10-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
