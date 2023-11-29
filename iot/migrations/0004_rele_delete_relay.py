# Generated by Django 4.2.7 on 2023-11-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0003_relay_delete_dispositivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('topico', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Relay',
        ),
    ]