# Generated by Django 4.0.6 on 2022-11-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_department_id_alter_position_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='departament',
            new_name='department',
        ),
    ]
