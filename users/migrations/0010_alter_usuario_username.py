# Generated by Django 4.2.8 on 2023-12-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_nombre_usuario_nombres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]