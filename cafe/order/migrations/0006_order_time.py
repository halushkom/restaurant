# Generated by Django 3.0.1 on 2020-02-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Time',
            field=models.TimeField(max_length=10, null=True),
        ),
    ]
