# Generated by Django 5.0 on 2023-12-27 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('ano_criacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artista')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('segundos', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.album')),
            ],
        ),
    ]
