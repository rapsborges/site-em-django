# Generated by Django 4.0.4 on 2022-05-06 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_episodios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Episodios',
            new_name='Episodio',
        ),
    ]
