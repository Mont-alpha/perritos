# Generated by Django 4.2.5 on 2024-10-18 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='perritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_perrito', models.CharField(max_length=100)),
                ('edad', models.DateField()),
                ('raza', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
    ]
