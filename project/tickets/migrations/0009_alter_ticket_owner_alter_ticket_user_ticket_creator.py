# Generated by Django 4.0.6 on 2022-11-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_alter_ticket_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='owner',
            field=models.CharField(choices=[('tomas-reves', 'tomas-reves'), ('admin-2', 'admin-2'), ('mantas.petraitis', 'mantas.petraitis'), ('jonas.kazlauskas', 'jonas.kazlauskas'), ('petras.nauseda', 'petras.nauseda'), ('justina.zukauskaite', 'justina.zukauskaite'), ('simona.paulauskaite', 'simona.paulauskaite'), ('andrius.andriukaitis', 'andrius.andriukaitis')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user_ticket_creator',
            field=models.CharField(choices=[('tomas-reves', 'tomas-reves'), ('vardenis.pavardenis', 'vardenis.pavardenis'), ('admin-2', 'admin-2'), ('mantas.petraitis', 'mantas.petraitis'), ('jonas.kazlauskas', 'jonas.kazlauskas'), ('petras.nauseda', 'petras.nauseda'), ('justina.zukauskaite', 'justina.zukauskaite'), ('simona.paulauskaite', 'simona.paulauskaite'), ('jonas.paulauskas', 'jonas.paulauskas'), ('dominyka.morkunaite', 'dominyka.morkunaite'), ('mantas.stonkus', 'mantas.stonkus'), ('martynas.bigas', 'martynas.bigas'), ('justinas.pocius', 'justinas.pocius'), ('petras.petraitis', 'petras.petraitis'), ('andrius.andriukaitis', 'andrius.andriukaitis'), ('kipras.naujanis', 'kipras.naujanis')], max_length=50, null=True),
        ),
    ]
