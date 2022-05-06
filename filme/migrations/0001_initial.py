# Generated by Django 4.0.4 on 2022-05-05 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(upload_to='thumb_filmes')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000)),
                ('categoria', models.CharField(choices=[('ANALISES', 'Análises'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'Outros')], max_length=15)),
                ('visualizacoes', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
