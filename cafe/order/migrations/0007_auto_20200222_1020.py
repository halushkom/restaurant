# Generated by Django 3.0.1 on 2020-02-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Data',
            new_name='Date',
        ),
    ]
