# Generated by Django 4.0.5 on 2022-06-24 07:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_remove_contato_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
