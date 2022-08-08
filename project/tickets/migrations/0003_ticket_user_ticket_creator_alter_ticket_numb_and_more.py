# Generated by Django 4.0.6 on 2022-08-06 19:16

from django.db import migrations, models
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_numb'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user_ticket_creator',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='numb',
            field=models.CharField(default=tickets.models.id_gen, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='owner',
            field=models.CharField(choices=[('tomas-reves', 'tomas-reves'), ('test-user', 'test-user'), ('vardenis.pavardenis', 'vardenis.pavardenis'), ('tomas.reves', 'tomas.reves')], max_length=50, null=True),
        ),
    ]
