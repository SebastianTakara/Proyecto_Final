# Generated by Django 4.0.5 on 2022-07-24 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=200)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=80)),
                ('fecha', models.CharField(max_length=8)),
            ],
        ),
    ]
