# Generated by Django 4.2.13 on 2024-12-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0003_etudiant_nom_etudiant_prenom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
