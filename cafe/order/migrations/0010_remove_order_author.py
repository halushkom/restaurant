# Generated by Django 3.0.1 on 2020-03-12 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20200227_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='author',
        ),
    ]
