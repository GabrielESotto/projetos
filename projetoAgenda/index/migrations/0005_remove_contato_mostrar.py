# Generated by Django 4.0.5 on 2022-06-24 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_contato_mostrar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='mostrar',
        ),
    ]
