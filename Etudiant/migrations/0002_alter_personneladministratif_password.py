# Generated by Django 5.1.4 on 2024-12-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personneladministratif',
            name='Password',
            field=models.CharField(max_length=100),
        ),
    ]