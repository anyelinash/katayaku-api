# Generated by Django 4.2.7 on 2023-11-09 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('codigo_emp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('ruc', models.CharField(max_length=11)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo_usu', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=8)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
                ('codigo_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.empresa')),
            ],
        ),
    ]