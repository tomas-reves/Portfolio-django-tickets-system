# Generated by Django 4.0.6 on 2022-11-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_departament_department_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='departament',
            field=models.CharField(blank=True, choices=[('IT', 'IT'), ('Human Resourses', 'Human Resourses'), ('Finance', 'Finance'), ('Operations', 'Operations'), ('Support', 'Support'), ('Finance', 'Finance'), ('Management', 'Management'), ('Test', 'Test'), ('Test2', 'Test2')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, choices=[('Specialist', 'Specialist'), ('Senior', 'Senior'), ('Administrator', 'Administrator'), ('Supervisor', 'Supervisor'), ('Analyst', 'Analyst'), ('Sr Analyst', 'Sr Analyst'), ('Business Analyst', 'Business Analyst'), ('HR', 'HR')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='templates\\profile_imgs'),
        ),
    ]